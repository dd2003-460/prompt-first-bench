#!/usr/bin/env python3
# origin: ai
# T8b 错误归因分析（D 2026-11-25 口径变更新增）
# 对 correctness 探针判"错/无法提取"的输出，检查全文是否覆盖赢家配置 3090×4/W4/n=2 的关键要素。
# 分类：a) 缺关键要素 → coverage 问题；b) 关键要素齐全但结论错 → 推理/算术问题。
# 背景：gold 赢家是时点特定的（gold-tree.md L6 注明混合负载可能改变排名），
#       稳定的是树结构（准入规则+计算路径），不是标签。
#       故本归因量的是"推理链完整性"（覆盖更多要素是否自然导出正确答案），非 winner 稳定性 claim。
import re

# 赢家配置 3090×4/W4/n=2 的关键要素（机械可检测）。
# 每项 (name, [patterns])：列表内所有 pattern 都命中才算覆盖该要素（AND 语义）。
# 校准注记（2026-11-25）：「3090 显存/带宽」类要素必须与 3090 联立，
#   否则 A100 方案的 24GB/936GB 数字会误判为「覆盖了 3090 要素」。
KEY_ELEMENTS = [
    ("3090卡型", [r"3090"]),
    ("3090×4数量", [r"(4\s*[×x*]\s*(?:RTX\s*)?3090|4\s?张\s*(?:RTX\s*)?3090|四\s?张\s*3090|3090\s*[×x*]\s*4)"]),
    ("3090显存24GB", [r"3090", r"(24\s?GB|24576|24\s?G\b)"]),
    ("3090带宽936GB/s", [r"3090", r"936\s?GB"]),
    ("W4/INT4精度", [r"(W4|INT4|4\s?bit|4-bit|nvfp4)"]),
    ("W4权重VRAM~13-14GB", [r"(?:W4|INT4|4\s?bit|4-bit).{0,250}(?:1[34]\.?[0-9]?\s?GB)|(?:1[34]\.?[0-9]?\s?GB).{0,250}(?:W4|INT4|4\s?bit)"]),
    ("W4质量损失论证", [r"(?:W4|INT4|4\s?bit|4-bit|量化).{0,150}(?:质量损失|可接受|困惑度|perplexity|下降|损失|精度损失)"]),
    ("多卡/4卡判断", [r"(?:多卡|4\s?卡|四\s?卡|tensor\s?parallel|TP\s*=?\s*4|2\s*[×x*]\s*2)"]),
    ("并发n判断", [r"(?:n\s*=\s*[0-9]|并发\s*[0-9]|batch\s*[0-9]|streams?\s*=?\s*[0-9]|KV.{0,40}(?:并发|stream))"]),
]

# 判定"覆盖赢家关键要素"的最小集合：缺任一即归为 coverage 问题(a)
CRITICAL = ["3090卡型", "W4/INT4精度", "多卡/4卡判断"]


def analyze_attribution(text, verdict):
    """对 correctness 判 错/无法提取 的输出做归因。
    返回 dict: covered/missing/crit_missing/category('a'|'b'|None)。
    category=None 表示 verdict==对（无需归因）。
    要素覆盖 = 该要素的 [patterns] 全部命中（AND 语义）。
    """
    if verdict == "对":
        return {"covered": [], "missing": [], "crit_missing": [], "category": None}
    covered, missing = [], []
    for name, pats in KEY_ELEMENTS:
        if all(re.search(p, text, re.I | re.S) for p in pats):
            covered.append(name)
        else:
            missing.append(name)
    crit_missing = [m for m in missing if m in CRITICAL]
    category = "a" if crit_missing else "b"
    return {"covered": covered, "missing": missing,
            "crit_missing": crit_missing, "category": category}
