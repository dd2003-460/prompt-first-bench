#!/bin/bash
# origin: ai · 2026-11-25 · T-REPAIR-1 repair loop 4 臂析因实验执行器
# 设计: tasks/repair-loop-design-20261124.md + tasks/repair-loop-diff-prep-20261124.md
#   2×2 析因: Fix-A(directed 可达) × Fix-B(re-entry), Q6 budget=300, n=3/臂
#   预测: P-A(directed 修复率↑) / P-B(rework_count 行使到 2) / P-A+B(交互)
# 析因成立前提(设计文档 §4): baseline 臂必须跑未修改 SM, 故序列固定:
#   baseline(H0) → apply A(H_A) → apply B(H_AB) → apply -R A(H_B)
#   每步 commit 留痕, 任意臂可 git checkout 复现; 反向 apply 无残留已验证(md5 一致)。
# 时序: Gate 等 post-pilot 队列 PID 退出 + vLLM /v1/models 就绪(队列 STEP1 正 import SM)。
# 安全: 不改在跑的队列 .sh; 每臂独立 SM_CKPT_DIR(防陈旧子树); 同 SM_SEED=42(臂间可比)。
# 用法: setsid nohup bash t-repair1-4arm.sh <queue_pid> > /dev/null 2>&1 &
set -uo pipefail

PFB=/Users/a1-6/Desktop/workspace/pfb
SA=$PFB/experiments/stage-ablation
QFILE=$PFB/bench/questions/Q6-network-arch.txt
OUT=$PFB/modules/B-pipeline-ablation/data/t-repair1
LOG=$SA/logs/t-repair1-4arm-$(date +%Y%m%d-%H%M%S).log
mkdir -p "$OUT"
cd "$SA"

QUEUE_PID=${1:?用法: t-repair1-4arm.sh <queue_pid>}
SEED=42
BUDGET=300
REPS=3

log() { echo "[$(date '+%H:%M:%S')] $*" | tee -a "$LOG"; }

# ---- Gate 1: 等队列 PID 退出 ----
log "ARM-QUEUE-START waiting queue PID=$QUEUE_PID"
while kill -0 "$QUEUE_PID" 2>/dev/null; do sleep 120; done
log "queue PID=$QUEUE_PID exited"

# ---- Gate 2: vLLM 就绪 ----
for i in $(seq 1 30); do
  if curl -sf -m 5 http://127.0.0.1:8787/v1/models >/dev/null 2>&1; then
    log "vLLM /v1/models OK (try $i)"; break
  fi
  log "vLLM not ready (try $i/30)"; sleep 30
done

# ---- 记录 H0(回滚点, 当前 SM 未修改) ----
H0=$(git -C "$PFB" rev-parse HEAD)
log "H0=$H0 (SM 未修改基线)"
# 前置: SM 必须是原始版(Fix-A/B marker 都不在)
if grep -q 'Fix-A (T-REPAIR-1' s5_state_machine.py || grep -q 'Fix-B (T-REPAIR-1' s5_state_machine.py; then
  log "FATAL: SM 已含 Fix marker, 非基线态 — 中止(析因作废)。先 git checkout $H0 -- experiments/stage-ablation/s5_state_machine.py"; exit 1
fi

# ---- 跑一臂: 3 reps, 每 rep 独立 ckpt 目录 + 提取 rework 统计 + judge 评分 ----
run_arm() {
  local arm="$1"
  local ckpt="$OUT/arms/$arm/checkpoints"
  mkdir -p "$ckpt"
  for rep in $(seq 1 $REPS); do
    local ts=$(date '+%Y%m%d-%H%M%S')
    local t0=$(date +%s)
    SM_SEED=$SEED SM_CKPT_DIR="$ckpt" python3 -u s5_state_machine.py \
      --question-file "$QFILE" --qid q6 --max-nodes $BUDGET \
      > "$OUT/arms/$arm/${arm}-r${rep}.stdout" 2>&1
    local rc=$?
    local t1=$(date +%s); local dur=$((t1 - t0))
    if [ -f runs-s5-sm-q6.json ]; then
      local dst="$OUT/arms/$arm/${arm}-r${rep}-${ts}.json"
      cp runs-s5-sm-q6.json "$dst"
      log "arm=$arm rep=$rep rc=$rc wall_s=$dur out=$(basename $dst)"
      # 提取 rework 统计(析因核心: mode 分布 + attempt 分布 + 修复率) + judge 评分
      python3 - "$dst" "$arm" "$rep" "$dur" "$OUT/t-repair1-stats.json" "$LOG" 2>/dev/null << 'PYEOF'
import sys, json, os
sys.path.insert(0, '/Users/a1-6/Desktop/workspace/pfb/modules/B-pipeline-ablation')
f, arm, rep, dur, out, logf = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), sys.argv[5], sys.argv[6]
d = json.load(open(f))
nodes = d.get("nodes", [])
rew = d.get("rework_events", [])
mode_dist = {}
for e in rew:
    m = e.get("mode", "unknown"); mode_dist[m] = mode_dist.get(m, 0) + 1
