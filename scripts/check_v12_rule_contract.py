#!/usr/bin/env python3
"""Compare archived rule text contracts, not referee runtime behavior."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
TITLES = [
    '赛事概况', '赛前公布、检录与代码版本', '比赛流程、时长与晋级',
    '地图、视野、资源与基础属性', 'Tick、动作提交与结算顺序', '四种动作',
    '阵亡、复活与效果保留', '自然语言随机事件', '第一阶段：基础自主采集',
    '第二阶段：对抗、任务与计分', '统一 AI 服务', '选手接口与信息边界',
    '合法策略、禁止行为与处罚', '成绩确认、申诉与故障', '规则解释',
]


def normalized(text):
    text = re.sub(r'^\s*\d+\s*$', '', text, flags=re.M)
    return re.sub(r'[\s\ufeff]+', '', text)


def sections(path):
    text = path.read_text().replace('\f', '\n')
    text = text[text.index('\n1. 赛事概况') + 1:]
    matches = [m for m in re.finditer(r'(?m)^(\d{1,2})\. ([^\n]+)', text)
               if 1 <= int(m[1]) <= len(TITLES)
               and m[2] == TITLES[int(m[1]) - 1]]
    assert [int(m[1]) for m in matches] == list(range(1, 16))
    return {m[1]: normalized(text[m.start():matches[i + 1].start()
                                if i + 1 < len(matches) else len(text)])
            for i, m in enumerate(matches)}


old = sections(ROOT / 'materials/releases/v1.1/extracted/rules.txt')
new_path = ROOT / 'materials/releases/v1.2/extracted/rules.txt'
new = sections(new_path)
unchanged = ['2', '3', '4', '5', '6', '9', '10', '11', '13', '14']
for section in unchanged:
    assert old[section] == new[section], 'unexpected change in section ' + section
phrases = ['语言无限制', '推荐使用C++17及以上', '复活机制如下',
           '障碍只排除落点，不阻断选点搜索', '但是资源格可以复活',
           '按席位A→B→C→D', '生成区域多数为(11,11)-(13,13)',
           '部分地图存在特殊变化', '代码仓库、技术报告', '如何ai协同开发']
compact = normalized(new_path.read_text())
for phrase in phrases:
    assert phrase in compact, phrase
pdf = ROOT / 'materials/releases/v1.2/original/competition-rules-v1.2.pdf'
assert hashlib.sha256(pdf.read_bytes()).hexdigest() == (
    'd902e26381166aefe8dedc79a3655b583dc4ce863a3bb0024a8a2e9cad465c57')
result = {
    'method': '按精确主章节标题切分15节，去独立页码、空白和BOM；不把章节内数字列表当主标题',
    'sections': [{'section': str(i), 'normalized_equal': old[str(i)] == new[str(i)]}
                 for i in range(1, 16)],
    'required_phrase_checks': [{'phrase': p, 'present': True} for p in phrases],
    'original_pdf_sha256_verified': True,
    'limits': '第12节表格/示例排版、第15节尾文字另经人工复核；只做文档一致性检查，未验证裁判运行',
}
print(json.dumps(result, ensure_ascii=False, indent=2))
