// 研究夹具：只验证两步采集的评价盲点，不模拟战斗、事件、AI资格或整场胜率。
#include "rmtc_bot/strategy.hpp"
#include "rmtc_bot/scoring.hpp"
#include <array>
#include <cmath>
#include <iostream>
#include <map>
#include <stdexcept>
#include <string>
#include <vector>

namespace { // 只供本文件使用的固定场景与两步穷举。
using Json = nlohmann::json; // 构造公开感知和输出证据。
using Cell = std::pair<int, int>; // 测试端的真实[x,y]位置。
using Resources = std::map<Cell, int>; // 测试端尚未收集的资源；不是策略的额外输入。
constexpr std::array<Cell, 4> steps = {{{0,-1}, {1,0}, {0,1}, {-1,0}}}; // 上右下左。
constexpr std::array<const char *, 4> names = {{"up", "right", "down", "left"}};
const Resources initial = {{{4,3},20}, {{5,4},10}, {{6,4},20}}; // 上20；右10后面再有20。

Json perception(int tick, Cell position, const Resources &remaining, double current_r,
                const Json &receipt) {
  // 只提供本队感知：无敌车、无墙、无事件、无任务，地图9×9、视野半径4。
  Json p = {{"session_id", "two-tick-fixture"}, {"tick", tick}, {"vision_radius", 4},
            {"map", {{"width",9}, {"height",9}}},
            {"self", {{"position", {position.first,position.second}}, {"alive",true},
                      {"hp",100}, {"protected",false}, {"last_action",receipt}}},
            {"visible_entities", Json::array()}, {"missions", Json::array()},
            {"event_text", ""}, {"score", {{"resource_value",current_r},
                      {"effective_damage",0}, {"mission_completed_ids",Json::array()}}}};
  if (tick == 0) p["self"]["position_reason"] = "initial";
  for (const auto &[cell,value] : remaining) {
    const int dx = cell.first-position.first, dy = cell.second-position.second;
    if (std::abs(dx)>4 || std::abs(dy)>4) continue;
    std::string grid; // 协议要求每个实体独立一张9×9相对位置图。
    for (int y=0; y<9; ++y) {
      if (y) grid += '\n';
      for (int x=0; x<9; ++x)
        grid += x==4 && y==4 ? '1' : x==4+dx && y==4+dy ? '2' : '0';
    }
    p["visible_entities"].push_back({{"type",value==20 ? "resource_high" : "resource_normal"},
                                   {"value",value}, {"position",grid}});
  }
  return p;
}

int collect(Cell position, Resources &remaining) {
  // 此夹具只有成功移动后的存活采集；同一资源从集合删除，不重复计分。
  const auto found = remaining.find(position);
  if (found==remaining.end()) return 0;
  const int value = found->second;
  remaining.erase(found);
  return value;
}

Json probe(double initial_r) {
  Strategy strategy(2); // 运行当前真实策略，不替换其目标评分。
  Resources remaining = initial;
  Cell position{4,4};
  double gathered = 0; // 本场景新增R，不含场景开始前的R。
  Json actions = Json::array(), receipt; // 实际策略动作和下一帧确认的上一动作回执。
  for (int tick=0; tick<2; ++tick) {
    const auto action = strategy.decide(perception(tick,position,remaining,initial_r+gathered,receipt));
    actions.push_back({{"action",action}, {"reason",strategy.reason()}});
    int direction = -1;
    if (action.value("action",std::string())=="move") {
      for (int i=0; i<4; ++i) if (action.at("direction")==names[i]) direction=i;
      if (direction<0) throw std::runtime_error("invalid fixture move");
      position.first += steps[direction].first;
      position.second += steps[direction].second;
    }
    gathered += collect(position,remaining);
    receipt = {{"tick",tick}, {"action",action.at("action")}, {"moved",direction>=0}};
  }
  // 固定两步穷举4×4个MOVE序列，仅作为此静态小场景的对照答案。
  // 不调用practice、不读隐藏地图；不是已实施的新参赛算法。
  double best_r = -1;
  Json best_paths = Json::array();
  for (int first=0; first<4; ++first) for (int second=0; second<4; ++second) {
    Resources test_remaining = initial;
    Cell test_position{4,4};
    double test_r = 0;
    for (const int step : {first,second}) {
      test_position.first += steps[step].first;
      test_position.second += steps[step].second;
      test_r += collect(test_position,test_remaining);
    }
    if (test_r>best_r) { best_r=test_r; best_paths=Json::array(); }
    if (test_r==best_r) best_paths.push_back({names[first],names[second]});
  }
  const double baseline_score = rmtc::score_delta(initial_r,gathered,120,30);
  const double comparison_score = rmtc::score_delta(initial_r,best_r,120,30);
  if (std::abs(gathered-20)>1e-9 || std::abs(best_r-30)>1e-9)
    throw std::runtime_error("baseline behavior or fixture changed; review expected result");
  if (std::abs((comparison_score-baseline_score)-(initial_r==0 ? 2.5 : 0.0))>1e-9)
    throw std::runtime_error("capped score comparison changed");
  return {{"initial_R",initial_r}, {"horizon",2}, {"enumerated_move_sequences",16},
          {"baseline_actions",actions}, {"baseline_added_R",gathered},
          {"baseline_official_resource_score_delta",baseline_score},
          {"max_resource_sequence_added_R",best_r}, {"max_resource_sequences",best_paths},
          {"comparison_official_resource_score_delta",comparison_score},
          {"official_score_gap",comparison_score-baseline_score}};
}
} // namespace

int main() {
  std::cout << Json{{"scope","two synthetic collection cases; no match, combat, events or AI"},
                   {"cases", {probe(0),probe(110)}}}.dump(2) << '\n';
}
