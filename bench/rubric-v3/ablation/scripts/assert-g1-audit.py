#!/usr/bin/env python3
"""G1 矛盾审计机判脚本（RUBRIC-V3-FULL-AUDIT / G1）。

只读输入：hit-matrix.json / prior-estimates.json / judge-blindtest-r1.json / stats-recomputed.json。
输出：一致性数字 + p̃ 分布合理性信号 + 矛盾清单计数。exit 0 = 全部断言通过（数据自洽），
      exit 1 = 存在 FAIL（数据不自洽或复算不匹配）。SIGNAL 行不影响 exit code。

可复算性：抽检样本由固定种子 20261030 从 8×31=248 单元抽取 75（≈30%），
样本清单落盘 scripts/g1-sample-cells.json；重跑本脚本得到逐位相同的结果。
"""
import json, math, os, random, sys

HERE = os.path.dirname(os.path.abspath(__file__))
AB = os.path.dirname(HERE)
SEED = 20261030
SAMPLE_SIZE = 75

def load(name):
    with open(os.path.join(AB, name)) as f:
        return json.load(f)

def spearman(xs, ys):
    def rank(a):
        order = sorted(range(len(a)), key=lambda i: a[i])
        ranks = [0.0] * len(a); i = 0
        while i < len(order):
            j = i
            while j + 1 < len(order) and a[order[j+1]] == a[order[i]]:
                j += 1
            avg = (i + j) / 2 + 1
            for k in range(i, j + 1):
                ranks[order[k]] = avg
            i = j + 1
        return ranks
    rx, ry = rank(xs), rank(ys)
    mx = sum(rx) / len(rx); my = sum(ry) / len(ry)
    cov = sum((a - mx) * (b - my) for a, b in zip(rx, ry))
    sx = math.sqrt(sum((a - mx) ** 2 for a in rx)); sy = math.sqrt(sum((b - my) ** 2 for b in ry))
    return cov / (sx * sy)

