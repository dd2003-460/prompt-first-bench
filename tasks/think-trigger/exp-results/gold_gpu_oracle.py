#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gold_gpu_oracle.py — 独立 gold 预言机（T8c token-matched 对照的 oracle 种子）

# origin: ai (2026-11-25, T8b 副产物)
# 作用: 给定候选硬件, 机械复算 gold 树的三道约束 (N-5.1 显存门 / N-5.2 带宽门 / c_pass 成本),
#       输出可行配置按 c_pass 排序, 复现 gold winner = 3090×4/W4/n=2。
#
# 为什么需要它: T8b 发现 0/6 correctness 是『题面 32K 画像 vs gold 64K 画像』分叉, 不是 gold 不一致。
#   T8c 要做 token-matched 对照, 必须有一个独立于被测模型的 gold 参照——本预言机就是这个参照:
#   它把 gold 的 64K 画像 + 20 tok/s 解码目标 + 成本模型固化成可复算代码, 不依赖任何 LLM。
#
# 来源分级 (全部 ①类, 无凭记忆填数):
#   - c_pass / mem_per_card / 硬件规格 / 黑盒参数: 直接 import calc.py (已验证 4/4 验收锚)
#   - N-5.2 带宽门公式: 本轮从 gold 三档下限精确恢复 + 6/6 gold 判断校验 (见 t8b-smoke-report.md §3.2)
#   - 并发约定 n = n_cards//2 (2 卡/流): 部署驱动 (gold SHARED 注 n=min(n_speed,n_cap)), 非自由优化变量;
#     本约定精确复现 gold winner 3090×4/W4/n=2 (0.681)。
#   - 候选集: 默认 sweep 用 calc.py HARDWARE 里已有 ①类规格的卡 (3090 / V100)——
#     这是 gold 树候选集 (gold-tree.md L94: 3090/M2Ultra/L40S/A100 + V100/TPU/Groq/Cerebras/SambaNova)
#     中规格齐全的 2 卡子集, 保证复现 gold winner。
#     另 4 类 (L40S/A100/H100/M2Ultra) 在 KB 缺 flops/price (null=[待核验]), 不凭记忆填 (③类风险)。
#     4090 例外: KB 有完整 ①类规格 (rtx-4090.json, conf 0.85), 但 4090 不在 gold 候选集内——
#     见下方 4090 敏感性分析: 一旦把 4090 加入候选集, gold winner 翻转为 4090×4/W4/n=2。
#
# 验收锚 (跑本脚本应全过):
#   ① winner = 3090×4/W4/n=2
#   ② c_pass(winner) ≈ 0.679 ¢/task (calc.py 标定值, 容差 1%)
#   ③ N-5.2 门对 6 个 gold 判断 6/6 吻合 (M2Ultra/L40S/A100/3090×2-W8/3090×2-W16 fail, 3090×4-W4 pass)
"""
import os, sys

# 复用 calc.py 的已验证函数与参数 (①类来源)
CALC_DIR = "/Users/a1-6/Desktop/workspace/pfb/bench/rubric-v3/tasks/T0-local-27b/reference"
sys.path.insert(0, CALC_DIR)
import calc  # noqa: E402

# ---- N-5.2 带宽门 (本轮恢复的一般式) ----
# 每卡需求 = r × (W_bytes + n_streams×KV) / n_cards   vs   每卡有效带宽 = bw_peak × η_bw
# r = 20 tok/s (目标每流解码速率), KV = 24.7 GB/流 @64K (calc.KV_PER_STREAM), η_bw = 0.80 (calc.ETA_BW)
R_TOK_S = 20.0
KV = calc.KV_PER_STREAM      # 24.7 @64K
ETA_BW = calc.ETA_BW         # 0.80
W_BYTES = calc.W_BYTES       # {W4:14, W8:27, W16:54}


def n52_bandwidth_ok(card, n_cards, quant, n_streams):
    """N-5.2 带宽准入门: 每卡有效带宽 >= 每卡需求? 返回 (ok, per_card_need, eff_bw)."""
    hw = calc.HARDWARE[card]
    per_card_need = R_TOK_S * (W_BYTES[quant] + n_streams * KV) / n_cards
    eff_bw = hw["bw"] * ETA_BW
    return eff_bw >= per_card_need, per_card_need, eff_bw


def n51_vram_ok(card, n_cards, quant, n_streams):
    """N-5.1 显存门: 每卡显存需求 <= 单卡显存? 返回 (ok, per_card_mem, total_mem)."""
    hw = calc.HARDWARE[card]
    per_card_mem = calc.mem_per_card(card, quant, n_streams, n_cards)
    return per_card_mem <= hw["mem"], per_card_mem, hw["mem"]


def conv_streams(n_cards):
    """gold 的并发约定: n = n_cards // 2 (2 卡/流), 非自由优化变量.
    依据: gold-tree.md SHARED 注 'n = min(n_speed, n_cap)' (部署驱动, 非成本优化);
    calc.py 自身对比用 3090×4→n=2 / 3090×2→n=1, 即 2 卡/流。
    本约定精确复现 gold winner 3090×4/W4/n=2 (0.681)。"""
    return max(1, n_cards // 2)


def sweep(cards=("3090", "V100"), max_cards=4, quants=("W4", "W8", "W16")):
    """枚举可行配置 (n 按 2 卡/流约定), 应用两道门, 按 c_pass 排序. 返回 (ranked_rows, eliminated)."""
    ranked, eliminated = [], []
    for card in cards:
        if card not in calc.HARDWARE:
            continue
        for nc in range(2, max_cards + 1):  # ≥2 卡才有 1 流 (2 卡/流)
            for q in quants:
                ns = conv_streams(nc)  # 部署约定, 非自由变量
                ok_v, pm, tm = n51_vram_ok(card, nc, q, ns)
                ok_b, need, eff = n52_bandwidth_ok(card, nc, q, ns)
                cfg = f"{card}×{nc}/{q}/n={ns}"
                if not ok_v:
                    eliminated.append((cfg, f"N-5.1 显存 {pm:.1f}>{tm}"))
                    continue
                if not ok_b:
                    eliminated.append((cfg, f"N-5.2 带宽 {eff:.0f}<{need:.0f}"))
                    continue
                c, _, _ = calc.c_pass(card, nc, q, ns)
                ranked.append((c, cfg, pm, need, eff))
    ranked.sort(key=lambda x: x[0])
    return ranked, eliminated


def check_4090_flip():
    """4090 候选集敏感性: 把 4090 加入候选集后 gold winner 是否翻转.
    ①类来源: 4090 规格取 KB rtx-4090.json (conf 0.85, NVIDIA 官网 2026-11-20 抓取),
    口径与 calc.py 3090 一致 (FP16 non-tensor = 2×FP32: 3090→71, 4090→165.2)。
    4090 不在 gold 候选集 (gold-tree.md L94), 但 T8b 题面『候选硬件: 自行搜索』→
    模型自然纳入 4090。本函数量化: 一旦纳入, 成本最优从 3090×4/W4/n=2 翻转为 4090×4/W4/n=2。
    返回 (flip: bool, c_4090, c_3090, breakeven_price).
    """
    # 4090: 165.2 TFLOPS (FP16 non-tensor), 1008 GB/s, 24GB, 450W, $1599 MSRP (KB rtx-4090.json)
    spec = dict(tf_peak=165.2e12, bw=1008.0, mem=24.0, tdp=450.0)
    calc.HARDWARE["4090"] = dict(spec, price_each=1599.0)
    c4090, _, _ = calc.c_pass("4090", 4, "W4", 2)
    c3090, _, _ = calc.c_pass("3090", 4, "W4", 2)
    flip = c4090 < c3090
    # 盈亏平衡价: 4090 c_pass = 3090 c_pass 时的单价 (二分)
    lo, hi = 500.0, 5000.0
    for _ in range(60):
        mid = (lo + hi) / 2
        calc.HARDWARE["4090"] = dict(spec, price_each=mid)
        c, _, _ = calc.c_pass("4090", 4, "W4", 2)
        if c < c3090:
            lo = mid
        else:
            hi = mid
    breakeven = (lo + hi) / 2
    return flip, c4090, c3090, breakeven


def check_gold_judgments():
    """N-5.2 门对 gold-tree.md 6 个判断的复算 (①类校验)."""
    # gold-tree.md N-5.2: 划掉 M2Ultra(560)·L40S×1·A100×1-W16·3090×2-W8/W16; 赢家 3090×4/W4
    # 注: M2Ultra/L40S/A100 不在 calc.HARDWARE, 用其 ①类峰值带宽单独验门 (来源: formal-matrix doc-A2/D3)
    ext_bw = {"M2Ultra": 560.0, "L40S": 864.0, "A100": 1935.0}  # ①类 (blind-eval doc-A2/D3 规格书)
    gold = [("M2Ultra", 1, "W4", "fail"), ("L40S", 1, "W4", "fail"),
            ("A100", 1, "W16", "fail"), ("3090", 2, "W8", "fail"),
            ("3090", 2, "W16", "fail"), ("3090", 4, "W4", "pass")]
    rows, all_ok = [], True
    for card, nc, q, g in gold:
        need = R_TOK_S * (W_BYTES[q] + nc * KV) / nc   # 一卡一流 n_streams=n_cards
        peak = ext_bw[card] if card in ext_bw else calc.HARDWARE[card]["bw"]
        eff = peak * ETA_BW
        v = "pass" if eff >= need else "fail"
        ok = (v == g)
        all_ok = all_ok and ok
        rows.append(f"    {card}×{nc}/{q:<4} 需 {need:6.1f} vs 有效 {eff:6.1f} → {v:<4} (gold {g}) {'✓' if ok else '✗'}")
    return all_ok, rows


def main():
    print("=" * 68)
    print("gold_gpu_oracle.py — 独立 gold 预言机 (T8c oracle 种子)")
    print("=" * 68)

    # ③ N-5.2 门 6/6 校验
    ok6, rows = check_gold_judgments()
    print("\n[③ N-5.2 带宽门 6/6 gold 判断校验]")
    print("\n".join(rows))
    print(f"    → 6/6 吻合: {ok6}")

    # ①② 候选集 sweep + winner
    ranked, eliminated = sweep()
    print(f"\n[①② 可行配置按 c_pass 排序] (候选集={list(calc.HARDWARE.keys())}, ≤4 卡)")
    for i, (c, cfg, pm, need, eff) in enumerate(ranked, 1):
        print(f"    {i}. {cfg:<20} c_pass={c:.3f} ¢/task  (显存 {pm:.1f}GB/卡, 带宽需 {need:.0f}≤{eff:.0f})")
    print(f"\n    [淘汰 {len(eliminated)} 个配置]")
    for cfg, why in eliminated:
        print(f"      ✗ {cfg:<20} {why}")

    winner_cfg = ranked[0][1]
    winner_c = ranked[0][0]
    expect = "3090×4/W4/n=2"
    win_ok = winner_cfg == expect
    c_ok = abs(winner_c - 0.679) / 0.679 < 0.01
    print(f"\n{'=' * 68}")
    print(f"验收: winner={winner_cfg} {'✅' if win_ok else '❌ 期望 '+expect}   "
          f"c_pass={winner_c:.3f}≈0.679 {'✅' if c_ok else '❌'}   "
          f"N-5.2 6/6 {'✅' if ok6 else '❌'}")
    print(f"结论: gold winner 复现 {'成立' if win_ok and c_ok else '失败'}"
          f" (oracle 可用于 T8c token-matched 对照的独立参照)")

    # 4090 候选集敏感性 (①类: KB rtx-4090.json conf 0.85)
    flip, c4090, c3090, breakeven = check_4090_flip()
    print(f"\n[4090 候选集敏感性] (4090 不在 gold 候选集, 但 T8b 题面『自行搜索』会纳入)")
    print(f"    4090×4/W4/n=2 = {c4090:.3f}  vs  3090×4/W4/n=2 = {c3090:.3f}  "
          f"→ winner {'翻转为 4090' if flip else '不变'}  (盈亏平衡价 ≈ ${breakeven:.0f})")
    print(f"    → gold winner 3090×4/W4/n=2 是『候选集不含 4090』的条件性结论;")
    print(f"      4090 一旦入候选集, 成本最优变 4090×4/W4/n=2 (construct mismatch 第三维: 候选集依赖)")
    print(f"{'=' * 68}")
    return 0 if (win_ok and c_ok and ok6) else 1


if __name__ == "__main__":
    sys.exit(main())
