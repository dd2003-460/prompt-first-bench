#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
calc.py — 每个通过任务的成本 c_pass [¢/task] 计算器（重建版）

# origin: ai (2026-11-22 重建; 原文件丢失, git 历史无记录)
# 重建依据: projects/decomp/bench/gold/ 的 L3.md / L4.md / L5-blackbox.md
# 验收锚:
#   ① c_pass(3090x4/W4/n=2) = 0.679 ¢/task   (L5§4, tp_eff=0.81 标定)
#   ② 六弹性 (L4§4 实测表): u=1.000 η_bw=0.599 MFU=0.401 H=0.507 电价=0.493 G=1.029
#   ③ prefill:decode 时间比 = 40:60 (L4§4 F-A 订正, 独立于 tp_eff 绝对值)
#   ④ 排名 3090x4/W4/n=2 < 3090x2/W4/n=1 (L5§4, 不依赖 tp_eff 绝对值)

公式 (gold-tree.md N-0):
    c_pass = c_hour / ( u × λ_raw × G_pass )
    c_hour = 摊销 + 电费 + 故障
    λ_raw  = 3600 / t_task ;  t_task = t_prefill + t_decode/n
    t_prefill = prefill_FLOPs / (卡数 × 峰值TFLOPS × MFU × tp_eff)
    t_decode  = 输出tok × (W + n×KV) / (卡数 × 峰值BW × η_bw × tp_eff)

诚实边界:
    tp_eff 文档标 S-a 但未钉数值; 本文件用 0.81 标定使点值对上 0.679。
    弹性表 + 40:60 比例 + 排名 均不依赖 tp_eff 绝对值 (tp_eff 同乘 prefill/decode)。
    所以 "3090x4 是 winner" 的排名结论对 tp_eff 稳健, 点值 0.679 依赖标定。