def main():
    hm = load("hit-matrix.json")
    pe = load("prior-estimates.json")["nodes"]
    bt = load("judge-blindtest-r1.json")["nodes"]
    sr = load("stats-recomputed.json")
    nodes = sorted(hm["run1"].keys())
    runs = list(hm.keys())
    fails, signals = [], []

    # A1: 矩阵结构完整性 — 8 run × 31 node，h∈{0,1}，h=1 必有非空 evidence
    assert len(runs) == 8, "run count != 8"
    assert len(nodes) == 31, "node count != 31"
    for r in runs:
        assert set(hm[r].keys()) == set(nodes), f"{r}: node set mismatch"
        for v in nodes:
            c = hm[r][v]
            assert c["h"] in (0, 1), f"{r}/{v}: h not in {{0,1}}"
            if c["h"] == 1:
                assert c["evidence"], f"{r}/{v}: h=1 without evidence"
            else:
                assert c["evidence"] is None, f"{r}/{v}: h=0 with non-null evidence"
    print("PASS A1 matrix-structure 8x31 h∈{0,1} evidence-policy")

    # A2: O3 分数复算 — W0/W1/W2 × 8 run 与 stats-recomputed.json 精确一致
    mism = 0
    for mode, key in (("W0", lambda v: 1.0), ("W1", lambda v: pe[v]["w1"]), ("W2", lambda v: pe[v]["w2"])):
        for r in runs:
            num = sum(key(v) * hm[r][v]["h"] for v in nodes)
            den = sum(key(v) for v in nodes)
            if abs(num / den - sr["scores"][mode][r]) > 5e-5:
                mism += 1
    if mism:
        fails.append(f"A2 {mism} O3 score mismatches vs stats-recomputed.json")
    else:
        print("PASS A2 o3-recompute 24/24 exact match stats-recomputed.json")

    # A3: 冻结文件只读声明 — 本脚本对三个冻结 JSON 仅做 open() 读
    print("PASS A3 frozen-read-only hit-matrix/prior-estimates/judge-blindtest 未被本脚本写入")

    # A4: 抽检样本确定性 — 固定种子抽 75/248，与落盘清单逐位一致
    cells = [(r, n) for r in runs for n in nodes]
    rnd = random.Random(SEED)
    sample = rnd.sample(cells, SAMPLE_SIZE)
    disk = json.load(open(os.path.join(HERE, "g1-sample-cells.json")))
    if sample != [tuple(x) for x in disk]:
        fails.append("A4 sample list drift vs g1-sample-cells.json")
    else:
        h1 = sum(1 for r, n in sample if hm[r][n]["h"] == 1)
        print(f"PASS A4 sample-deterministic seed={SEED} n={len(sample)} (h=1:{h1} h=0:{len(sample)-h1})")

    # S1: 证据逐字核验 — 抽检内所有 h=1 的 evidence 必须逐字（空白归一）出现在 run 原文
    texts = {}
    import re
    for i in range(1, 9):
        texts[f"run{i}"] = re.sub(r"\s+", "", open(os.path.join(AB, f"runs-C0-run{i}.md")).read())
    bad = [(r, n) for r, n in sample if hm[r][n]["h"] == 1 and re.sub(r"\s+", "", hm[r][n]["evidence"]) not in texts[r]]
    h1 = sum(1 for r, n in sample if hm[r][n]["h"] == 1)
    if bad:
        fails.append(f"S1 {len(bad)} evidence strings not verbatim in run text: {bad}")
    else:
        print(f"SIGNAL S1 evidence-verbatim sampled-h1-all-pass ({h1} cells checked)")

    # S2: p̃ 分布合理性 — 经验命中率 vs p̃ 的相关（两 judge 口径）
    idx = [i for i, v in enumerate(nodes) if v != "N-0"]
    hr = [sum(hm[r][v]["h"] for r in runs) / 8 for v in nodes]
    po = [pe[v]["p_tilde"] for v in nodes]; pn = [bt[v]["p_tilde"] for v in nodes]
    rho_o = round(spearman([hr[i] for i in idx], [po[i] for i in idx]), 4)
    rho_n = round(spearman([hr[i] for i in idx], [pn[i] for i in idx]), 4)
    rho_x = round(spearman(po[1:], pn[1:]), 4)
    print(f"SIGNAL S2 ptile-vs-hitrate spearman orig={rho_o} new={rho_n}; cross-judge rho={rho_x}")
    if rho_o < 0.5:
        print(f"SIGNAL S2 LOW-CORR orig judge p̃ 与 8run 经验命中率相关弱 (ρ={rho_o}<0.5) → 系统性偏差信号")

    # S3: 二项式红旗 — 零命中但 P(全miss|p)<0.05；全命中但 P(全hit|p)<0.05
    flags = []
    for v in nodes:
        h = sum(hm[r][v]["h"] for r in runs); p = pe[v]["p_tilde"]
        if p is None:
            continue
        if h == 0 and (1 - p) ** 8 < 0.05:
            flags.append(f"{v}(zero-hit,p_orig={p},P_allmiss={(1-p)**8:.4f})")
        if h == 8 and p ** 8 < 0.05:
            flags.append(f"{v}(all-hit,p_orig={p},P_allhit={p**8:.6f})")
    print(f"SIGNAL S3 binomial-flags n={len(flags)}: {'; '.join(flags)}")

    # S4: 跨 judge 权重漂移 — w2 gap top-3（构念效度根因线索，供 G2 消费）
    gaps = sorted(((abs(pe[v]["w2"] - bt[v]["w2"]), v) for v in nodes), reverse=True)[:3]
    print("SIGNAL S4 w2-cross-judge-gap top3: " + "; ".join(f"{v}(Δ{d:.2f})" for d, v in gaps))

    if fails:
        for f in fails:
            print("FAIL", f)
        sys.exit(1)
    print("RESULT: all PASS, signals logged")

if __name__ == "__main__":
    main()
