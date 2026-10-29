# ChatGPT离线日志与补跑：2026-10-29

这里归档实际运行产物。离线自建裁判不代表原版DDS实战，也没有付费模型调用。代码与全部参数身份见[run-manifest.json](run-manifest.json)、[versions.json](versions.json)、[engine.json](engine.json)。

| 批次 | 实际范围与结果 |
| --- | --- |
| 原联赛 | 65c8714与8da0ede各144，共288个版本×局面；终局报告齐全，逐帧旧tape仅220完整、68截断 |
| 68补跑 | 原engine二进制SHA核对通过、相同冻结worker/场景/种子；68终局world/result/rank等全部一致；首次56完整/12仍截断，原件与检查均保留 |
| 最终回放归档 | 12条再在临时目录重跑；校验实际gzip字节及逐Tick后写入归档；最终68条从完成的tar.xz再解压逐条验证通过 |
| 本轮回归 | 19:43:53–19:44:35，六条命令全部exit0，58次定向回归及核心/规则/原版HTTP固定上游；完整stdout/stderr/命令/退出码见regressions |
| 用户新想法短场景 | 七份夹具通过：纯MOVE争格、改攻击、当前策略墙角、反向换位失败、两敌MOVE阵亡/DEFEND保一Tick、隔墙普通攻击 |

旧gzip截断原因尚未定位。终局JSON齐全不能替代完整回放，补跑不算独立样本。全部原文件逐字节封装保留，没有修补旧gzip尾部或补造Tick。首次补跑现场保存在首次补跑归档，最终完整回放在verified归档。

## 文件

- [original-report.md](original-report.md)：原288局可读全表。
- [old-tape-integrity.json](old-tape-integrity.json)：288条原tape的完整性与缺失Tick范围。
- [raw-file-manifest.json](raw-file-manifest.json)：原full-league/causal-window/new-probe共1527个文件的大小和SHA256。
- [recovered-tape-integrity.json](recovered-tape-integrity.json)：最终68条完整回放及校验。
- `first-recovery/`：第一次68补跑收据/输出/完整性审查，保留12条仍不完整的事实。
- `regressions/`：本轮各命令stdout、stderr和receipt。
- `chase-probes/`：七份场景、完整输出、报告与断点；手写纯MOVE不是生产策略的替身，当前策略在简单同轴墙角能攻击，仍需用户真实失败现场。

## 解包与校验

归档分为每块最多2MiB的原始Git文件，完整大小及SHA见raw-parts.json、recovery-parts.json、first-recovery-parts.json。克隆log分支并进入本目录：

```bash
python3 verify_archives.py
mkdir -p extracted
tar -xJf raw-offline-artifacts.tar.xz -C extracted
tar -xJf verified-recovery-and-regressions.tar.xz -C extracted
tar -xJf first-recovery-raw.tar.xz -C extracted
```

`verify_archives.py`先按清单顺序核对每块SHA再拼接、核对整包SHA；解包后`raw-file-manifest.json`可核对原始文件。原归档中的68个坏gzip会继续报EOF，完整补跑对应同case/label的verified-recovery条目，不覆盖原文件。

重现时先从相同完整Git SHA冻结worker，再将plan.versions路径指向本机冻结目录，另选输出目录。原绝对路径仅记录本轮环境，不能把改过路径的plan冒称原签名缓存。

## 2026-10-29 上传完整性补正

最终远端校验发现：提交 c1c64dd0ad176a6696a6a48e19b0ce647548b28b 中原始日志包与最终补跑包的34个Git分块在上传时被截断，不能按当时清单拼接成功。本次已从本地完整原包重新上传这34块，并逐块核对实际Git blob SHA与本地完整字节计算值一致；首次补跑包7块原本完整，已核对保留。清单和运行结果未改，旧提交保留历史。

请使用本分支最新提交中的分块执行上面的校验与解包命令。完整性记录见 [upload-integrity-2026-10-29.json](upload-integrity-2026-10-29.json)。本补正只修复上传产物，不增加比赛样本，也不把旧的68条坏gzip冒充完整原回放。
