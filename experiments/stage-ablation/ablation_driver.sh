#!/bin/zsh
# T53b 消融实验 driver（CC 侧，不改受保护设施文件）。
# 从 cc-state.json 取第一个 done=false 的 run，清场 → 跑 SM → 落盘/judge/记账。
# 用法: zsh ablation_driver.sh（前台跑一个 run，由 CC 会话看门）
# 设计（对应 cc-to-lead.md 发现 1-6 的 CC 边界内处置）：
#   - 不用 ablation_run_one.py 的 subprocess（1800s 超时不够，r01 实际 ~30min）
#   - 每 run 前清场（选项 B 脚本化：rm 该 qid 的 ckpt + 主/synth 输出）
#   - 记账只信本 run 刚生成的文件（mtime 校验），不读 watcher 的账
#   - L1 不确定性判据：claim 全文含关键词（原判据读不存在的 scope 字段，
#     必然 false；见 cc-to-lead 发现 3，等 Lead 正式裁决）
set -euo pipefail
setopt NULL_GLOB  # zsh: glob 匹配不到时展开为空，避免 rm -f 因 nomatch 失败（T1 测试暴露）
cd /Users/a1-6/Desktop/workspace/pfb
STAGE=experiments/stage-ablation
CC_STATE=tasks/T53-bus/cc-state.json
LOG_DIR=/tmp/t53b
mkdir -p "$LOG_DIR" "$STAGE/ablation-runs" "$STAGE/ablation-notes"

# ── 取下一个 pending run ──
RUN="$(python3 -c "
import json, re
s=json.load(open('$CC_STATE'))
pat=re.compile(r'^(gpu|nat|soc)_(formula|text)_r(\d{2})$')
for wu in s['work_units']:
    if not wu.get('done') and pat.match(wu.get('name','')):
        print(wu['name']); break
")"
if [[ -z "$RUN" ]]; then echo "NO PENDING RUNS"; exit 0; fi
QID="${RUN%%_*}"; rest="${RUN#*_}"; ARM="${rest%%_*}"; ROUND="${rest#*_r}"
echo "=== driver: $RUN (started $(date '+%F %T')) ==="

# ── 清场（该 qid 的 ckpt + 主输出 + synth 输出 + FATAL ckpt）──
rm -f "$STAGE/checkpoints/sm-${QID}-r"*.json \
      "$STAGE/runs-s5-sm-${QID}.json" \
      "$STAGE/runs-s5-sm-${QID}-synth.json" \
      "$STAGE/runs-s5-sm-${QID}-checkpoint.json"
echo "[clean] removed ${QID} ckpt/output files"

# ── 跑 SM（SM_SEED=42 固定，前台，无超时——由 CC 会话看门）──
# 注意：不用 `if ! cmd; then RC=$?`——`!` 反转退出码，then 里 $? 是 0 不是 cmd 的 rc（T2 测试暴露）
T0=$(date +%s)
RC=0
SM_SEED=42 python3 "$STAGE/s5_state_machine.py" "$QID" --obj-mode="$ARM" --synth \
      > "$LOG_DIR/${RUN}.sm.log" 2>&1 || RC=$?
if [ $RC -ne 0 ]; then
  echo "[FAIL] SM exited rc=$RC after $(( $(date +%s) - T0 ))s — 不记账，保持 done=false，查 $LOG_DIR/${RUN}.sm.log"
  exit $RC
fi
echo "[sm] done in $(( $(date +%s) - T0 ))s"

# ── 校验输出新鲜（防 FATAL 后旧文件记账，cc-to-lead 发现 5/7）──
# synth 文件必须存在且 mtime ≥ T0（本 run 启动时间）；SM 早退/FATAL 时
# 文件不存在或仍是旧 mtime → 拒记账。
SRC="$STAGE/runs-s5-sm-${QID}-synth.json"
if [[ ! -f "$SRC" ]]; then
  echo "[FAIL] no synth output — FATAL 路径？查 $LOG_DIR/${RUN}.sm.log 尾部"; tail -20 "$LOG_DIR/${RUN}.sm.log"
  exit 1
fi
MT=$(stat -f %m "$SRC")
if (( MT < T0 )); then
  echo "[FAIL] synth output stale (mtime $MT < start $T0) — SM 未产出新数据，拒记账"; tail -20 "$LOG_DIR/${RUN}.sm.log"
  exit 1
