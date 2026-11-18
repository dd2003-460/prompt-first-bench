#!/usr/bin/env python3
"""T53b 消融实验：单 run 执行器。

CC 每个 run 调一次：
  python3 ablation_run_one.py {qid} {arm} {round}

流程：
1. 跑 s5_state_machine.py（SM_SEED=42）
2. 复制输出 JSON 到 ablation-runs/
3. 跑 judge_v2_depth.py
4. 提取 coverage/depth
5. 检查 L1 不确定性维度
6. 更新 ablation-results.json
7. 写过程 note
8. 更新 cc-state.json
"""
import json, os, shutil, subprocess, sys, time
from datetime import datetime

STAGE_DIR = os.path.dirname(os.path.abspath(__file__))
PFB_ROOT = os.path.dirname(os.path.dirname(STAGE_DIR))
ABLATION_RUNS = os.path.join(STAGE_DIR, "ablation-runs")
ABLATION_NOTES = os.path.join(STAGE_DIR, "ablation-notes")
RESULTS_FILE = os.path.join(STAGE_DIR, "ablation-results.json")
CC_STATE_FILE = os.path.join(PFB_ROOT, "tasks", "T53-bus", "cc-state.json")

def run_cmd(cmd, cwd=None, timeout=1800):
    """跑命令，返回 (returncode, stdout, stderr)。"""
    print(f"[run] {cmd}", flush=True)
    t0 = time.time()
    r = subprocess.run(cmd, shell=True, cwd=cwd or PFB_ROOT,
                       capture_output=True, text=True, timeout=timeout)
    elapsed = time.time() - t0
    print(f"[run] exit={r.returncode} elapsed={elapsed:.0f}s", flush=True)
    if r.stdout:
        print(r.stdout[-2000:], flush=True)  # 最后 2000 字符
    if r.stderr:
        print(f"[stderr] {r.stderr[-1000:]}", flush=True)
    return r.returncode, r.stdout, r.stderr

def extract_l1_uncertainty(run_json_path):
    """检查 L1 节点是否有独立'不确定性/随机性'维度。"""
    with open(run_json_path) as f:
        d = json.load(f)
    nodes = d.get("nodes", [])
    l1_nodes = [n for n in nodes if n.get("level") == "L1"]
    for n in l1_nodes:
        claim = n.get("claim", "")
        scope = n.get("scope", "") or n.get("description", "")
        # 判据：claim 以"不确定性/随机/uncertainty/stochastic"开头
        if any(claim.lower().startswith(kw) for kw in ["不确定性", "随机", "uncertainty", "stochastic"]):
            # 且 scope 提到"横切/作用于其他维度"
            if any(kw in scope for kw in ["横切", "作用于", "cross-cut", "affect"]):
                return True
    return False

