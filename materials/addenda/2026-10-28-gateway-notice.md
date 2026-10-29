# 用户转贴的正式网关新公告（2026-10-28）

来源：本轮用户消息。未取得主办方公告独立URL，不把本归档说成官网抓取。

当前正式网关没有主动关闭思考。除model外其余请求字段直接转发。按DeepSeek官方接口，思考默认开启。关闭时，在请求JSON顶层加入：

```json
{"thinking":{"type":"disabled"}}
```

当前网关没有对LLM请求体设置字段白名单。选手需要使用POST /v1/chat/completions，携带本场Authorization: Bearer令牌；请求符合上游模型接口，遵守配额、并发和大小限制。thinking、temperature、max_tokens、response_format由选手填写，网关转发，上游判断是否合法。模型统一deepseek-flash。

用户粘贴的请求示例：

```json
{
  "model":"deepseek-flash",
  "thinking":{"type":"disabled"},
  "response_format":{"type":"json_object"},
  "messages":[{"role":"user","content":"请只输出 JSON，格式示例：{\"action\":\"move\",\"direction\":\"up\"}"}],
  "max_tokens":512
}
```

用户要求先完成当前工作，再处理本公告。本次已经按顺序执行。示例512不自动解读为比赛硬上限；示例动作JSON也不自动替换当前公告解释契约。