"""

# ---- 参数表 (来源: L3/L4/L5, 逐条标注) ----
# 3090 单卡规格: tf_peak=71 TFLOPS (L4: 4x71), bw=936 GB/s (L4: 4x936), 显存 24GB, TDP 350W
# 27B 权重: W4=14.0 / W8=27.0 / W16=54.0 GB (L4: 27e9×bits/8)
# KV@64K: 24.7 GB/流 (L4: B7 "我"口径 46层/16KV头; 另一口径 12.3GB 见 B7)

HARDWARE = {
    "3090":  dict(tf_peak=71e12,  bw=936.0,  mem=24.0,  tdp=350.0, price_each=1050.0),
    # V100 规格: knowledgebase/hardware/datacenter-cards.json (125 TFLOPS FP16 tensor dense,
    # 900 GB/s HBM2, 32GB, 250W, NVLink 300GB/s)。二手价 2500$/张 [待核验, 2026 市场价]
    "V100":  dict(tf_peak=125e12, bw=900.0,  mem=32.0,  tdp=250.0, price_each=2500.0),
}
# 非黑盒参数 (L4§2 叶子表, S-a 可直接算/查):
HOST_PRICE = 2000.0     # 主机价 4卡平台 (L4: 2000$)
RESID      = 0.40       # 残值率 (L4: B8)
H_HOURS    = 26280.0    # 摊销小时数 3年 (L4: 26280h)
P_FAIL     = 0.20       # 三年故障概率 (L4: B8)
PREFILL_FLOPS = 594e12  # 594 TFLOP (L4: 2×27e9×5898)
OUT_TOK    = 655        # 输出 token (L3: decode 655)
TP_EFF     = 0.81       # 多卡互联效率 [标定值, 文档标 S-a 未钉数值]

# 黑盒取中位数 (L5§2, 结论参数):
U, G, ELEC, MFU, ETA_BW = 0.35, 0.68, 0.12, 0.45, 0.80
W_BYTES = {"W4": 14.0, "W8": 27.0, "W16": 54.0}
KV_PER_STREAM = 24.7    # GB/流 @64K (B7 "我"口径)


def c_pass(card, n_cards, quant, n, tp_eff=TP_EFF):
    """返回 (c_pass[¢/task], t_prefill[s], t_decode_per_stream[s])。"""
    hw = HARDWARE[card]
    gpu_price = hw["price_each"] * n_cards
    # c_hour = 摊销 + 电费 + 故障
    amort = (gpu_price + HOST_PRICE - gpu_price * RESID) / H_HOURS
    elec  = (n_cards * hw["tdp"] + 300) / 1000.0 * ELEC   # kW × $/kWh
    fail  = P_FAIL * gpu_price / H_HOURS
    c_hour = amort + elec + fail
    # t_task = t_prefill + t_decode/n
    t_prefill = PREFILL_FLOPS / (n_cards * hw["tf_peak"] * MFU * tp_eff)
    t_decode  = OUT_TOK * (W_BYTES[quant] + n * KV_PER_STREAM) / (n_cards * hw["bw"] * ETA_BW * tp_eff)
    t_task = t_prefill + t_decode / n
    lam = 3600.0 / t_task
    return c_hour / (U * lam * G) * 100.0, t_prefill, t_decode / n


def mem_per_card(card, quant, n, n_cards):
    """每卡显存需求 (TP 下权重+KV 按卡数分摊)。用于可行性检查。
    口径: L5 B7 —— 24.7GB 是每流总 KV, TP 下每卡承担 KV/n_cards。
    文档 '3090×4-W4 只能开 n=2' 即由此口径得出。"""
    hw = HARDWARE[card]
    return (W_BYTES[quant] + n * KV_PER_STREAM) / n_cards


def elasticity(card, n_cards, quant, n, key, base_val, tp_eff=TP_EFF):
    """数值微分: 对参数 key 的弹性 dln(c_pass)/dln(key)。"""
    h = base_val * 1e-6
    def cp(val):
        # 临时改全局参数
        old = globals()[key]
        globals()[key] = val
        r = c_pass(card, n_cards, quant, n, tp_eff)[0]
        globals()[key] = old
        return r
    return (cp(base_val + h) - cp(base_val - h)) / (2 * h) / cp(base_val) * base_val


def main():
    print("=" * 64)
    print("calc.py 重建验证 (3090x4 / W4 / n=2)")
    print("=" * 64)

    # ① 点值
    cp, tp, td = c_pass("3090", 4, "W4", 2)
    ratio = tp / (tp + td) * 100
    print(f"\n[① 点值] c_pass = {cp:.4f} ¢/task   (文档目标 0.679, 差 {abs(cp-0.679)/0.679*100:.2f}%)")
    print(f"          t_prefill={tp:.3f}s  t_decode/n={td:.3f}s")

    # ③ prefill:decode 比例 (独立于 tp_eff)
    print(f"\n[③ 时间比] prefill:decode = {ratio:.1f}:{100-ratio:.1f}   (文档锚 40:60, F-A)")

    # ② 六弹性
    print(f"\n[② 弹性] 参数      实测      文档(L4)   判定")
    doc = {"U": 1.000, "ETA_BW": 0.599, "MFU": 0.401, "H_HOURS": 0.507, "ELEC": 0.493, "G": 1.029}
    all_ok = True
    for key, d in doc.items():
        e = elasticity("3090", 4, "W4", 2, key, globals()[key])
        ok = abs(abs(e) - d) / d < 0.03
        all_ok = all_ok and ok
        print(f"          {key:<10} {e:>8.4f}  {d:>8.3f}   {'✅' if ok else '🟡'}")

    # ④ 排名 (不依赖 tp_eff 绝对值)
    print(f"\n[④ 排名] (u=0.35 G=0.68 电价0.12 MFU0.45 η_bw0.80)")
    configs = [("3090", 4, "W4", 2, "3090×4/W4/n=2"),
               ("3090", 2, "W4", 1, "3090×2/W4/n=1")]
    rows = []
    for card, nc, q, n, label in configs:
        c, _, _ = c_pass(card, nc, q, n)
        rows.append((c, label))
    rows.sort()
    for i, (c, label) in enumerate(rows, 1):
        print(f"          {i}. {label:<16} {c:.3f} ¢/task")
    winner = "3090×4/W4/n=2" if rows[0][1] == "3090×4/W4/n=2" else rows[0][1]
    print(f"          → winner = {winner}   (文档: 3090×4/W4/n=2)")

    print(f"\n{'=' * 64}")
    print(f"验收: 点值 {'✅' if abs(cp-0.679)/0.679<0.01 else '🟡'}  "
          f"弹性 {'✅' if all_ok else '🟡'}  "
          f"比例 {'✅' if abs(ratio-40.1)<1 else '🟡'}  "
          f"排名 {'✅' if winner=='3090×4/W4/n=2' else '🟡'}")
    print(f"结论: 3090×4/W4/n=2 winner 验证 "
          f"{'成立(排名对tp_eff稳健)' if winner=='3090×4/W4/n=2' else '失败'}")
    print(f"{'=' * 64}")


if __name__ == "__main__":
    main()
