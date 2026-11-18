#!/usr/bin/env python3
"""T53b watcher v2：监控 s5_state_machine.py 进程，进程退出后处理输出。

CC 跑 s5_state_machine.py 时，watcher 监控进程。
进程退出（run 完成）后：
1. 复制 runs-s5-sm-{qid}-synth.json 到 ablation-runs/
2. 跑 judge
3. 更新 ablation-results.json
4. 写过程 note
5. 更新 cc-state.json

用法: python3 ablation_watcher.py（后台跑）
"""
import json, os, shutil, sys, time, hashlib, subprocess
from datetime import datetime

STAGE_DIR = os.path.dirname(os.path.abspath(__file__))
PFB_ROOT = os.path.dirname(os.path.dirname(STAGE_DIR))
ABLATION_RUNS = os.path.join(STAGE_DIR, "ablation-runs")
ABLATION_NOTES = os.path.join(STAGE_DIR, "ablation-notes")
RESULTS_FILE = os.path.join(STAGE_DIR, "ablation-results.json")
CC_STATE_FILE = os.path.join(PFB_ROOT, "tasks", "T53-bus", "cc-state.json")
WATCH_LOG = os.path.join(STAGE_DIR, "ablation-watcher.log")

def log(msg):
    ts = datetime.now().strftime("%H:%M:%S")
    line = f"[{ts}] {msg}"
    print(line, flush=True)
    with open(WATCH_LOG, "a") as f:
        f.write(line + "\n")

def get_sm_processes():
    """找所有 s5_state_machine.py 进程，返回 [(pid, qid, arm), ...]"""
    procs = []
    try:
        r = subprocess.run("ps aux | grep 's5_state_machine.py' | grep -v grep",
                          shell=True, capture_output=True, text=True)
        for line in r.stdout.strip().split("\n"):
            if not line:
                continue
            parts = line.split()
            if len(parts) < 11:
                continue
            pid = parts[1]
            cmd = " ".join(parts[10:])
            # 提取 qid
            qid = None
            for q in ["gpu", "nat", "soc"]:
                if f" {q} " in f" {cmd} " or cmd.endswith(f" {q}"):
                    qid = q
                    break
            # 提取 arm
            arm = "formula" if "--obj-mode=formula" in cmd or "--obj-mode" not in cmd else "text"
            if qid:
                procs.append((pid, qid, arm))
    except Exception as e:
        log(f"[error] get_sm_processes: {e}")
    return procs

def get_next_pending_run(qid, arm):
    """从 cc-state.json 取第一个 done=false 的 {qid}_{arm}_rNN run。"""
    if not os.path.exists(CC_STATE_FILE):
        return None
    with open(CC_STATE_FILE) as f:
        d = json.load(f)
    prefix = f"{qid}_{arm}_r"
    for wu in d.get("work_units", []):
        if not wu.get("done") and wu.get("name", "").startswith(prefix):
            return wu
    return None

