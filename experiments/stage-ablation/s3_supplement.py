"""G1 supplement: S3 arm (cross-verification) × nat,soc × 30 reps.

S3 = A0 base + cross-verification protocol (≥2 independent sources, adversarial check).
This is the "流程各阶段边际收益" story piece that was missing from the original G1 run
(goal file requires it; original run only did S0/A3/A4).

Usage: python3 s3_supplement.py --reps 30 --out runs-prod-s3
"""
import argparse, json, os, random, sys, time
from s8b_pilot import build_prompt, judge, QUESTIONS, GOLD
from ablation_harness import call_llm

S3_RULE = (
    "【交叉核验协议】回答中每个关键事实/数字，你必须：\n"
    "1. 给出至少两个独立来源的表述（可以是「凭记忆的」不同知识路径，或题面条件+常识推断的两条独立链）；\n"
    "2. 对每条结论做一次对抗检查：假设它是错的，找出最可能的错误模式（口径混淆/量级错误/前提缺失），判断是否成立；\n"
    "3. 如果两条链矛盾，显式报告矛盾点并说明你采信哪条、为什么；\n"
    "4. 最终答案只保留通过对抗检查的结论，未通过的降级为 [待核验] 并说明缺什么信息。\n"
    "输出格式：先给完整推导链（含交叉核验过程），最后单独一节「最终答案」。\n\n"
)

def s3_prompt(qid):
    base = build_prompt("A0", qid)
    return base.replace("问题：", S3_RULE + "问题：")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--reps", type=int, default=30)
    ap.add_argument("--qs", default="nat,soc")
    ap.add_argument("--out", default="runs-prod-s3")
    ap.add_argument("--start-rep", type=int, default=1)
    args = ap.parse_args()

    qs = args.qs.split(",")
    os.makedirs(args.out, exist_ok=True)
    out_f = open(f"{args.out}/run.log", "a")
    t0 = time.time()
    total = len(qs) * max(0, args.reps - args.start_rep + 1)
    done = 0

    for qid in qs:
        for rep in range(args.start_rep, args.reps + 1):
            tag = f"S3-{qid}-r{rep}"
            fp = f"{args.out}/{tag}.json"
            if os.path.exists(fp):
                done += 1
                continue
            prompt = s3_prompt(qid)
            perturb = "".join(random.choice(["\u200b", "\u200c", " ", "\u200d"]) for _ in range(4))
            try:
                ans, usage = call_llm(prompt + perturb, max_tokens=8000)
                if not ans:
                    print(f"[{done+1}/{total}] {tag} EMPTY ({time.time()-t0:.0f}s)", flush=True)
                    continue
                j = judge(qid, ans)
                scores = j.get("scores", [])
                cov = sum(1 for s in scores if s >= 0.5) / max(len(scores), 1)
                rec = {"tag": tag, "arm": "S3", "qid": qid, "rep": rep,
                       "prompt_chars": len(prompt), "answer": ans, "judge": j,
                       "ts": time.strftime("%Y-%m-%dT%H:%M:%S%z")}
                with open(fp, "w") as f:
                    json.dump(rec, f, ensure_ascii=False)
                done += 1
                print(f"[{done}/{total}] {tag} cov={cov:.3f} ({time.time()-t0:.0f}s)", flush=True)
                out_f.write(f"{tag}\tcov={cov:.3f}\n"); out_f.flush()
            except Exception as e:
                print(f"[{done+1}/{total}] {tag} ERROR: {e}", flush=True)

    # summary
    print("\n=== SUMMARY ===")
    for qid in qs:
        coves = []
        per_pt = {}
        for rep in range(1, args.reps + 1):
            fp = f"{args.out}/S3-{qid}-r{rep}.json"
            if not os.path.exists(fp):
                continue
            d = json.load(open(fp))
            scores = d["judge"].get("scores", [])
            coves.append(sum(1 for s in scores if s >= 0.5) / max(len(scores), 1))
            for i, s in enumerate(scores):
                per_pt.setdefault(i, []).append(1 if s >= 0.5 else 0)
        if coves:
            mean = sum(coves) / len(coves)
            sd = (sum((c - mean) ** 2 for c in coves) / max(len(coves) - 1, 1)) ** 0.5
            pts_str = " ".join(f"pt{i+1}:{sum(v)}/{len(v)}" for i, v in sorted(per_pt.items()))
            print(f"S3-{qid}: n={len(coves)} mean={mean:.3f}±{sd:.3f} | {pts_str}")
    print(f"Total wall: {time.time()-t0:.0f}s")
    out_f.close()

if __name__ == "__main__":
    main()