# 修复率: rework 过的节点(rc>0)中终态 verified 的比例
rc_pos = [n for n in nodes if (n.get("rework_count") or 0) > 0]
rc_ver = [n for n in rc_pos if n.get("status") == "verified"]
rc_deg = [n for n in rc_pos if n.get("status") == "degraded"]
rec = {"arm": arm, "rep": rep, "wall_s": dur, "n_nodes": d.get("n_nodes"),
       "final_state": d.get("final_state"),
       "rework": {"n_events": len(rew), "mode_dist": mode_dist,
                  "n_rc_pos": len(rc_pos), "n_verified": len(rc_ver), "n_degraded": len(rc_deg),
                  "repair_rate": (round(len(rc_ver)/len(rc_pos), 4) if rc_pos else None)},
       "judge": {}}
try:
    from judge_v1 import judge_run
    rj = judge_run(f)
    rec["judge"] = {"total": rj["total_score"],
                    "depth": rj["layers"]["structure"]["depth_score"],
                    "cov": rj["layers"]["coverage"]["coverage"]}
except Exception as e:
    rec["judge"]["err"] = str(e)
scores = json.load(open(out)) if os.path.exists(out) else []
scores.append(rec)
json.dump(scores, open(out, "w"), ensure_ascii=False, indent=1)
rr = rec["rework"]["repair_rate"]
log2 = f"  [stat] arm={arm} r{rep} n_nodes={rec['n_nodes']} rework={rec['rework']['n_events']} mode={mode_dist} repair_rate={rr} judge={rec['judge'].get('total','NA')}"
with open(logf, "a") as _lf:
    _lf.write("[" + __import__("datetime").datetime.now().strftime("%H:%M:%S") + "] " + log2 + "\n")
print(log2)
PYEOF
    else
      log "arm=$arm rep=$rep rc=$rc wall_s=$dur out=MISSING"
    fi
  done
}

# ---- 4 臂序列(析因成立前提: baseline 跑未修改 SM) ----
log "ARM1 baseline START (SM=H0 未修改)"
run_arm baseline

log "ARM2 apply Fix-A"
git -C "$PFB" apply tasks/repair-loop-fix-a.diff || { log "FATAL: apply fix-a 失败, 中止"; exit 1; }
python3 -m py_compile s5_state_machine.py || { log "FATAL: fix-a 后 py_compile 失败, 回滚"; git -C "$PFB" apply -R tasks/repair-loop-fix-a.diff; exit 1; }
git -C "$PFB" add experiments/stage-ablation/s5_state_machine.py
git -C "$PFB" commit -m "T-REPAIR-1 arm A: apply Fix-A(directed 可达) — 4 臂析因 H_A" --quiet
HA=$(git -C "$PFB" rev-parse HEAD); log "H_A=$HA"
run_arm fixA

log "ARM3 apply Fix-B (A+B)"
git -C "$PFB" apply tasks/repair-loop-fix-b.diff || { log "FATAL: apply fix-b 失败, 中止"; exit 1; }
python3 -m py_compile s5_state_machine.py || { log "FATAL: fix-b 后 py_compile 失败"; git -C "$PFB" apply -R tasks/repair-loop-fix-b.diff; exit 1; }
git -C "$PFB" add experiments/stage-ablation/s5_state_machine.py
git -C "$PFB" commit -m "T-REPAIR-1 arm A+B: apply Fix-B(re-entry) atop A — 4 臂析因 H_AB" --quiet
HAB=$(git -C "$PFB" rev-parse HEAD); log "H_AB=$HAB"
run_arm fixAB

log "ARM4 apply -R Fix-A (回到只含 B)"
git -C "$PFB" apply -R tasks/repair-loop-fix-a.diff || { log "FATAL: reverse fix-a 失败, 中止"; exit 1; }
python3 -m py_compile s5_state_machine.py || { log "FATAL: reverse 后 py_compile 失败"; exit 1; }
# 反向后 Fix-B marker 应在, Fix-A marker 应不在
if ! grep -q 'Fix-B (T-REPAIR-1' s5_state_machine.py || grep -q 'Fix-A (T-REPAIR-1' s5_state_machine.py; then
  log "FATAL: 反向 apply 后 marker 状态异常(A 应无 B 应有), 中止"; exit 1
fi
git -C "$PFB" add experiments/stage-ablation/s5_state_machine.py
git -C "$PFB" commit -m "T-REPAIR-1 arm B: reverse Fix-A(只留 Fix-B) — 4 臂析因 H_B" --quiet
HB=$(git -C "$PFB" rev-parse HEAD); log "H_B=$HB"
run_arm fixB

# ---- 收尾: 恢复 SM 到基线 H0(不留修改态给后续实验; 做成 commit 保审计链线性+工作树干净) ----
git -C "$PFB" checkout $H0 -- experiments/stage-ablation/s5_state_machine.py
git -C "$PFB" add experiments/stage-ablation/s5_state_machine.py
git -C "$PFB" commit -m "T-REPAIR-1 restore: SM 回到基线 H0(4 臂析因收尾, 实验态清除; 审计链 H0→H_A→H_AB→H_B→restore)" --quiet
HR=$(git -C "$PFB" rev-parse HEAD); log "SM restored to H0 content, restore-commit=$HR (工作树干净)"
log "T-REPAIR-1 4-arm DONE log=$LOG stats=$OUT/t-repair1-stats.json"
