#!/usr/bin/env python3
"""q7 719 档 curve JSON 回填脚本 (2026-11-24).

背景: q7-budget-response-curve.json 是手工维护的 (无自动重生成脚本)。
队列跑完每个 rep 会自动把分数 append 到 q7-scan-scores.json (q7_budget_scan_queue.sh L39-55),
watcher 也会自动跑 post-run 协议 + replication-check, 但都不碰 curve JSON。
所以 719 档 r3 落盘后, 需要把 curve JSON 的 719 行从 n=2 升到 n=3 —— 本脚本做这件事,
消除手工算术错误风险 (300-r2 复制污染正是手工口径错误的教训)。

数据源 (权威):
  - q7-scan-scores.json : 每个 rep 的 judge.total / judge.depth / judge.cov / wall_s (队列自动 append)
  - q7-719-r*.json      : 每个 rep 的 run 文件, 用于 claim-set 去重 (排除字节级复制污染)

去重逻辑: 同一 budget 下, 两个 run 文件的 claim-set (节点 claim 集合 sha1) 相同 = 一个是另一个的
字节级复制 (如 300-r2 = 300-r1 复制), 剔除后者。719 档 r1/r2 已核验 SHA 独立, r3 落盘后应为第三
个独立 claim-set。

用法:
  python3 q7-curve-backfill-719.py            # dry-run: 只打印将写入的值, 不改文件
  python3 q7-curve-backfill-719.py --apply    # 实际写入 curve JSON

幂等: 可重复运行; 每次从 q7-scan-scores.json + run 文件重算 719 行, 结果一致。
"""
import glob, json, os, sys, hashlib, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
CURVE = os.path.join(HERE, "q7-budget-response-curve.json")
SCORES = os.path.join(HERE, "q7-scan-scores.json")
BUDGET = 719

def claim_set(run_file):
    """节点 claim 集合 sha1 (与 watcher post-run 协议同口径)."""
    d = json.load(open(run_file))
    cs = hashlib.sha1("|".join(sorted(nd.get("claim", "")[:40] for nd in d["nodes"])).encode()).hexdigest()[:12]
    return cs, len(d["nodes"])

def main():
    apply = "--apply" in sys.argv
    scores = json.load(open(SCORES))
    # 每个 (budget, rep) -> score record
    by_rep = {}
    for rec in scores:
        if rec.get("budget") == BUDGET:
            by_rep[rec.get("rep")] = rec

    # 收集 719 run 文件, 按 rep 解析, claim-set 去重
    runs = sorted(glob.glob(os.path.join(HERE, f"q7-{BUDGET}-r*.json")))
    seen_cs = {}
    kept = []  # (rep, run_file, cs, n_nodes)
    dropped = []
    for f in runs:
        base = os.path.basename(f)
        # 文件名 q7-719-r{rep}-{ts}.json -> rep
        try:
            rep = int(base.split("-r")[1].split("-")[0])
        except (IndexError, ValueError):
            continue
        cs, n = claim_set(f)
        if cs in seen_cs:
            dropped.append((rep, base, seen_cs[cs]))
            continue
        seen_cs[cs] = base
        kept.append((rep, base, cs, n))

    # 按 rep 取分数
    reps_with_score = []
    for rep, base, cs, n in kept:
        rec = by_rep.get(rep)
        if rec is None:
            print(f"[warn] rep {rep} ({base}) 在 q7-scan-scores.json 无分数记录 — 跳过 (r3 落盘后队列会自动 append)")
            continue
        reps_with_score.append((rep, rec, base, n))

    if not reps_with_score:
        print("[abort] 719 档无可用 rep — 不写")
        return

    jts = [r[1]["judge"]["total"] for r in reps_with_score]
    covs = [r[1]["judge"]["cov"] for r in reps_with_score]
    depths = [r[1]["judge"].get("depth") for r in reps_with_score if r[1]["judge"].get("depth") is not None]
    walls = [r[1]["wall_s"] for r in reps_with_score]
    n_reps = len(reps_with_score)

    new_row_vals = {
        "n_reps": n_reps,
        "judge_total_mean": round(sum(jts) / n_reps, 4),
        "judge_total_min": round(min(jts), 4),
        "judge_total_max": round(max(jts), 4),
        "cov_mean": round(sum(covs) / n_reps, 4),
    }
    if depths:
        new_row_vals["depth_mean"] = round(sum(depths) / len(depths), 3)
    if walls:
        new_row_vals["wall_s_mean"] = round(sum(walls) / len(walls))

    print(f"=== 719 档回填 (dry-run={'NO' if apply else 'YES'}) ===")
    print(f"独立 rep: {[(r[0], r[2][:8], 'n='+str(r[3])) for r in reps_with_score]}")
    if dropped:
        print(f"剔除复制: {[(r[0], r[1], 'cs 同 '+r[2]) for r in dropped]}")
    print("将写入 719 行:")
    for k, v in new_row_vals.items():
        print(f"  {k} = {v}")
    print(f"  (逐 rep judge.total={[round(x,4) for x in jts]}, cov={[round(x,4) for x in covs]})")

    if not apply:
        print("\n[dry-run] 未写文件。确认后加 --apply 写入。")
        return

    curve = json.load(open(CURVE))
    for row in curve["rows"]:
        if row.get("budget") == BUDGET:
            before = {k: row.get(k) for k in new_row_vals}
            row.update(new_row_vals)
            row["note"] = (
                f"n={n_reps} 独立 rep (claim-set 去重); 逐 rep judge.total="
                f"{[round(x,4) for x in jts]} cov={[round(x,4) for x in covs]}; "
                f"回填时间 {datetime.datetime.now().astimezone().isoformat(timespec='seconds')} "
                f"(q7-curve-backfill-719.py)"
            )
            print(f"\n[applied] 719 行 before={before}")
            print(f"[applied] 719 行 after ={ {k: row.get(k) for k in new_row_vals} }")
            break
    curve["updated_at"] = datetime.datetime.now().astimezone().isoformat(timespec="seconds")
    curve["pending"] = f"719 档已回填 n={n_reps} (r1/r2/r3 独立); 300 档 n=2 独立 rep 不变 (r2 复制已剔除)"
    curve["source"] = f"q7-scan-scores.json ({len(scores)} 条; 719 n={n_reps} 独立 claim-set, 300-r2 复制剔除)"
    json.dump(curve, open(CURVE, "w"), ensure_ascii=False, indent=1)
    print(f"[applied] curve JSON 已写: {CURVE}")

if __name__ == "__main__":
    main()
