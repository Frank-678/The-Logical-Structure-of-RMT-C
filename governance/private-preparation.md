# 私密预备资料与未来公开边界

ANALYSIS 与 COMPARISON 是用户指定的临时保密预备区，禁止在其他分支、PR、Issue、标签、公开工作流、发布说明或网站暴露其名称、入口或存在历史。不要将研究分支合并进正式开发历史。

仓库当前private，但Git分支没有独立访问隔离；删除分支引用不保证清除旧提交、缓存、其他refs或克隆。未来公开优先使用审查过的文件导出与干净新历史/独立发布仓库，不携带本分支的Git对象、文档、链接或submodule研究入口。

本次不公开仓库、不创建PR、不删除这些分支、不重写main。若未来仍要公开原仓库，需单独审查refs、提交和GitHub缓存，不能只删分支。

参考：[GitHub官方说明](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository)。
