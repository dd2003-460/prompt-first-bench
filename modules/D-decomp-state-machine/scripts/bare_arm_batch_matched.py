#!/usr/bin/env python3
"""bare arm 匹配负载 batch（2026-11-21, D 指令：两臂相同负载下跑）。

与生产并发版（bare_arm_batch_prod.py, 4 workers 全压同一题）的区别：
  - 3 路并发、每 qid 一路、线内串行 —— 与 T53b SM 臂的采集结构
    （nat/soc/gpu 三线同时起、线内串行, t53b-batch-*.log 2026-11-20 01:51:12）一致
  - 输出到 runs_matched/（与 runs/ 串行、runs_prod/ 4 路并发分开）
  - 协议/目标/工具与前两版完全一致

目的：裸臂 vs SM 臂唯一变量 = pipeline。搜索通道状态随时间漂移不可控
（ego 超时/DDG 限流），但并发结构可以且必须对齐——否则"4 路裸 vs 3 路 SM"
混入基础设施负载变量。
"""
import concurrent.futures as cf
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
PFB_ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
RUNS = os.path.join(PFB_ROOT, "modules/B-pipeline-ablation/data/t53b/runs_matched")
NOTES = os.path.join(PFB_ROOT, "modules/B-pipeline-ablation/data/t53b/notes")
LOG = os.path.join(NOTES, "bare-batch-matched.log")
os.makedirs(RUNS, exist_ok=True)
os.makedirs(NOTES, exist_ok=True)

qids = ["nat", "soc", "gpu"]
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


def lane(qid):
    """一个 qid 一路：线内串行（与 T53b SM 臂同结构）。"""
    for rid in rounds:
        res = work(qid, rid)
        log(res)


log(f"MATCHED BATCH start: 3 lanes x 10 rounds, runs={RUNS}")
t0 = time.time()
with cf.ThreadPoolExecutor(max_workers=3) as ex:
    futs = [ex.submit(lane, q) for q in qids]
    for f in cf.as_completed(futs):
        f.result()
log(f"MATCHED BATCH DONE in {time.time()-t0:.0f}s")
