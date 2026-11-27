#!/usr/bin/env python3
"""G1 production run: S0/A3/A4 × Q1-Q5(nat,soc) × n reps, anti-cache, JSONL output.

Arms:
  S0 = A0 baseline (bare researcher prompt)
  A3 = S0 + one-line dimension discipline
  A4 = A3 + few-shot u·T_res example (only meaningful for nat; soc gets same text, that's fine — it's a constant add-on)

Usage: python3 prod_run.py --arms S0,A3,A4 --qs nat,soc --reps 30 --out runs-prod
"""
import argparse, json, os, random, sys, time
from s8b_pilot import build_prompt, judge, QUESTIONS
from ablation_harness import call_llm

A3_RULE = ("硬规则：每个数字写出量纲；每个比率写明分子/分母各是什么口径；"
           "严格区分「访问间隔」（两次被访之间）和「驻留时间」（对象在缓存里能活多久）。")
A4_EXAMPLE = ("参考示例（正确推导格式，注意 T_res 是驻留时间不是访问间隔）：\n"
              "例：某缓存对象平均驻留时间 T_res = 30 天，内容更新率 u = 5%/天。"
              "p_stale = 1 - exp(-u·T_res) = 1 - exp(-1.5) ≈ 0.78。"
              "有效命中率折扣因子 = 1 - p_stale ≈ 0.22。"
              "注意：u·T_res 是无量纲的乘积（1/天 × 天），它才是决定折扣的量。\n\n")

def arm_prompt(arm, qid):
    base = build_prompt("A0", qid)
    if arm == "S0":
        return base
    extra = A3_RULE + "\n"
    if arm == "A4":
        extra += A4_EXAMPLE
    return base.replace("问题：", extra + "问题：")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--arms", default="S0,A3,A4")
    ap.add_argument("--qs", default="nat,soc")
    ap.add_argument("--reps", type=int, default=30)
    ap.add_argument("--out", default="runs-prod")
    ap.add_argument("--start-rep", type=int, default=1, help="resume support")
    args = ap.parse_args()
    os.makedirs(args.out, exist_ok=True)
    arms, qs = args.arms.split(","), args.qs.split(",")
    out_f = open(f"{args.out}/run.log", "a")
    t0 = time.time()
    total = len(arms)*len(qs)*max(0, args.reps-args.start_rep+1)
    done = 0
    for arm in arms:
        for qid in qs:
            for rep in range(args.start_rep, args.reps+1):
                tag = f"{arm}-{qid}-r{rep}"
                fp = f"{args.out}/{tag}.json"
                if os.path.exists(fp):
                    done += 1
                    continue
                prompt = arm_prompt(arm, qid)
                # anti-cache perturbation (invisible zero-width chars) — call_llm also adds its own pad
                perturb = "".join(random.choice(["\u200b","\u200c"," ","\u200d"]) for _ in range(4))
                try:
                    ans, usage = call_llm(prompt + perturb, max_tokens=8000)
                    if not ans:
                        raise RuntimeError("empty answer from LLM")
                    j = judge(qid, ans)
                    rec = {"tag": tag, "arm": arm, "qid": qid, "rep": rep,
                           "prompt_chars": len(prompt), "answer": ans,
                           "judge": j, "ts": time.time()}
                    with open(fp, "w") as f:
                        json.dump(rec, f, ensure_ascii=False)
                    cov = round(j.get("coverage") or 0, 3)
                    done += 1
                    print(f"[{done}/{total}] {tag} cov={cov} ({time.time()-t0:.0f}s)", flush=True)
                    out_f.write(json.dumps({"tag": tag, "cov": cov, "ok": True}, ensure_ascii=False)+"\n"); out_f.flush()
                except Exception as e:
                    print(f"[{done}/{total}] {tag} FAIL {e}", flush=True)
                    out_f.write(json.dumps({"tag": tag, "ok": False, "err": str(e)}, ensure_ascii=False)+"\n"); out_f.flush()
                    time.sleep(10)
    # summary
    agg = {}
    for arm in arms:
        for qid in qs:
            coves = []
            for rep in range(1, args.reps+1):
                fp = f"{args.out}/{arm}-{qid}-r{rep}.json"
                if os.path.exists(fp):
                    r = json.load(open(fp)); coves.append(r["judge"].get("coverage") or 0)
            if coves:
                agg[f"{arm}-{qid}"] = {"n": len(coves), "mean": round(sum(coves)/len(coves),4),
                                       "min": min(coves), "max": max(coves)}
    json.dump(agg, open(f"{args.out}/summary.json","w"), indent=1)
    print("SUMMARY:", json.dumps(agg, indent=1), flush=True)

if __name__ == "__main__":
    main()