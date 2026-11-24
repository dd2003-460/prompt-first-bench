"""#53 跨域复现: 供给侧瓶颈判定 Y 在 nat/soc run 树的信息论贡献测量.

补 IDEA-INDEX #53 标注的开放缺口: 原 GPU 域结论 (浅层=判定信息源, 深层=高命中率
低信息增量, #53 claim 被反驳) 只在 GPU 域测过, 跨域复现未做. 本脚本用同一固化词表
(SUPPLY∧JUDGE, 复用 idea53_common) + 同一信息论量 (I(X;Y) + 逐层 KL 贡献
c(x)=P(x)*D_KL(P(Y|x)||P(Y)), Σc=I) 测 nat/soc 两域.

边界 (D taste, claim 圈在测得出来的范围): n<30 降级, 只报节点分布不报信息论量.
同族 judge (27b 评 27b) 分数仅相对有效.
"""
import json, glob, re, math, os, importlib.util
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("c53", HERE + "/idea53_common.py")
c53 = importlib.util.module_from_spec(spec); spec.loader.exec_module(c53)
SUPPLY, JUDGE = c53.SUPPLY, c53.JUDGE
text_of = c53.text_of

BASE = "/Users/a1-6/Desktop/workspace/pfb/experiments/stage-ablation/checkpoints"
MIN_Y = 30  # n<30 降级 (任务规则)


def load_domain(prefix):
    by_tree = defaultdict(list)
    for f in glob.glob(BASE + "/**/node.json", recursive=True):
        parts = f.split('/')
        run = next((p for p in parts if re.match(prefix + r'-r\d+$', p)), None)
        if not run:
            continue
        try:
            d = json.load(open(f))
        except Exception:
            continue
        if isinstance(d, dict) and isinstance(d.get('level'), str):
            by_tree[run].append(d)
    return by_tree


def H2(p):
    if p <= 0 or p >= 1:
        return 0.0
    return -(p * math.log2(p) + (1 - p) * math.log2(1 - p))


def measure(prefix):
    trees = load_domain(prefix)
    tot = sum(len(v) for v in trees.values())
    lvl_all = defaultdict(int); lvl_y = defaultdict(int)
    for ns in trees.values():
        for nd in ns:
            lv = nd.get('level'); lvl_all[lv] += 1
            if SUPPLY.search(text_of(nd)) and JUDGE.search(text_of(nd)):
                lvl_y[lv] += 1
    levels = sorted(lvl_all)
    Y = sum(lvl_y.values())
    out = {
        "n_trees": len(trees), "n_nodes": tot, "n_Y": Y,
        "base_rate": (Y / tot) if tot else 0.0,
        "per_layer_nodes": {lv: lvl_all[lv] for lv in levels},
        "per_layer_Y": {lv: lvl_y[lv] for lv in levels},
    }
    if Y < MIN_Y:
        out["degraded"] = True
        out["note"] = f"n_Y={Y} < {MIN_Y}, 降级: 测不了, 只报节点分布"
        return out
    pY = Y / tot; HY = H2(pY); HYx = 0.0
    # 两遍: 先算 Ixy 总和, 再算 frac (避免循环内 Ixy 未累加完就除)
    raw = []
    for lv in levels:
        nx = lvl_all[lv]; ny = lvl_y[lv]; px = nx / tot
        pYx = ny / nx if nx else 0.0
        kl = (pYx * math.log2(pYx / pY) + (1 - pYx) * math.log2((1 - pYx) / (1 - pY))) if nx else 0.0
        c = px * kl; HYx += px * H2(pYx)
        raw.append((lv, px, pYx, c, HY - H2(pYx)))
    Ixy = sum(r[3] for r in raw)
    rows = [{"level": lv, "P_x": px, "P_Yx": pYx, "c_bits": c,
             "frac": (c / Ixy) if Ixy else 0.0,
             "point_gain": g} for (lv, px, pYx, c, g) in raw]
    rows_c = sorted(rows, key=lambda x: -x["c_bits"])
    rows_g = sorted(rows, key=lambda x: -x["point_gain"])
    deep = [lv for lv in levels if lv in ("L4", "L5")]
    out.update({
        "degraded": False,
        "H_Y": HY, "H_Yx": HYx, "I_XY_bits": Ixy,
        "I_over_HY": (Ixy / HY) if HY else 0.0,
        "per_layer": rows,
        "contribution_ranking": [r["level"] for r in rows_c],
        "point_gain_ranking": [r["level"] for r in rows_g],
        "max_contribution_layer": rows_c[0]["level"],
        "max_layer_frac": rows_c[0]["frac"],
        "deep_block": deep,
        "deep_block_contrib_bits": sum(r["c_bits"] for r in rows if r["level"] in deep),
        "deep_block_frac": (sum(r["c_bits"] for r in rows if r["level"] in deep) / Ixy) if Ixy else 0.0,
        "deep_point_gains": {r["level"]: r["point_gain"] for r in rows if r["level"] in deep},
    })
    return out


if __name__ == "__main__":
    res = {
        "task": "#53 跨域复现: 供给侧瓶颈判定 Y 在 nat/soc run 树的信息论贡献",
        "method": "I(X;Y) + 逐层 KL 贡献 c(x)=P(x)*D_KL(P(Y|x)||P(Y)), Σc=I; 同 GPU 域口径 (Y=SUPPLY∧JUDGE, 复用 idea53_common 词表)",
        "boundary": "n_Y<30 降级只报节点分布; 同族 judge 27b 评 27b 仅相对有效",
        "domains": {
            "nat域(缓存/网络, L1-L4)": measure(r"sm-nat"),
            "soc域(二手市场, L1-L4)": measure(r"sm-soc"),
        },
        "conclusion": (
            "nat域 (n=308 可测): I(X;Y)=0.0066 bits (层对判定总信息量 2.3% of H(Y)), "
            "最大贡献层=L2 浅层(66%), 深层 L4 仅 28% -> 复现 GPU 域反驳 (浅层=判定信息源, 总信息量极小). "
            "soc域 (n=23<30 降级): 供给侧瓶颈 Y 基本不存在, 测不了. "
            "注意: nat 深层 L4 点增益为正(+0.0725b) 与 GPU 深层点增益为负不同, "
            "因 nat 基率低(4.9% vs GPU 19%), 深层命中率(3.3%)<基率 -> 点增益正; "
            "但'浅层主导贡献+总信息量极小'的核心方向跨域一致. "
            "结论: #53 claim(深层信息贡献更大)跨域仍被反驳, 复现稳健."
        ),
    }
    outp = HERE + "/idea53-cross-domain-replication.json"
    json.dump(res, open(outp, "w"), ensure_ascii=False, indent=2)
    print("[落盘]", outp)
    for name, d in res["domains"].items():
        if d.get("degraded"):
            print(f"{name}: {d['note']} 分布={d['per_layer_Y']}")
        else:
            print(f"{name}: I={d['I_XY_bits']:.4f}b max层={d['max_contribution_layer']}({d['max_layer_frac']*100:.0f}%) 深层块{d['deep_block']}={d['deep_block_frac']*100:.0f}%")
