#!/usr/bin/env python3
"""bare arm 生产并发 batch（2026-11-21, D 指令：先跑生产环境，更真实，多轮看噪声模式）。

与串行版（bare_arm_batch.py）的区别：
  - 4 个 worker 并发跑（模拟生产 continuous batching 条件）
  - 输出到 runs_prod/（与串行 runs/ 分开，两套数据回答不同问题：
    串行=管线值多少（消融），并发=生产条件下管线还值多少+噪声模式）
  - 协议/目标/工具与串行版完全一致（完整目标描述+模型自规划自定 vs pfb 状态机）
  - 跳过 runs_prod/ 里已存在的 run（断点续跑）

注意：并发下 vLLM batch 组合引入浮点非确定性（T53b verification.md 已证），
本数据不可逐 token 复现，统计看分布+噪声模式，不和串行数据直接比绝对值。
"""
import concurrent.futures as cf
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
PFB_ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
RUNS = os.path.join(PFB_ROOT, "modules/B-pipeline-ablation/data/t53b/runs_prod")
NOTES = os.path.join(PFB_ROOT, "modules/B-pipeline-ablation/data/t53b/notes")
LOG = os.path.join(NOTES, "bare-batch-prod.log")
os.makedirs(RUNS, exist_ok=True)
os.makedirs(NOTES, exist_ok=True)

WORKERS = 4
qids = ["gpu", "nat", "soc"]  # gpu 最权威优先（D 2026-11-21）
rounds = [f"r{i:02d}" for i in range(1, 11)]


def log(msg):
    line = f"[{time.strftime('%H:%M:%S')}] {msg}"
    print(line, flush=True)
    with open(LOG, "a") as f:
        f.write(line + "\n")


def work(qid, rid):
    out = os.path.join(RUNS, f"{qid}_bare_{rid}.json")
    if os.path.exists(out):
        return f"skip {qid} {rid} (exists)"
    t0 = time.time()
    r = subprocess.run(
        [sys.executable, os.path.join(HERE, "bare_arm_run.py"), qid, rid,
         "--runs-dir", RUNS],
        capture_output=True, text=True, cwd=HERE)
    tail = (r.stdout.strip().splitlines() or [""])[-1]
    dt = time.time() - t0
    if r.returncode == 0 and os.path.exists(out):
        return f"OK {qid} {rid} {dt:.0f}s | {tail}"
    return f"FAIL {qid} {rid} rc={r.returncode} | {r.stderr.strip()[-200:]}"


tasks = [(q, r) for q in qids for r in rounds]
log(f"PROD BATCH start: {len(tasks)} tasks, {WORKERS} workers, runs={RUNS}")
ok = fail = skip = 0
with cf.ThreadPoolExecutor(max_workers=WORKERS) as ex:
    futs = {ex.submit(work, q, r): (q, r) for q, r in tasks}
    for fut in cf.as_completed(futs):
        res = fut.result()
        log(res)
        if res.startswith("OK"):
            ok += 1
        elif res.startswith("FAIL"):
            fail += 1
        else:
            skip += 1
log(f"PROD BATCH DONE: ok={ok} fail={fail} skip={skip}")
