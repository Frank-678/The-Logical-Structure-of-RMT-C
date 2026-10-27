# 已执行的静态校验

新增[PDF覆盖](releases/v1.1/pdf-reading-inventory.json)、[发行包差异](releases/v1.1/package-diff.json)、三份全文diff、[24项算术结果](releases/v1.1/scoring-examples.json)。旧已验证文件按远端Git对象保留，新7个原件和新manifest16文件哈希均核对；不代表ROS或引擎运行通过。

运行 python3 scripts/verify_materials.py 核对八份原始附件和练习包manifest的16个文件；运行 python3 scripts/check_links.py 检查自撰Markdown内部链接。结果见 materials-verification.json、link-check.json。完整文件哈希清单见 file-manifest.json（不包含清单自身）。

2026-10-21新增两张群内截图，登记为CHAT-01/02，按原字节归档并加入catalog哈希检查。链接检查覆盖新增自撰转录，不改原始课程/程序资料。截图与PDF赛程交叉核对通过只代表记录一致，不代表复活行为或有线联调已经运行验收。

这不代表ROS运行、真实AI请求或比赛策略已通过测试。PDF原始页数与提取记录保存在pdf-extraction-inventory.json。原课程材料内部的历史链接和引用保持原样，不当作本次自撰导航。

2026-10-27新增[对话与实施记录](../docs/18-conversation-and-implementation.md)及[21项代码提交证据](implementation-commits-2026-10-27.json)。独立C++核心、固定HTTP、原版转发处理器夹具和ASan/UBSan已有对应通过记录；ROS/Humble、裁判二进制及真实LLM尚未联调。不同证据层级见该文第12节。
