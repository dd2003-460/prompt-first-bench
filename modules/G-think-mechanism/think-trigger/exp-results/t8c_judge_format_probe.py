#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""t8c_judge_format_probe.py — J1 三型判别器对 T8c 题面输出格式的探针。

# origin: ai (2026-11-25, T8c 前置产出)
# 目的: correctness_layer_v0.py 的 selftest 只覆盖 T8b 格式输出。T8c 题面
#       (t8c-spec-final.md §4) 要求的输出格式不同（配置枚举表 + c_pass 排序 +
#       强推荐行）。若判别器在 T8c 格式下误判（正确输出→A3 假阳性, 或
#       错误输出→indeterminate 漏判）, smoke 的三型标签就不可信, 白跑。
# 方法: 4 个合成样本, 格式严格模仿 §4 题面输出要求（表格式枚举 + c_pass 数值 +
#       强推荐关键词行）, 期望标签: CORRECT→indeterminate, ERR_A1→A1,
#       ERR_A2→A2, ERR_A3→A3。全对 = judge 对 T8c 格式就绪。
"""
import os, sys

# 2026-11-26 路径修复: 原硬编码 pfb worktree 路径在 pfb-thinkmech worktree 不存在(ModuleNotFoundError), 改脚本相对(跨 worktree 可移植)
sys.path.insert(0, os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "modules", "B-pipeline-ablation", "research")))
from correctness_layer_v0 import judge_text

# 共同骨架: 按 §4 输出要求 1-5 的格式（枚举表 + 淘汰说明 + 精度论证 + 来源标注）
HEADER = (
    "【可行配置枚举】（两道门通过者, 按 c_pass 升序）\n"
    "| 配置 | c_pass (¢/task) | 显存/卡 | 带宽需求 |\n"
    "|---|---|---|---|\n"
)
TAIL = (
    "\n【精度论证】选 W4: 27B W4 量化困惑度上升约 0.3-0.5 [待核验, 凭记忆], "
    "对本地推理场景可接受。\n"
    "【来源标注】936 GB/s / 24.7 GB/流 / 774 GB/s 门限 = 题面给定; c_pass 数值 = 按题面公式推导。\n"
)

# 1) CORRECT: 4×V100/W4/n=2 被枚举、被评估、被强推荐
CORRECT = HEADER + (
    "| V100×4/W4/n=2 | 0.4511 | 15.8 GB | 317 GB/s |\n"
    "| V100×4/W8/n=2 | 0.5188 | 19.1 GB | 382 GB/s |\n"
    "| 3090×4/W4/n=2 | 0.6807 | 15.8 GB | 317 GB/s |\n"
    "\n【淘汰】3090×2/W8/n=1: 显存 25.9>24 GB 装不下; V100×2/W16/n=1: 显存 39.4>32 GB。\n"
    "\n【最终推荐】主推荐: 4×V100 SXM2 / W4 / n=2（c_pass=0.4511 ¢/task, 全表最低）。\n"
) + TAIL

# 2) ERR_A1: V100 从未进候选集（模型只看了 3090）
ERR_A1 = HEADER + (
    "| 3090×4/W4/n=2 | 0.6807 | 15.8 GB | 317 GB/s |\n"
    "| 3090×4/W8/n=2 | 0.764 | 19.1 GB | 382 GB/s |\n"
    "\n【淘汰】3090×2/W8/n=1: 显存 25.9>24 GB 装不下。\n"
    "\n【最终推荐】主推荐: 4×RTX 3090 / W4 / n=2（c_pass=0.6807 ¢/task, 全表最低）。\n"
) + TAIL

# 3) ERR_A2: V100 多次出现(≥4, 避开 C1e=0.5 的设计边界保守归 A1)
#    但 4×V100 从未被构造/评估（只算了 V100×2）
ERR_A2 = HEADER + (
    "| V100×2/W4/n=1 | 0.7088 | 19.35 GB | 387 GB/s |\n"
    "| 3090×4/W4/n=2 | 0.6807 | 15.8 GB | 317 GB/s |\n"
    "\n【淘汰】V100×2/W16/n=1: 显存 39.4>32 GB 装不下; V100 单卡 32 GB 装不下 "
    "27B W4+KV@64K, V100 多卡组合未展开计算。\n"
    "\n【最终推荐】主推荐: 4×RTX 3090 / W4 / n=2（c_pass=0.6807 ¢/task, 全表最低）。\n"
) + TAIL

# 4) ERR_A3: 4×V100 被完整评估（有数值）但排序垫底, 推荐 3090
ERR_A3 = HEADER + (
    "| 3090×4/W4/n=2 | 0.6807 | 15.8 GB | 317 GB/s |\n"
    "| V100×4/W4/n=2 | 0.4511* | 15.8 GB | 317 GB/s |\n"
    "*注: V100×4 的 c_pass 按题面公式算为 0.4511, 但考虑二手市场供应稳定性与散热, "
    "综合评分后列为次选。\n"
    "\n【淘汰】V100×2/W16/n=1: 显存 39.4>32 GB 装不下。\n"
    "\n【最终推荐】主推荐: 4×RTX 3090 / W4 / n=2（综合评分最高）。\n"
    "备选: 4×V100 SXM2/W4/n=2（c_pass 更低但供应稳定性差, 列次选）。\n"
) + TAIL

# 5) CORRECT_TBL: 表格行格式(卡型/卡数分列)的正确答案——winner 评估行+推荐行均为表格
CORRECT_TBL = (
    "### 1. 可行配置枚举（两道门通过者, 按 c_pass 升序）\n"
    "| 卡型 | 卡数 | 精度 | n | c_pass (¢/task) |\n"
    "|---|---|---|---|---|\n"
    "| V100 SXM2 | 4 | W4 | 2 | 0.4511 |\n"
    "| V100 SXM2 | 4 | W8 | 2 | 0.5188 |\n"
    "| RTX 3090 | 4 | W4 | 2 | 0.6807 |\n"
    "\n### 2. 最优选卡方案\n"
    "| **V100 SXM2** | 4 | W4 | 2 | **0.4511** | —（**最优选**） |\n"
    "\n### 3. 淘汰原因\n"
    "| RTX 3090 | 2 | W8 | 1 | 显存 25.85>24 装不下 |\n"
    "| V100 SXM2 | 2 | W16 | 1 | 显存 39.35>32 装不下 |\n"
    "\n【精度论证】W4 质量损失可接受 [待核验]。\n"
    "【来源标注】900 GB/s / 24.7 GB/流 = 题面给定; c_pass = 按题面公式推导。\n"
)

# 6) ERR_A3_TBL: 表格行格式的 A3——winner(V100×4) 被完整评估(0.437, 单卡价误读口径)但推荐 3090
#    (模拟 smoke 第一批 A 臂 run2 的真实形态, 含 gpu_price 单卡价误读口径)
ERR_A3_TBL = (
    "### 1. 可行配置枚举（两道门通过者, 按 c_pass 升序）\n"
    "| 卡型 | 卡数 | 精度 | n | c_pass (¢/task) | 备注 |\n"
    "|---|---|---|---|---|---|\n"
    "| **RTX 3090** | 4 | W4 | 2 | **0.437** | —（**最优选**） |\n"
    "| V100 SXM2 | 4 | W4 | 2 | 0.521 | c_pass 更高 |\n"
    "| V100 SXM2 | 4 | W8 | 2 | 0.584 | c_pass 更高 |\n"
    "\n### 2. 最优选卡方案\n"
    "**RTX 3090 × 4 卡 × W4 × n=2**, c_pass = 0.4374 ¢/task（全局最低）。\n"
    "\n### 3. 淘汰原因\n"
    "- **V100 SXM2 W16 2卡**：显存不足（39.35 GB/卡 > 32 GB）。\n"
    "- **V100 SXM2 所有配置**：二手市场供应稳定性差, 散热劣于 3090, 列次选。\n"
    "\n【精度论证】W4 质量损失可接受 [待核验]。\n"
    "【来源标注】900 GB/s / 24.7 GB/流 = 题面给定; c_pass = 按题面公式推导。\n"
)

CASES = [("CORRECT", CORRECT, "indeterminate"),
         ("ERR_A1", ERR_A1, "A1"),
         ("ERR_A2", ERR_A2, "A2"),
         ("ERR_A3", ERR_A3, "A3"),
         ("CORRECT_TBL", CORRECT_TBL, "indeterminate"),
         ("ERR_A3_TBL", ERR_A3_TBL, "A3")]

fails = 0
for name, text, want in CASES:
    j = judge_text(text)
    ok = j["verdict"] == want
    fails += (not ok)
    print(f"{name:<13} 期望={want:<14} 实际={j['verdict']:<14} "
          f"C={j['C']} E={j['E']} R_low={j['R_low']} P_A1={j['P_A1']} P_A3={j['P_A3']} "
          f"C2BP={j['C2BP']} {'✅' if ok else '❌'}")
print()
if fails:
    print(f"FAIL — {fails}/{len(CASES)} 误判: J1 判别器对 T8c 格式未就绪, 修判别器或改题面输出格式后再跑")
    raise SystemExit(1)
print(f"PASS — J1 判别器对 T8c 题面输出格式 {len(CASES)}/{len(CASES)} 正确(含表格行格式), smoke 三型标签可信")
