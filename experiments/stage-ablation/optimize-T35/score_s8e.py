#!/usr/bin/env python3
"""T35 评分：复用现有 score.py:score_run，对 S7/S7V/S8E 在 Q1/Q4×r1,r2 共 12 run 本地重算。

- 口径：score.py 6 维（M1/M4 为同族 27B 单 judge，标注 qwen3.8-27b ×1, non-IRR；
  M6 为 URL 存活检查）。与 paper §4.1 主表同口径（见 01-research.md §0 复算证明）。
- gold：gold/Q1.md、gold/Q4.md（仓库内自带，README/paper §3.3 指向的 gold/ 目录）。
- 三臂用同一 gold、同一 judge、同一 scorer → 可直接比较。
- 禁代理：urllib 直连（等效 curl --noproxy '*'）；本地端点与 arxiv 均直连可达。
- 输出：scores.json（全量，可复核）、scores-summary.txt（per-question 表）。
"""
import json, os, sys, urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(HERE)
sys.path.insert(0, BASE)

# 显式禁代理（等效 curl --noproxy '*'）：本地 :8787 直连，arxiv 直连已验证可达
urllib.request.install_opener(
    urllib.request.build_opener(urllib.request.ProxyHandler({}))
)
import score as scorer  # noqa: E402

GOLD = {
    q: open(os.path.join(BASE, "gold", q + ".md"), encoding="utf-8").read()
    for q in ("Q1", "Q4")
}

PLAN = [(arm, q, r) for arm in ("S7", "S7V", "S8E")
        for q in ("Q1", "Q4") for r in (1, 2)]


def path_for(arm, q, r):
    if arm == "S8E":
        return os.path.join(HERE, "runs", f"S8E-{q}-r{r}.json")
    return os.path.join(BASE, "runs", f"{arm}-{q}-r{r}.json")


def one(item):
    arm, q, r = item
    return scorer.score_run(path_for(arm, q, r), GOLD[q], arm, q)


def main():
    results = []
    with ThreadPoolExecutor(max_workers=4) as ex:
        futs = {ex.submit(one, it): it for it in PLAN}
        for f in as_completed(futs):
            it = futs[f]
            try:
                s = f.result()
                s["_tag"] = f"{it[0]}-{it[1]}-r{it[2]}"
                results.append(s)
                print(f"  [{s['_tag']}] total={s['total']:.4f} "
                      f"M1={s['scores']['M1']:.3f} M4={s['scores']['M4']:.3f} "
                      f"M6={s['scores']['M6']:.3f}", flush=True)
            except Exception as e:
                print(f"  [{it}] SCORE ERROR: {e}", flush=True)

    results.sort(key=lambda s: (s["arm"], s["qid"], s["rep"]))
    with open(os.path.join(HERE, "scores.json"), "w", encoding="utf-8") as f:
        json.dump({
            "judge": "qwen3.8-27b x1, non-IRR (same-family single judge)",
            "scorer": "score.py:score_run (6-dim, WEIGHTS M1 .25/M2 .20/M3 .15/M4 .20/M5 .10/M6 .10)",
            "gold": "gold/Q1.md, gold/Q4.md",
            "runs": results,
        }, f, ensure_ascii=False, indent=2)

    # per-question 汇总（r1,r2 均值）
    lines = ["# T35 per-question 汇总（score.py 6 维口径，本地重算）", "",
             f"> judge: qwen3.8-27b x1, non-IRR  |  n=2 reps per arm×Q",
             "", "| Arm | Q | M1 | M4 | M6 | Total |", "|---|---|---|---|---|---|"]
    summary = {}
    for arm in ("S7", "S7V", "S8E"):
        for q in ("Q1", "Q4"):
            rs = [s for s in results if s["arm"] == arm and s["qid"] == q]
            if not rs:
                continue
            def avg(k):
                return sum(s[k] for s in rs) / len(rs)
            def avgsc(k):
                return sum(s["scores"][k] for s in rs) / len(rs)
            m1, m4, m6, tot = avgsc("M1"), avgsc("M4"), avgsc("M6"), avg("total")
            summary[f"{arm}-{q}"] = {"M1": round(m1, 4), "M4": round(m4, 4),
                                     "M6": round(m6, 4), "total": round(tot, 4), "n": len(rs)}
            lines.append(f"| {arm} | {q} | {m1:.4f} | {m4:.4f} | {m6:.4f} | {tot:.4f} |")
    lines += ["", "## 逐 run 明细", "",
              "| Arm | Q | Rep | M1 | M2 | M3 | M4 | M5 | M6 | Total | wall_s | tok_out |",
              "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for s in results:
        sc = s["scores"]
        lines.append(
            f"| {s['arm']} | {s['qid']} | r{s['rep']} | {sc['M1']:.3f} | {sc['M2']:.3f} | "
            f"{sc['M3']:.3f} | {sc['M4']:.3f} | {sc['M5']:.3f} | {sc['M6']:.3f} | "
            f"{s['total']:.4f} | {s['wall_s']} | {s['tokens'].get('out', '?')} |")
    txt = "\n".join(lines) + "\n"
    with open(os.path.join(HERE, "scores-summary.txt"), "w", encoding="utf-8") as f:
        f.write(txt)
    print("\n" + txt)
    print("Saved: scores.json / scores-summary.txt")


if __name__ == "__main__":
    main()
