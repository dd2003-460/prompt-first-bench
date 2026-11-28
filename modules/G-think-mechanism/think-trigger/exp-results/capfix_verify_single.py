#!/usr/bin/env python3
# T8c-CapFix-Verify 单 run 验证脚本（2026-11-27）
# 目的：验证 04.5 cap=16384 修复后 B 臂单样本不再截断
# 逻辑 = run_exp_t8c.run_arm_b 的单 run 版（逐行同源，只跑 run1，输出到新文件）
# 用法：setsid nohup python3 capfix_verify_single.py > LOG 2>&1 &
import json, time, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import run_exp_t8c as m

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "capfix-verify-outputs.json")
# sidecar 隔离目录：绝不覆盖 smoke 的 t8c_stages/（数据可追溯性）
SIDECAR_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "t8c_stages_capfix-verify")
os.makedirs(SIDECAR_DIR, exist_ok=True)

result = {"meta": {"experiment": "T8c CapFix-Verify (04.5 cap=16384, 单 run)",
                   "model": m.MODEL, "temperature": m.TEMP,
                   "max_b": m.MAX_B, "max_b_review_045": m.MAX_B_REVIEW,
                   "started_at": time.strftime("%Y-%m-%d %H:%M:%S %z")},
          "arm_a": [], "arm_b": []}

i = 1  # 只跑 run1
tag = f"B-pfb-run{i}"
msgs = [{"role": "user", "content": m.Q}]
stage_outs = {}
total_t0 = time.time()
tot_tok = 0
for sid, instr in m.STAGES.items():
    st0 = time.time()
    cap = m.MAX_B_REVIEW if sid == "04.5" else m.MAX_B
    r = m.call(msgs + [{"role": "user", "content": instr}], cap, f"{tag}-{sid}")
    r.update({"stage": sid, "elapsed_s": round(time.time() - st0, 1),
              "repeat5": m.repeat_score(r["content"] + r["reasoning"]),
              "completion_tokens": m.cost(r["usage"])})
    stage_outs[sid] = r
    # 自定义 sidecar（m.save_stage_sidecar 硬编码写 t8c_stages/ 会覆盖 smoke 数据）
    json.dump(r, open(os.path.join(SIDECAR_DIR, f"B{i}_{sid}.json"), "w"),
              ensure_ascii=False, indent=2)
    tot_tok += m.cost(r["usage"])
    print(f"[{tag}-{sid}] OK content={r['content_chars']} finish={r['finish_reason']} "
          f"tok={r['completion_tokens']} repeat5={r['repeat5']} {r['elapsed_s']}s", flush=True)
    if r["repeat5"] > 3:
        print(f"[{tag}-{sid}] WARNING: 疑似复读循环 repeat5={r['repeat5']}", flush=True)
    msgs.append({"role": "assistant", "content": r["content"] or r["reasoning"][:500]})
    time.sleep(1)
final = stage_outs["04.5"]
result["arm_b"].append({
    "arm": "B_pfb", "run": i, "final": final, "stages": stage_outs,
    "total_elapsed_s": round(time.time() - total_t0, 1),
    "total_completion_tokens": tot_tok,
    "final_content": final["content"], "final_reasoning": final["reasoning"],
})
result["finished_at"] = time.strftime("%Y-%m-%d %H:%M:%S %z")
json.dump(result, open(OUT, "w"), ensure_ascii=False, indent=2)
print(f"WROTE {OUT}")
print(f"VERDICT: 04.5 finish={final['finish_reason']} "
      f"tok={final['completion_tokens']} (旧截断值 12288)")