fi

# ── copy + judge + 记账 + note + state（一次性 python，只信本 run 文件）──
RUN="$RUN" QID="$QID" ARM="$ARM" ROUND="$ROUND" SRC="$SRC" python3 - <<'PYEOF'
import json, os, shutil, sys, glob
from datetime import datetime
STAGE = "experiments/stage-ablation"
RUN, QID, ARM = os.environ["RUN"], os.environ["QID"], os.environ["ARM"]
ROUND = int(os.environ["ROUND"])
SRC = os.environ["SRC"]
ABL = f"{STAGE}/ablation-runs"
NOTES = f"{STAGE}/ablation-notes"
RESULTS = f"{STAGE}/ablation-results.json"
CC = "tasks/T53-bus/cc-state.json"

dst = f"{ABL}/{RUN}.json"
shutil.copy2(SRC, dst)

with open(dst) as f:
    run_data = json.load(f)
answer = run_data.get("answer", "")
coverage = run_data.get("coverage")
depth = run_data.get("depth_score")

# judge（judge_v2_depth.score_run，与任务书一致）
sys.path.insert(0, STAGE)
from judge_v2_depth import score_run
judge_result = None
if answer:
    judge_result = score_run(QID, answer)
    with open(f"{ABL}/{RUN}_judge.json", "w") as f:
        json.dump(judge_result, f, ensure_ascii=False, indent=2)
    depth = judge_result.get("overall", depth)
    print(f"[judge] overall={depth}")

# 节点统计 + L1 判据（读本 run 的 checkpoint 最新文件；claim 全文含关键词）
n_nodes = run_data.get("n_nodes", 0)
n_verified = n_degraded = 0
l1_unc = False
ckpts = sorted(glob.glob(f"{STAGE}/checkpoints/sm-{QID}-r*.json"))
if ckpts:
    ck = json.load(open(ckpts[-1]))
    nodes = ck.get("nodes", [])
    n_verified = sum(1 for n in nodes if n.get("status") == "verified")
    n_degraded = sum(1 for n in nodes if n.get("status") == "degraded")
    for n in nodes:
        if n.get("level") != "L1":
            continue
        claim = (n.get("claim") or "").lower()
        if any(k in claim for k in ["不确定性", "随机", "uncertainty", "stochastic"]):
            if any(k in claim for k in ["横切", "作用于", "cross-cut", "affect"]):
                l1_unc = True
                break

# results（去重后追加，防双记账）
results = json.load(open(RESULTS)) if os.path.exists(RESULTS) else {"runs": []}
results["runs"] = [r for r in results["runs"]
                   if not (r.get("qid") == QID and r.get("arm") == ARM and r.get("round") == ROUND)]
results["runs"].append({
    "qid": QID, "arm": ARM, "round": ROUND,
    "coverage": coverage, "depth": depth,
    "n_nodes": n_nodes, "n_verified": n_verified, "n_degraded": n_degraded,
    "l1_uncertainty": l1_unc,
    "run_file": f"ablation-runs/{RUN}.json",
    "judge_file": f"ablation-runs/{RUN}_judge.json" if judge_result else None,
    "timestamp": datetime.now().astimezone().isoformat(),
})
with open(RESULTS, "w") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

# note
note = f"""# {QID} {ARM} r{ROUND:02d}

- 时间: {datetime.now().astimezone().isoformat()}
- 节点数: {n_nodes} (verified: {n_verified}, degraded: {n_degraded})
- coverage: {coverage}
- depth: {depth}
- L1 不确定性维度: {'是' if l1_unc else '否'}
- 观察: （CC 填写）
"""
with open(f"{NOTES}/{RUN}.md", "w") as f:
    f.write(note)

# cc-state
s = json.load(open(CC))
for wu in s["work_units"]:
    if wu.get("name") == RUN:
        wu["done"] = True
        break
with open(CC, "w") as f:
    json.dump(s, f, ensure_ascii=False, indent=2)
print(f"[book] {RUN} cov={coverage} depth={depth} nodes={n_nodes} l1_unc={l1_unc}")
PYEOF
echo "=== driver: $RUN DONE ==="