def process_run(qid, arm, round_num, src_json):
    """处理一个完成的 run。"""
    run_name = f"{qid}_{arm}_r{round_num:02d}"
    dst_json = os.path.join(ABLATION_RUNS, f"{run_name}.json")

    # 1. 复制
    shutil.copy2(src_json, dst_json)
    log(f"[copy] {run_name} → ablation-runs/")

    # 2. 读 run 数据
    with open(dst_json) as f:
        run_data = json.load(f)
    answer = run_data.get("answer", "")
    coverage = run_data.get("coverage")
    depth = run_data.get("depth_score")
    n_nodes = run_data.get("n_nodes", 0)

    # 3. 跑 judge
    judge_result = None
    try:
        sys.path.insert(0, STAGE_DIR)
        from judge_v2_depth import score_run
        if answer:
            judge_result = score_run(qid, answer)
            judge_path = os.path.join(ABLATION_RUNS, f"{run_name}_judge.json")
            with open(judge_path, "w") as f:
                json.dump(judge_result, f, ensure_ascii=False, indent=2)
            depth = judge_result.get("overall", depth)
            log(f"[judge] {run_name} overall={depth}")
    except Exception as e:
        log(f"[judge] ERROR {run_name}: {e}")

    # 4. 检查 L1 不确定性维度（从 checkpoint 文件读 nodes）
    l1_unc = False
    ckpt_dir = os.path.join(STAGE_DIR, "checkpoints")
    if os.path.exists(ckpt_dir):
        # 找最新的 sm-{qid}-r*.json
        import glob
        ckpts = sorted(glob.glob(os.path.join(ckpt_dir, f"sm-{qid}-r*.json")))
        if ckpts:
            with open(ckpts[-1]) as f:
                ckpt = json.load(f)
            nodes = ckpt.get("nodes", [])
            for n in nodes:
                if n.get("level") == "L1":
                    claim = n.get("claim", "")
                    scope = n.get("scope", "") or n.get("description", "")
                    if any(claim.lower().startswith(kw) for kw in ["不确定性", "随机", "uncertainty", "stochastic"]):
                        if any(kw in scope for kw in ["横切", "作用于", "cross-cut", "affect"]):
                            l1_unc = True
                            break

    # 5. 更新 ablation-results.json
    if os.path.exists(RESULTS_FILE):
        with open(RESULTS_FILE) as f:
            results = json.load(f)
    else:
        results = {"runs": []}
    results["runs"] = [r for r in results["runs"] if not (r["qid"] == qid and r["arm"] == arm and r["round"] == round_num)]
    results["runs"].append({
        "qid": qid, "arm": arm, "round": round_num,
        "coverage": coverage, "depth": depth,
        "n_nodes": n_nodes,
        "l1_uncertainty": l1_unc,
        "run_file": f"ablation-runs/{run_name}.json",
        "judge_file": f"ablation-runs/{run_name}_judge.json" if judge_result else None,
        "timestamp": datetime.now().astimezone().isoformat(),
    })
    with open(RESULTS_FILE, "w") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    log(f"[results] {run_name} cov={coverage} depth={depth} nodes={n_nodes} l1_unc={l1_unc}")

    # 6. 写过程 note
    note_path = os.path.join(ABLATION_NOTES, f"{run_name}.md")
    note = f"""# {qid} {arm} r{round_num:02d}

- 时间: {datetime.now().astimezone().isoformat()}
- 节点数: {n_nodes}
- coverage: {coverage}
- depth: {depth}
- L1 不确定性维度: {'是' if l1_unc else '否'}
- 观察: （watcher 自动记录）
"""
    with open(note_path, "w") as f:
        f.write(note)

    # 7. 更新 cc-state.json
    if os.path.exists(CC_STATE_FILE):
        with open(CC_STATE_FILE) as f:
            cc_state = json.load(f)
        for wu in cc_state.get("work_units", []):
            if wu.get("name") == run_name:
                wu["done"] = True
                break
        with open(CC_STATE_FILE, "w") as f:
            json.dump(cc_state, f, ensure_ascii=False, indent=2)
        log(f"[state] {run_name} done=true")

def main():
    log("=== watcher v2 started (process monitoring) ===")
    os.makedirs(ABLATION_RUNS, exist_ok=True)
    os.makedirs(ABLATION_NOTES, exist_ok=True)

    # 记录正在监控的进程
    monitored = {}  # pid -> (qid, arm, start_time)

    while True:
        try:
            # 找当前在跑的 s5_state_machine 进程
            sm_procs = get_sm_processes()
            current_pids = set(p[0] for p in sm_procs)

            # 检查之前监控的进程是否退出了
            for pid in list(monitored.keys()):
                if pid not in current_pids:
                    qid, arm, start_time = monitored[pid]
                    del monitored[pid]
                    # 进程退出了，处理输出
                    src = os.path.join(STAGE_DIR, f"runs-s5-sm-{qid}-synth.json")
                    if os.path.exists(src):
                        pending = get_next_pending_run(qid, arm)
                        if pending:
                            name = pending.get("name", "")
                            parts = name.rsplit("_r", 1)
                            if len(parts) == 2:
                                round_num = int(parts[1])
                                elapsed = time.time() - start_time
                                log(f"[detect] {qid} {arm} process {pid} exited after {elapsed:.0f}s, processing {name}")
                                process_run(qid, arm, round_num, src)
                        else:
                            log(f"[skip] {qid} {arm} no pending run in cc-state.json")
                    else:
                        log(f"[skip] {qid} {arm} no synth output file")

            # 监控新出现的进程
            for pid, qid, arm in sm_procs:
                if pid not in monitored:
                    monitored[pid] = (qid, arm, time.time())
                    log(f"[monitor] started tracking {qid} {arm} pid={pid}")

        except Exception as e:
            log(f"[error] {e}")

        time.sleep(15)

if __name__ == "__main__":
    main()
