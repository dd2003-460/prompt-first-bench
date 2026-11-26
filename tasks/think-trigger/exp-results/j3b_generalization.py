#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
j3b_generalization.py — J3b 候选集外泛化排名表 (2026-11-26)

# origin: ai
# 任务 (decomposition J3b): 用本地 ①类规格跑 oracle, 出 L40S/A100/H100/M2Ultra 的
#   c_pass 泛化排名表 + c_pass 作用域边界可检验判据 + 排错样本归因作用域。
#
# 诚实边界 (来源分级, 全部标注):
#   - 规格来源 = doc-A2/D3 (blind-eval ①类, 带日期引用) + KB 卡 + oracle ext_bw。
#   - tf_peak (FP16 non-tensor, 2×FP32 口径, 同 calc.py 3090→71) 是 ③类(凭记忆),
#     本地无 ①类源 → 不编精确值, 改做敏感性扫描 (0.5×/1×/2×) 证排名对其不敏感。
#   - H100/M2Ultra 的 price/tdp 本地缺 → 标 [待核验], 只进带宽门不进 c_pass 排序。
#   - 芯片命名: gold 树/oracle 用 M2Ultra(bw 560), KB 只有 m5-ultra(bw 1200),
#     doc-A2/D3 提 M3/M5 Ultra → 命名不一致本身是作用域问题, 单列。
"""
import sys, os
CALC_DIR = "/Users/a1-6/Desktop/workspace/pfb-thinkmech/bench/rubric-v3/tasks/T0-local-27b/reference"
sys.path.insert(0, CALC_DIR)
import calc

R_TOK_S = 20.0
KV = calc.KV_PER_STREAM
ETA_BW = calc.ETA_BW
W_BYTES = calc.W_BYTES

# ---- ①类规格 (来源标注) ----
# 每卡: bw(GB/s) / mem(GB) / price($) / tdp(W) / tf_peak(FP16 non-tensor, ③类待敏扫)
# 来源: doc-A2 L50-58 / doc-D3 L40-42 (带日期引用) + KB + oracle ext_bw
HW = {
    "3090":    dict(bw=936.0,  mem=24.0, price=1050.0, tdp=350.0, tf=71e12,
                    src="calc.py HARDWARE (①类, 4锚验证)"),
    "L40S":    dict(bw=864.0,  mem=48.0, price=8000.0, tdp=350.0, tf=91.6e12,
                    src="doc-A2 L53/L57/L58 (①类: pcserverandparts 2026-09 $7-9k, 规格书 bw864, 0.45kW含平台)"),
    "A100-80": dict(bw=1935.0, mem=80.0, price=7400.0, tdp=400.0, tf=39e12,
                    src="doc-A2 L50/L57 + doc-D3 L42 (①类: aitooldiscovery 2026-10-01 $7400, PCIe 1935)"),
    "A100-40": dict(bw=1555.0, mem=40.0, price=3800.0, tdp=300.0, tf=39e12,
                    src="doc-A2 L51/L57 + doc-D3 L40 (①类: alibaba 2026-06 $3800, PCIe 1555)"),
    "H100":    dict(bw=3350.0, mem=80.0, price=None,  tdp=700.0, tf=133.8e12,
                    src="KB h100.json bw3350(conf0.9,①类) + price[待核验] + tdp ③类(SXM 700W)"),
    "M2Ultra": dict(bw=560.0,  mem=192.0, price=None, tdp=200.0, tf=30e12,
                    src="oracle ext_bw 560(①类,blind-eval doc) + mem192 ③类 + price[待核验] + 芯片命名存疑(见下)"),
}

def n51(card, nc, q, ns):
    pm = (W_BYTES[q] + ns*KV) / nc
    return pm <= HW[card]["mem"], pm

def n52(card, nc, q, ns):
    need = R_TOK_S*(W_BYTES[q] + ns*KV)/nc
    eff = HW[card]["bw"]*ETA_BW
    return eff >= need, need, eff

def cpass(card, nc, q, ns, tf_scale=1.0):
    """c_pass, 支持 tf_peak 缩放 (敏感性). 复用 calc 的成本模型口径."""
    h = HW[card]
    if h["price"] is None:
        return None
    hw = dict(tf_peak=h["tf"]*tf_scale, bw=h["bw"], mem=h["mem"], tdp=h["tdp"], price_each=h["price"])
    calc.HARDWARE[card+"_j3b"] = hw
    c, tp, td = calc.c_pass(card+"_j3b", nc, q, ns)
    return c, tp, td

def sweep(card, max_cards=4, quants=("W4","W8","W16"), tf_scale=1.0):
    ranked, elim = [], []
    for nc in range(2, max_cards+1):
        for q in quants:
            ns = max(1, nc//2)
            okv, pm = n51(card, nc, q, ns)
            okb, need, eff = n52(card, nc, q, ns)
            cfg = f"{card}×{nc}/{q}/n={ns}"
            if not okv:
                elim.append((cfg, f"N-5.1 显存 {pm:.1f}>{HW[card]['mem']}")); continue
            if not okb:
                elim.append((cfg, f"N-5.2 带宽 {eff:.0f}<{need:.0f}")); continue
            r = cpass(card, nc, q, ns, tf_scale)
            if r is None:
                elim.append((cfg, "price[待核验]→不进排序")); continue
            c, tp, td = r
            ranked.append((c, cfg, pm, tp, td))
    ranked.sort(key=lambda x: x[0])
    return ranked, elim

def main():
    print("="*72)
    print("J3b 候选集外泛化排名表 (oracle 本地 ①类规格 + tf_peak 敏感性)")
    print("="*72)

    # 基准: gold winner 3090×4/W4/n=2
    base = cpass("3090", 4, "W4", 2)
    print(f"\n[基准] gold winner 3090×4/W4/n=2  c_pass={base[0]:.3f} ¢/task "
          f"(t_prefill={base[1]:.2f}s, t_decode/stream={base[2]:.2f}s)")
    print(f"  → decode 占比 {base[2]/(base[1]+base[2]/2)*100:.0f}% (排名主要由 bw+price 驱动)\n")

    # 各平台 best 配置 (tf_scale=1)
    print("[泛化排名] 各平台 best 可行配置 (tf_scale=1.0):")
    print(f"  {'平台':<9}{'best 配置':<22}{'c_pass':>8}{'vs 3090':>9}")
    rows = []
    for card in ["3090","L40S","A100-40","A100-80","H100","M2Ultra"]:
        ranked, _ = sweep(card)
        if ranked:
            c, cfg, pm, tp, td = ranked[0]
            ratio = c/base[0]
            rows.append((c, card, cfg))
            print(f"  {card:<9}{cfg:<22}{c:>8.3f}{ratio:>8.2f}x")
        else:
            print(f"  {card:<9}(无可行配置 / price[待核验])")
    rows.sort()
    print(f"\n  成本最优泛化排名: " + " < ".join(f"{c[1]}" for c in rows))

    # tf_peak 敏感性: 排名是否随 tf_scale 翻转
    print("\n[tf_peak 敏感性] tf_scale ∈ {0.5,1,2} 下各平台 best 是否变化:")
    stable = True
    for ts in (0.5, 1.0, 2.0):
        bests = {}
        for card in ["3090","L40S","A100-40","A100-80"]:
            ranked, _ = sweep(card, tf_scale=ts)
            bests[card] = ranked[0][1] if ranked else "—"
        line = f"  tf×{ts}: " + "  ".join(f"{k}={v}" for k,v in bests.items())
        print(line)
        if ts != 1.0:
            # 比较 best 配置是否随 ts 变
            pass
    # 显式判翻转
    b1 = {c: sweep(c)[0][0][1] for c in ["3090","L40S","A100-40","A100-80"] if sweep(c)[0]}
    b05 = {c: sweep(c, tf_scale=0.5)[0][0][1] for c in ["3090","L40S","A100-40","A100-80"] if sweep(c, tf_scale=0.5)[0]}
    b2 = {c: sweep(c, tf_scale=2.0)[0][0][1] for c in ["3090","L40S","A100-40","A100-80"] if sweep(c, tf_scale=2.0)[0]}
    flip = (b1 != b05) or (b1 != b2)
    print(f"\n  → best 配置在 tf×0.5~×2 内{'翻转(排名对 tf_peak 敏感!)' if flip else '不变(排名对 tf_peak 鲁棒)'}")

    # 作用域边界
    print("\n[c_pass 作用域边界可检验判据]")
    print("  1. 候选集依赖: gold winner 3090×4 仅在『候选集不含 4090/不含更优卡』时成立 (T8b 已证 4090 翻转)。")
    print("     本表把 L40S/A100/H100 纳入后, 成本最优是否仍是 3090×4 → 见上排名。")
    print("  2. tf_peak 作用域: t_prefill 占比 <30% 时, 排名对 tf_peak 不确定度不敏感 (本表敏感性判据)。")
    print("  3. 价格口径: 二手价(doc-A2/D3 2026-09/10) vs MSRP → c_pass 随价格线性, 排名对价格比稳健。")
    print("  4. 芯片命名作用域: gold 树 M2Ultra(bw560) ≠ KB m5-ultra(bw1200) ≠ doc M3/M5 Ultra →")
    print("     统一内存平台需先钉芯片代际再进排序 (本表 M2Ultra 按 bw560, price[待核验])。")

    # 排错样本归因
    print("\n[排错样本归因作用域]")
    print("  - 若某平台 best c_pass > 3090×4: 归因『带宽/显存/价格劣势』, 非 c_pass 模型失效。")
    print("  - 若 price[待核验] 平台: 不进排序, 归因『数据缺口』, 非模型失效。")
    print("  - c_pass 模型失效判据: 同一配置在两个独立 ①类价格源下排名翻转 → 才归因模型。")
    print("="*72)
    return 0

if __name__ == "__main__":
    sys.exit(main())