def main():
    if len(sys.argv) < 4:
        print("Usage: python3 ablation_run_one.py {qid} {arm} {round}")
        sys.exit(1)

    qid, arm, round_num = sys.argv[1], sys.argv[2], int(sys.argv[3])
    run_name = f"{qid}_{arm}_r{round_num:02d}"
    print(f"=== {run_name} ===", flush=True)

    # 1. 跑 s5_state_machine.py
    env = os.environ.copy()
    env["SM_SEED"] = "42"
    cmd = f"SM_SEED=42 python3 experiments/stage-ablation/s5_state_machine.py {qid} --obj-mode={arm} --synth"
    rc, out, err = run_cmd(cmd, cwd=PFB_ROOT, timeout=1800)
    if rc != 0:
        print(f"ERROR: s5_state_machine.py failed (rc={rc})", flush=True)
        sys.exit(rc)

    # 2. 复制输出 JSON 到 ablation-runs/
    src_json = os.path.join(STAGE_DIR, f"runs-s5-sm-{qid}-synth.json")
    dst_json = os.path.join(ABLATION_RUNS, f"{run_name}.json")
    if os.path.exists(src_json):
        shutil.copy2(src_json, dst_json)
        print(f"[copy] {src_json} → {dst_json}", flush=True)
    else:
        # 可能没有 --synth，用主输出
        src_json = os.path.join(STAGE_DIR, f"runs-s5-sm-{qid}.json")
        if os.path.exists(src_json):
            shutil.copy2(src_json, dst_json)
            print(f"[copy] {src_json} → {dst_json} (no synth)", flush=True)
        else:
            print(f"ERROR: no output JSON found", flush=True)
            sys.exit(1)

    # 3. 跑 judge（从 synth JSON 提取 answer，调 judge_v2_depth.py 的 score_run）
    judge_result = None
    run_data = {}
    try:
        with open(dst_json) as f:
            run_data = json.load(f)
        answer = run_data.get("answer", "")
        if answer:
            # 直接调 judge_v2_depth.py 的 score_run
            sys.path.insert(0, STAGE_DIR)
            from judge_v2_depth import score_run
            judge_result = score_run(qid, answer)
            judge_path = os.path.join(ABLATION_RUNS, f"{run_name}_judge.json")
            with open(judge_path, "w") as f:
                json.dump(judge_result, f, ensure_ascii=False, indent=2)
            print(f"[judge] overall={judge_result.get('overall', 'ERR')}", flush=True)
    except Exception as e:
        print(f"[judge] ERROR: {e}", flush=True)

    # 4. 提取 coverage/depth
    coverage = run_data.get("coverage")
    depth = run_data.get("depth_score")
    if judge_result:
        # judge 的 overall 作为 depth 的补充
        depth = judge_result.get("overall", depth)

    # 5. 检查 L1 不确定性维度
    l1_unc = extract_l1_uncertainty(dst_json)

    # 6. 节点统计
    nodes = run_data.get("nodes", [])
    n_nodes = len(nodes)
    n_verified = sum(1 for n in nodes if n.get("status") == "verified")
    n_degraded = sum(1 for n in nodes if n.get("status") == "degraded")

    # 7. 更新 ablation-results.json
    if os.path.exists(RESULTS_FILE):
        with open(RESULTS_FILE) as f:
            results = json.load(f)
    else:
        results = {"runs": []}

    results["runs"].append({
        "qid": qid,
        "arm": arm,
        "round": round_num,
        "coverage": coverage,
        "depth": depth,
        "n_nodes": n_nodes,
        "n_verified": n_verified,
        "n_degraded": n_degraded,
        "l1_uncertainty": l1_unc,
        "run_file": f"ablation-runs/{run_name}.json",
        "judge_file": f"ablation-runs/{run_name}_judge.json" if judge_result else None,
        "timestamp": datetime.now().astimezone().isoformat(),
    })
    with open(RESULTS_FILE, "w") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"[results] updated {RESULTS_FILE}", flush=True)

    # 8. 写过程 note
    note_path = os.path.join(ABLATION_NOTES, f"{run_name}.md")
    note = f"""# {qid} {arm} r{round_num:02d}

- 时间: {datetime.now().astimezone().isoformat()}
- 节点数: {n_nodes} (verified: {n_verified}, degraded: {n_degraded})
- coverage: {coverage}
- depth: {depth}
- L1 不确定性维度: {'是' if l1_unc else '否'}
- 观察: （CC 填写，200 字以内）
"""
    with open(note_path, "w") as f:
        f.write(note)
    print(f"[note] {note_path}", flush=True)

    # 9. 更新 cc-state.json
    if os.path.exists(CC_STATE_FILE):
        with open(CC_STATE_FILE) as f:
            cc_state = json.load(f)
        for wu in cc_state.get("work_units", []):
            if wu.get("name") == run_name:
                wu["done"] = True
                break
        with open(CC_STATE_FILE, "w") as f:
            json.dump(cc_state, f, ensure_ascii=False, indent=2)
        print(f"[state] updated {CC_STATE_FILE}", flush=True)

    print(f"=== {run_name} DONE ===", flush=True)

if __name__ == "__main__":
    main()
