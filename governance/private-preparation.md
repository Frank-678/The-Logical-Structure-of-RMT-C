# 私密预备资料与未来公开边界

用户明确要求 ANALYSIS 与 COMPARISON 为临时、保密的预备分支。不得向其他分支、PR、Issue、标签、公开工作流、发布说明或网站添加这些分支的名称、入口或曾存在的线索；不得把本研究历史合并到正式开发分支。仅在这两支内部提供研究导航。

当前仓库为 private；分支本身没有独立访问权限，已有仓库访问者仍能看到它们。删除分支引用不保证清除提交、缓存或他人的克隆。

未来公开前应导出经过审查的正式文件到全新干净历史/独立发布仓库，不携带本研究的 .git、分支、标签、合并父提交、研究文档或内部链接。不要仅删除两个分支就把同一对象库视为已经清洁。若必须公开原仓库，需要另行审查全部refs、历史、PR与缓存，并按GitHub流程处理；本次不执行公开、删除分支或重写main。

参考：[GitHub官方历史清理说明](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository)。当前归档不是对未来不可追溯性的保证。
