#!/usr/bin/env python3
"""bare arm batch: 3 题 × 10 轮，串行跑（8787 单模型，并发会触发非确定性）。
跳过已存在的 run 文件（断点续跑）。日志 tee 到 notes/bare-batch.log。
用法: python3 bare_arm_batch.py
"""
import subprocess, sys, os, time
HERE = os.path.dirname(os.path.abspath(__file__))
NOTES = os.path.abspath(os.path.join(HERE, "..", "..", "modules/B-pipeline-ablation/data/t53b/notes"))
os.makedirs(NOTES, exist_ok=True)
LOG = os.path.join(NOTES, "bare-batch.log")

def log(msg):
    line = f"[{time.strftime('%H:%M:%S')}] {msg}"
    print(line, flush=True)
    with open(LOG, "a") as f:
        f.write(line + "\n")

qids = ["nat", "soc", "gpu"]
rounds = [f"r{i:02d}" for i in range(1, 11)]
total, done, failed = 0, 0, 0
for qid in qids:
    for rid in rounds:
        out = os.path.join(NOTES, "..", "runs", f"{qid}_bare_{rid}.json")
        out = os.path.abspath(out)
        if os.path.exists(out):
            log(f"skip {qid} {rid} (exists)")
            continue
        total += 1
        t0 = time.time()
        r = subprocess.run([sys.executable, os.path.join(HERE, "bare_arm_run.py"),
                            qid, rid], capture_output=True, text=True, cwd=HERE)
        tail = (r.stdout.strip().splitlines() or [""])[-1]
        if r.returncode == 0 and os.path.exists(out):
            done += 1
            log(f"OK {qid} {rid} {time.time()-t0:.0f}s | {tail}")
        else:
            failed += 1
            log(f"FAIL {qid} {rid} rc={r.returncode} | {r.stderr.strip()[-200:]}")
log(f"BATCH DONE: total={total} ok={done} fail={failed}")
