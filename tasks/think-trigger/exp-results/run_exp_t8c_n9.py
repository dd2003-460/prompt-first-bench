#!/usr/bin/env python3
# origin: ai
# T8c n=9 补跑脚本：smoke(n=3/臂) 判决=扩样，补 run4-9 追加到 raw_outputs_t8c.json（不覆盖 run1-3）；
# 复用 run_exp_t8c 的冻结 Q/STAGES/caps/call（import 防题面漂移），不改原文件。
# 用法：python3 run_exp_t8c_n9.py all | a | b
import json, os, shutil, sys, time

import run_exp_t8c as base

ORDER = getattr(base, "ORDER", ["01", "02", "02.5", "03", "04", "04.5"])

RUNS = range(4, 10)  # n=9：补 run4-9


def run_arm_a(result, outpath):
    """A 臂补 run4-9：追加到 result['arm_a']（保留已有 run1-3）"""
    for i in RUNS:
        tag = f"A-direct-run{i}"
        t0 = time.time()
        r = base.call([{"role": "user", "content": base.Q}], base.MAX_A, tag)
        r.update({"arm": "A_direct", "run": i, "elapsed_s": round(time.time() - t0, 1),
                  "repeat5": base.repeat_score(r["content"] + r["reasoning"]),
                  "completion_tokens": base.cost(r["usage"])})
        result["arm_a"].append(r)
        print(f"[{tag}] OK content={r['content_chars']} finish={r['finish_reason']} "
              f"tok={r['completion_tokens']} repeat5={r['repeat5']} {r['elapsed_s']}s", flush=True)
        time.sleep(1)
    json.dump(result, open(outpath, "w"), ensure_ascii=False, indent=2)
    print("WROTE arm_a n9", flush=True)


def run_arm_b(result, outpath):
    """B 臂补 run4-9：逐阶段（base.STAGES 顺序），sidecar 写 t8c_stages/B4_*..B9_*，
    每 run 结束 append sample dict（字段与 run_exp_t8c.run_arm_b 完全一致）+ 增量写盘"""
    outdir = os.path.dirname(os.path.abspath(outpath))
    for i in RUNS:
        tag = f"B-pfb-run{i}"
        msgs = [{"role": "user", "content": base.Q}]
        stage_outs = {}
        total_t0 = time.time()
        tot_tok = 0
        for sid in ORDER:
            instr = base.STAGES[sid]
            st0 = time.time()
            cap = base.MAX_B_REVIEW if sid == "04.5" else base.MAX_B
            r = base.call(msgs + [{"role": "user", "content": instr}], cap, f"{tag}-{sid}")
            r.update({"stage": sid, "elapsed_s": round(time.time() - st0, 1),
                      "repeat5": base.repeat_score(r["content"] + r["reasoning"]),
                      "completion_tokens": base.cost(r["usage"])})
            stage_outs[sid] = r
            base.save_stage_sidecar(i, sid, r, outdir)
            tot_tok += base.cost(r["usage"])
            print(f"[{tag}-{sid}] OK content={r['content_chars']} finish={r['finish_reason']} "
                  f"tok={r['completion_tokens']} repeat5={r['repeat5']} {r['elapsed_s']}s", flush=True)
            if r["repeat5"] > 3:
                print(f"[{tag}-{sid}] WARNING: 疑似复读循环 repeat5={r['repeat5']}", flush=True)
            msgs.append({"role": "assistant", "content": r["content"] or r["reasoning"][:500]})
            time.sleep(1)
        final = stage_outs["04.5"]
        sample = {
            "arm": "B_pfb", "run": i,
            "final": final,
            "stages": stage_outs,
            "total_elapsed_s": round(time.time() - total_t0, 1),
            "total_completion_tokens": tot_tok,
            "final_content": final["content"],
            "final_reasoning": final["reasoning"],
        }
        result["arm_b"].append(sample)
        json.dump(result, open(outpath, "w"), ensure_ascii=False, indent=2)
        print(f"[{tag}] DONE total_tok={tot_tok} elapsed={sample['total_elapsed_s']}s "
              f"(incremental)", flush=True)


def main():
    outdir = os.path.dirname(os.path.abspath(__file__))
    outpath = os.path.join(outdir, "raw_outputs_t8c.json")
    bakpath = outpath + ".pre-n9"
    shutil.copy(outpath, bakpath)
    print(f"BACKUP {os.path.basename(outpath)} -> {os.path.basename(bakpath)}", flush=True)
    result = json.load(open(outpath))
    mode = sys.argv[1] if len(sys.argv) > 1 else "all"
    if mode in ("all", "a"):
        run_arm_a(result, outpath)
    if mode in ("all", "b"):
        run_arm_b(result, outpath)
        result["finished_at"] = time.strftime("%Y-%m-%d %H:%M:%S %z")
        json.dump(result, open(outpath, "w"), ensure_ascii=False, indent=2)
        print("WROTE arm_b n9 + finished", flush=True)


if __name__ == "__main__":
    main()
