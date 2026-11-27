#!/usr/bin/env python3
"""q9 run → correctness_layer_v0.judge_text 适配器。

D 2026-11-27: "之前不是说过用公式判断对错了吗, judge 没有接入这个方法?"
→ 接入: 把 Q9 预算扫描的 10 个 run (nodes[].claim 拼接, 同 S5 归一化口径)
  喂进已有的公式/数值机械判 (correctness_layer_v0.judge_text),
  与 llm-judge gate_hit 并排, 看公式判和 LLM-judge 是否给出不同结论。

⚠️ 跨题警告 (2026-11-27 21:15 更正): correctness_layer_v0 锚值来自**选卡题**
  gold (14GB/0.679¢/task/774-1034-1574/winner=V100×4), 而 q9-budget-scan 的
  run 是 **research-AGI 题** (gold=Q9-v2.md, 过程/定义型, 数值锚点仅 2 个)。
  本适配器的 CORR 列对 research-AGI run 只作**诊断** (看公式判在无锚题上的
  行为), **不得**作为"公式判 vs LLM-judge"的有效性对比 — 两把尺子不同题。
  有效对比需在每题各自的 gold 锚值上跑 (选卡题: T8b/S5; research-AGI: 待造
  数值锚点 gold)。

用法: python3 q9_correctness_adapter.py
输出: 每 run 一行 (judge_gate / CORR / S / N / verdict) + 相关性 + JSON 落盘
"""
import json, glob, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from correctness_layer_v0 import judge_text  # noqa: E402

BASE = os.path.join(HERE, "..", "data", "q9-budget-scan")
OUT = os.path.join(HERE, "q9-correctness-adapter-20261127.json")


def load_q9_runs():
    """[(name, text, budget, round), ...] — text = nodes[].claim 拼接 (S5 口径)。"""
    out = []
    for f in sorted(glob.glob(os.path.join(BASE, "q9-*-r*.json"))):
        r = json.load(open(f))
        name = os.path.basename(f).replace(".json", "")
        b = name.split("-")[1]
        rn = name.split("-")[2]
        text = "\n".join(n.get("claim", "") for n in r["nodes"])
        out.append((name, text, b, rn))
    return out


def main():
    runs = load_q9_runs()
    jsum = json.load(open(os.path.join(BASE, "llm-judge-coverage-20261127.json")))["summary"]
    rows = []
    for name, text, b, rn in runs:
        j = judge_text(text)
        jg = jsum.get(b, {}).get("per_run", {}).get(rn)
        rows.append({"run": name, "budget": b, "judge_gate": jg,
                     "CORR": round(j["corr"], 3), "C": round(j["C"], 3),
                     "E": round(j["E"], 3), "S": round(j["S"], 3),
                     "N": round(j["N"], 3), "verdict": j["verdict"]})
    hdr = f"{'run':<28} {'gate':>4} {'CORR':>6} {'S':>5} {'N':>5}  verdict"
    print(hdr)
    for r in rows:
        g = str(r["judge_gate"]) if r["judge_gate"] is not None else "-"
        print(f"{r['run']:<28} {g:>4} {r['CORR']:>6.3f} {r['S']:>5.2f} {r['N']:>5.2f}  {r['verdict']}")
    # 相关性: gate vs CORR / S / N
    def spearman(x, y):
        def rank(v):
            sv = sorted(range(len(v)), key=lambda i: v[i])
            rk = [0] * len(v)
            for p, i in enumerate(sv):
                rk[i] = p + 1
            return rk
        rx, ry = rank(x), rank(y)
        import statistics
        mx, my = statistics.mean(rx), statistics.mean(ry)
        num = sum((a - mx) * (b - my) for a, b in zip(rx, ry))
        den = (sum((a - mx) ** 2 for a in rx) * sum((b - my) ** 2 for b in ry)) ** 0.5
        return num / den if den else float("nan")
    ok = [r for r in rows if r["judge_gate"] is not None]
    G = [r["judge_gate"] for r in ok]
    print(f"\ncorr(gate, CORR) = {spearman(G, [r['CORR'] for r in ok]):+.2f}")
    print(f"corr(gate, S结构) = {spearman(G, [r['S'] for r in ok]):+.2f}")
    print(f"corr(gate, N数值) = {spearman(G, [r['N'] for r in ok]):+.2f}")
    json.dump({"rows": rows}, open(OUT, "w"), ensure_ascii=False, indent=1)
    print(f"\nJSON → {os.path.relpath(OUT)}")


if __name__ == "__main__":
    main()
