#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""t8c_spec_selfcheck.py — 题面 §4 可执行性自洽验证（不 import calc.py）。

# origin: ai (2026-11-25, T8c 前置产出)
# 目的: 验证 t8c-spec-final.md §4 题面正文（冻结版 2c16f644f）里的公式+参数
#       若被模型照抄执行, 能否复现 oracle winner = 3090×4/W4/n=2 (c_pass≈0.681)。
#       oracle 验证的是 calc.py 参数; 本脚本验证的是『题面文字本身』——
#       参数从题面 §4 手工转录（独立来源, 防题面笔误导致 T8c 白跑）。
# 用法: python3 t8c_spec_selfcheck.py  → exit 0 且打印 PASS 即题面自洽。
"""

# ---- 参数: 从 t8c-spec-final.md §4 题面正文逐字转录（非 calc.py） ----
HW = {
    "3090": dict(mem=24.0, bw=936.0, tf=71e12,  tdp=350.0, price=1050.0),
    "V100": dict(mem=32.0, bw=900.0, tf=125e12, tdp=250.0, price=2500.0),
}
KV = 24.7          # GB/流 @64K（题面硬约束1）
R_TOK_S = 20.0     # 解码吞吐目标（题面硬约束2）
W_BYTES = {"W4": 14.0, "W8": 27.0, "W16": 54.0}   # 题面候选硬件段
U, G = 0.35, 0.68  # 利用率/通过率（题面参数含义段）
HOST_PRICE, RESID = 2000.0, 0.40
H_HOURS, P_FAIL = 26280.0, 0.20
PREFILL_FLOPS, OUT_TOK = 594e12, 655
MFU, TP_EFF, ETA_BW, ELEC = 0.45, 0.81, 0.80, 0.12


def conv_streams(n_cards):
    return max(1, n_cards // 2)   # 题面硬约束3: n = floor(n_cards/2)


def gates(card, nc, q, n):
    """题面两道准入门。返回 (ok, reason)。"""
    hw = HW[card]
    per_mem = (W_BYTES[q] + n * KV) / nc
    if per_mem > hw["mem"]:
        return False, f"N-5.1 显存 {per_mem:.1f}>{hw['mem']}"
    need = R_TOK_S * (W_BYTES[q] + n * KV) / nc
    eff = hw["bw"] * ETA_BW
    if eff < need:
        return False, f"N-5.2 带宽 {eff:.0f}<{need:.0f}"
    return True, ""


def c_pass(card, nc, q, n):
    """题面 c_pass 公式逐行实现。"""
    hw = HW[card]
    gp = hw["price"] * nc
    amort = (gp + HOST_PRICE - gp * RESID) / H_HOURS
    elec = (nc * hw["tdp"] + 300) / 1000.0 * ELEC
    fail = P_FAIL * gp / H_HOURS
    c_hour = amort + elec + fail
    t_prefill = PREFILL_FLOPS / (nc * hw["tf"] * MFU * TP_EFF)
    t_decode = OUT_TOK * (W_BYTES[q] + n * KV) / (nc * hw["bw"] * ETA_BW * TP_EFF)
    t_task = t_prefill + t_decode / n
    lam = 3600.0 / t_task
    return c_hour / (U * lam * G) * 100.0


def sweep(max_cards=4):
    ranked, elim = [], []
    for card in ("3090", "V100"):
        for nc in range(2, max_cards + 1):
            for q in ("W4", "W8", "W16"):
                n = conv_streams(nc)
                ok, why = gates(card, nc, q, n)
                cfg = f"{card}×{nc}/{q}/n={n}"
                if not ok:
                    elim.append((cfg, why))
                    continue
                ranked.append((c_pass(card, nc, q, n), cfg))
    ranked.sort(key=lambda x: x[0])
    return ranked, elim


def main():
    ranked, elim = sweep()
    print("== 题面 §4 自洽验证（参数独立转录, 非 calc.py）==")
    print("[可行 top-3]")
    for c, cfg in ranked[:3]:
        print(f"  {c:.4f} ¢/task  {cfg}")
    print(f"[淘汰 {len(elim)} 个]")
    for cfg, why in elim:
        print(f"  ✗ {cfg}  {why}")
    cw, w = ranked[0]
    ok_winner = (w == "3090×4/W4/n=2")
    ok_cp = abs(cw - 0.681) / 0.681 < 0.01
    ok_elim = len(elim) == 5   # oracle 实跑淘汰 5 个
    print(f"\n验收: winner={'✅' if ok_winner else '❌ '+w}  "
          f"c_pass={cw:.4f}≈0.681 {'✅' if ok_cp else '❌'}  淘汰数={len(elim)}/5 {'✅' if ok_elim else '❌'}")
    print("PASS — 题面 §4 自洽, 模型照抄可得 oracle winner" if (ok_winner and ok_cp and ok_elim)
          else "FAIL — 题面 §4 与 oracle 不一致, 修题面后再跑 T8c")
    raise SystemExit(0 if (ok_winner and ok_cp and ok_elim) else 1)


if __name__ == "__main__":
    main()
