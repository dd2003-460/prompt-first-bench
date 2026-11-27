#!/bin/bash
# origin: ai · 2026-11-25 · fixB-r3 补跑（原 r3 rc=1 502 崩, 产物=r2 副本已隔离 _quarantine/）
# 背景: T-REPAIR-1 读数协议主判据=rep 级方向一致性 3/3, fixB 缺 r3 → 只 2/3, 读数歪。
# 安全: ①门控等所有 vLLM 消费者(catchup 36173/armC' 69029/eps-judge 71865)退出再跑, 防 502 风暴
#       ②只在 rc=0 且产物新鲜(mtime>t0)时才 cp, 修原 run_arm "rc=1 仍拷旧文件" 的 bug
#       ③SM 必须在 H0 无 marker 态才 apply fix-b.diff, 跑完 restore 回 H0
# 落盘: logs/fixb-r3-rerun-<ts>.log
set -uo pipefail
PFB=/Users/a1-6/Desktop/workspace/pfb
SA=$PFB/experiments/stage-ablation
BJ=$PFB/modules/B-pipeline-ablation
OUT=$BJ/data/t-repair1
QFILE=$PFB/bench/questions/Q6-network-arch.txt
SEED=42
BUDGET=300
# vLLM 消费者 PID(门控): catchup / armC' / eps-judge
GATE_PIDS=(36173 69029 71865)
TS=$(date '+%Y%m%d-%H%M%S')
LOG=$SA/logs/fixb-r3-rerun-$TS.log
log(){ echo "[$(date '+%H:%M:%S')] $*" | tee -a "$LOG"; }

log "FIXB-R3-RERUN-START gate_pids=${GATE_PIDS[*]}"

# ---- 门控: 等所有 vLLM 消费者退出(它们各自还在等 catchup, 退出=链上无 LLM 负载) ----
while :; do
  alive=0
  for p in "${GATE_PIDS[@]}"; do kill -0 "$p" 2>/dev/null && alive=1; done
  [ "$alive" -eq 0 ] && break
  log "gate: 仍有 vLLM 消费者存活(${GATE_PIDS[*]}), 等 120s"
  sleep 120
done
log "gate: 所有 vLLM 消费者已退出"

# ---- vLLM 健康确认(200) ----
for i in 1 2 3 4 5; do
  code=$(curl -s -o /dev/null -w '%{http_code}' -m 8 http://127.0.0.1:8787/health 2>/dev/null)
  [ "$code" = "200" ] && { log "vLLM health=200 OK"; break; }
  log "vLLM health=$code (第 $i 次), 等 60s"
  sleep 60
done
code=$(curl -s -o /dev/null -w '%{http_code}' -m 8 http://127.0.0.1:8787/health 2>/dev/null)
[ "$code" != "200" ] && { log "FATAL: vLLM 不健康, 中止补跑(不硬跑, 避免再 502)"; exit 1; }

# ---- 前置: SM 必须在 H0 无 marker 态 ----
cd "$SA"
if grep -q 'Fix-A (T-REPAIR-1' s5_state_machine.py || grep -q 'Fix-B (T-REPAIR-1' s5_state_machine.py; then
  log "FATAL: SM 已含 Fix marker, 非 H0 基线态 — 中止(不污染析因)。先人工 checkout H0"; exit 1
fi
H0=$(git -C "$PFB" rev-parse HEAD); log "H0=$H0 (SM 未修改基线)"

# ---- apply Fix-B (只含 B, 复刻 4arm ARM4 终态) ----
git -C "$PFB" apply tasks/repair-loop-fix-b.diff || { log "FATAL: apply fix-b 失败, 中止"; exit 1; }
python3 -m py_compile s5_state_machine.py || { log "FATAL: fix-b 后 py_compile 失败, 回滚"; git -C "$PFB" apply -R tasks/repair-loop-fix-b.diff; exit 1; }
if ! grep -q 'Fix-B (T-REPAIR-1' s5_state_machine.py || grep -q 'Fix-A (T-REPAIR-1' s5_state_machine.py; then
  log "FATAL: apply 后 marker 状态异常(B 应有 A 应无), 回滚中止"; git -C "$PFB" apply -R tasks/repair-loop-fix-b.diff; exit 1
fi
log "Fix-B applied (marker OK: B 有 A 无)"

# ---- 跑单 rep r3 (独立 ckpt 防陈旧子树) ----
ckpt="$OUT/arms/fixB/checkpoints-rerun"
mkdir -p "$ckpt"
t0=$(date +%s)
SM_SEED=$SEED SM_CKPT_DIR="$ckpt" python3 -u s5_state_machine.py \
  --question-file "$QFILE" --qid q6 --max-nodes $BUDGET \
  > "$OUT/arms/fixB/fixB-r3-rerun.stdout" 2>&1
rc=$?
t1=$(date +%s); dur=$((t1 - t0))

# ---- 只在 rc=0 且产物新鲜时才 cp (修原 bug) ----
if [ $rc -ne 0 ]; then
  log "FATAL: s5_state_machine rc=$rc (非 0), 不拷产物(避免再造假副本)。SM 仍 restore。"
else
  # 产物新鲜度: mtime 必须晚于 t0(本次启动), 防拷到上一 rep 残留
  if [ -f runs-s5-sm-q6.json ] && [ "$(stat -f %m runs-s5-sm-q6.json)" -gt "$t0" ]; then
    ts2=$(date '+%Y%m%d-%H%M%S')
    dst="$OUT/arms/fixB/fixB-r3-${ts2}.json"
    cp runs-s5-sm-q6.json "$dst"
    log "fixB-r3 rerun rc=0 wall_s=$dur out=$(basename $dst)"
    # 提取 stats (复刻 run_arm PYEOF, 追加到 stats.json)
    python3 - "$dst" "fixB" 3 "$dur" "$OUT/t-repair1-stats.json" "$LOG" 2>/dev/null << 'PYEOF'
import sys, json, os
sys.path.insert(0, '/Users/a1-6/Desktop/workspace/pfb/modules/B-pipeline-ablation')
f, arm, rep, dur, out, logf = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), sys.argv[5], sys.argv[6]
d = json.load(open(f))
nodes = d.get("nodes", [])
rew = d.get("rework_events", [])
mode_dist = {}
for e in rew:
    m = e.get("mode", "unknown"); mode_dist[m] = mode_dist.get(m, 0) + 1
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
    log "FATAL: 产物不存在或不新鲜(mtime<=t0), 不 cp(防假副本)。SM 仍 restore。"
  fi
fi

# ---- 收尾: restore SM 回 H0 ----
git -C "$PFB" checkout $H0 -- experiments/stage-ablation/s5_state_machine.py
git -C "$PFB" add experiments/stage-ablation/s5_state_machine.py
git -C "$PFB" commit -m "fixB-r3 rerun: SM restore 回 H0(补跑收尾, 实验态清除)" --quiet
HR=$(git -C "$PFB" rev-parse HEAD); log "SM restored to H0, restore-commit=$HR"
log "FIXB-R3-RERUN-DONE rc=$rc log=$LOG"
