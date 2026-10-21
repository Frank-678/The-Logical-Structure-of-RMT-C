# 数据与引用校验

初始化submodule后，在本分支运行：

    python3 tools/verify_upstream.py
    python3 tools/recompute_statistics.py
    python3 tools/scan_upstream.py --out /tmp/meow-rescan
    python3 tools/check_links.py

verify_upstream.py 验证固定提交、1078个文件哈希和3个原始摘录。recompute_statistics.py 只处理存档及纯评分函数，不运行bot或真实模型。data-checks.json保存本次更完整的原始统计核查；recomputed-statistics.json保存可复现脚本输出。upstream-verification.json与link-check.json保存本次核查输出。

所有检查通过只表示列出的不变量成立，不等于所有源代码正确、不等于已重新评测全部98780局，也未重新计算所有bootstrap区间。
