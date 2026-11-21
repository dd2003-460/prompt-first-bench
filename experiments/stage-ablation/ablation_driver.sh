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
# ── 实验形状由 spec 驱动（ABLATION_SPEC 指向 spec/<name>.json，run_ablation.sh 设置）──
# 无 ABLATION_SPEC 时回退 T53b 默认值（向后兼容：62 run 已验证的行为不变）。
# spec 是唯一改实验形状的地方（qid/臂/轮数/seed/judge/cc-state 路径），本脚本不硬编码。
ABLATION_SPEC="${ABLATION_SPEC:-}"
_SPEC_ENV="${TMPDIR:-/tmp}/ablation-spec-env.$$"
python3 - "$ABLATION_SPEC" > "$_SPEC_ENV" <<'PY'
import json, os, sys
p = sys.argv[1]
if p and os.path.exists(p):
    s = json.load(open(p))
    qids = '|'.join(s['qids']); arms = '|'.join(s['arms'].keys())
    pat = '^(' + qids + ')_(' + arms + ')_r(\\d{2})$'
    print("STAGE=" + s.get('stage', 'experiments/stage-ablation'))
    print("CC_STATE=" + s['cc_state'])
    print("SM_SEED=" + str(s.get('seed', 42)))
    print("RUN_PATTERN=" + pat)
    print("JUDGE_MODULE=" + s.get('judge_module', 'judge_v2_depth'))
    print("JUDGE_FUNC=" + s.get('judge_func', 'score_run'))
    out = s.get('output', {})
    print("RUNS_DIR=" + out.get('runs_dir', 'modules/B-pipeline-ablation/data/t53b/runs'))
    print("NOTES_DIR=" + out.get('notes_dir', 'modules/B-pipeline-ablation/data/t53b/notes'))
    print("RESULTS_FILE=" + out.get('results', 'modules/B-pipeline-ablation/data/t53b/results.json'))
    print("LOG_DIR=" + s.get('log_dir', '/tmp/ablation'))
    for a, fl in s['arms'].items():
        print("ARMFLAGS_%s=%s" % (a, fl))
else:
    print("STAGE=experiments/stage-ablation")
    print("CC_STATE=tasks/T53-bus/cc-state.json")
    print("SM_SEED=42")
    print("RUN_PATTERN=^(gpu|nat|soc)_(formula|text)_r(\\d{2})$")
    print("JUDGE_MODULE=judge_v2_depth")
    print("JUDGE_FUNC=score_run")
    print("RUNS_DIR=modules/B-pipeline-ablation/data/t53b/runs")
    print("NOTES_DIR=modules/B-pipeline-ablation/data/t53b/notes")
    print("RESULTS_FILE=modules/B-pipeline-ablation/data/t53b/results.json")
    print("LOG_DIR=/tmp/t53b")
    print("ARMFLAGS_formula=--obj-mode=formula")
    print("ARMFLAGS_text=--obj-mode=text")
PY
source "$_SPEC_ENV"
rm -f "$_SPEC_ENV"
mkdir -p "$LOG_DIR" "$STAGE/ablation-runs" "$STAGE/ablation-notes"

# ── 取下一个 pending run（支持 T53B_RUN 环境变量指定，batch 并行模式用）──
if [[ -n "${T53B_RUN:-}" ]]; then
  RUN="$T53B_RUN"
  echo "[driver] using T53B_RUN=$RUN (from batch)"
else
  RUN="$(RUN_PATTERN="$RUN_PATTERN" CC_STATE="$CC_STATE" python3 -c "
import json, re, os
s=json.load(open(os.environ['CC_STATE']))
pat=re.compile(os.environ['RUN_PATTERN'])
for wu in s['work_units']:
    if not wu.get('done') and pat.match(wu.get('name','')):
        print(wu['name']); break
")"
fi
if [[ -z "$RUN" ]]; then echo "NO PENDING RUNS"; exit 0; fi
QID="${RUN%%_*}"; rest="${RUN#*_}"; ARM="${rest%%_*}"; ROUND="${rest#*_r}"
echo "=== driver: $RUN (started $(date '+%F %T')) ==="

# ── 清场（该 qid 的 ckpt + 主输出 + synth 输出 + FATAL ckpt）──
# 2026-11-19 诊断员修复：SM 树形 ckpt 是目录（checkpoints/sm-{qid}-r{rnd}/，
# 2026-11-18 起新格式），旧清场只 rm *.json 漏掉目录 → 新 run 从残留树 resume
# 出污染状态（watchdog 03:05 日志已见 [clean] 只删 json 的口径）。
# 2026-11-20 D指令：checkpoint 是原始数据，不许删 → 改为 mv 归档。
# mv 后原路径清空，防 resume 污染的效果与 rm 等价，但逐节点数据保留。
# 已完成的 23 个 run 的节点级数据在改前已被 rm 销毁（不可恢复），
# 本改动只保护之后的 run。
ARCHIVE="$STAGE/checkpoints/archive/sm-${QID}-$(date +%Y%m%d-%H%M%S)"
mkdir -p "$ARCHIVE"
for f in "$STAGE/checkpoints/sm-${QID}-r"* \
         "$STAGE/runs-s5-sm-${QID}.json" \
         "$STAGE/runs-s5-sm-${QID}-synth.json" \
         "$STAGE/runs-s5-sm-${QID}-checkpoint.json"; do
  [ -e "$f" ] && mv "$f" "$ARCHIVE/"
done
echo "[clean] archived ${QID} ckpt/output files → $ARCHIVE"

# ── 跑 SM（seed 由 spec 固定，前台，无超时——由 CC 会话看门）──
# 臂参数由 spec 的 arms.<arm> 指定（ARMFLAGS_<arm>），T53b 默认 --obj-mode=<arm>。
# 注意：不用 `if ! cmd; then RC=$?`——`!` 反转退出码，then 里 $? 是 0 不是 cmd 的 rc（T2 测试暴露）
T0=$(date +%s)
RC=0
# 臂 flag 由 spec 的 arms.<arm> 给出（字符串，如 --obj-mode=formula）；zsh 间接展开
_AF_NAME="ARMFLAGS_$ARM"; _AF="${(P)_AF_NAME}"
SM_SEED="$SM_SEED" python3 -u "$STAGE/s5_state_machine.py" "$QID" ${=_AF} --synth \
      > "$LOG_DIR/${RUN}.sm.log" 2>&1 || RC=$?
# 2026-11-19 诊断员修复：SM FATAL 时落盘 runs-s5-sm-${QID}-checkpoint.json（E12），
# 旧逻辑直接 exit 丢弃进度 → batch 标记 done 跳过，整轮白干（19:42-20:47 连丢 7 个
# gpu_text run，其中 r04 已跑 36min 树 38 节点、r09 跑 42min 树 30 节点）。
# 现在 FATAL 且有 ckpt 时 resume 续跑（SM_SEED 固定 42，resume 跳过 L1 重拆，
# 已核验节点不重验，seed 只影响新节点采样 → 与一次性跑完的分布一致）。
RESUME_TRIES=0
while [ $RC -ne 0 ] && [ $RESUME_TRIES -lt 3 ]; do
  # 2026-11-19 诊断员修复：必须传绝对路径。SM 入口 os.chdir 到 stage-ablation/，
  # 相对路径 "experiments/stage-ablation/..." 会被解析成双重前缀 →
  # FileNotFoundError（r04/r05 各浪费 3 次 resume 全失败，见 /tmp/t53b/gpu_text_r04.sm.log）。
  CKPT="$(pwd)/$STAGE/runs-s5-sm-${QID}-checkpoint.json"
  if [[ ! -f "$CKPT" ]] || (( $(stat -f %m "$CKPT") < T0 )); then
    break
  fi
  RESUME_TRIES=$((RESUME_TRIES+1))
  echo "[resume] SM FATAL 后从 ckpt 续跑 (第${RESUME_TRIES}/3次): $CKPT"
  T0=$(date +%s)
  _AF_NAME="ARMFLAGS_$ARM"; _AF="${(P)_AF_NAME}"
  SM_SEED="$SM_SEED" python3 -u "$STAGE/s5_state_machine.py" "$QID" ${=_AF} --synth \
        --resume "$CKPT" >> "$LOG_DIR/${RUN}.sm.log" 2>&1 || RC=$?
done
if [ $RC -ne 0 ]; then
  echo "[FAIL] SM exited rc=$RC after $(( $(date +%s) - T0 ))s (resume $RESUME_TRIES 次) — 不记账，保持 done=false，查 $LOG_DIR/${RUN}.sm.log"
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
# STAGE/CC/JUDGE 由 spec 驱动（env 传入），T53b 默认值向后兼容。
RUN="$RUN" QID="$QID" ARM="$ARM" ROUND="$ROUND" SRC="$SRC" T0="$T0" \
STAGE="$STAGE" CC_STATE="$CC_STATE" JUDGE_MODULE="$JUDGE_MODULE" JUDGE_FUNC="$JUDGE_FUNC" \
RUNS_DIR="$RUNS_DIR" NOTES_DIR="$NOTES_DIR" RESULTS_FILE="$RESULTS_FILE" ARCHIVE="$ARCHIVE" \
python3 - <<'PYEOF'
import json, os, shutil, sys, glob, importlib.util
from datetime import datetime
STAGE = os.environ["STAGE"]
ROOT = os.getcwd()  # driver 在 repo root 执行（L13 cd）
RUNS_DIR = os.path.join(ROOT, os.environ["RUNS_DIR"])
RUN, QID, ARM = os.environ["RUN"], os.environ["QID"], os.environ["ARM"]
ROUND = int(os.environ["ROUND"])
SRC = os.environ["SRC"]
ABL = RUNS_DIR
NOTES = os.path.join(ROOT, os.environ["NOTES_DIR"])
RESULTS = os.path.join(ROOT, os.environ["RESULTS_FILE"])
CC = os.environ["CC_STATE"]

dst = f"{ABL}/{RUN}.json"
shutil.copy2(SRC, dst)

with open(dst) as f:
    run_data = json.load(f)
answer = run_data.get("answer", "")
coverage = run_data.get("coverage")
depth = run_data.get("depth_score")

# judge（spec 指定模块，T53b 默认 judge_v2_depth.score_run，与任务书一致）
sys.path.insert(0, STAGE)
_jmod_name = os.environ.get("JUDGE_MODULE", "judge_v2_depth")
_jfunc_name = os.environ.get("JUDGE_FUNC", "score_run")
_jspec = importlib.util.spec_from_file_location(_jmod_name, os.path.join(os.getcwd(), STAGE, f"{_jmod_name}.py"))
_jmod = importlib.util.module_from_spec(_jspec)
_jspec.loader.exec_module(_jmod)
score_run = getattr(_jmod, _jfunc_name)
judge_result = None
if answer:
    judge_result = score_run(QID, answer)
    with open(f"{ABL}/{RUN}_judge.json", "w") as f:
        json.dump(judge_result, f, ensure_ascii=False, indent=2)
    depth = judge_result.get("overall", depth)
    print(f"[judge] overall={depth}")

# 节点统计 + L1 判据（2026-11-20 修复：改读 non-synth 终盘文件——
# 它带完整 nodes 数组；旧逻辑 glob checkpoints/sm-{qid}-r*.json 只匹配
# 旧单文件格式，11-18 起 SM 写树形目录（sm-{qid}-r{rnd}/），glob 永远
# 匹配不到 → l1_uncertainty 恒 False，r7 复现判据被系统性判 FAIL。
# mtime ≥ T0 防读到上一 run 的旧文件（同 qid 串行覆盖）。）
n_nodes = run_data.get("n_nodes", 0)
n_verified = n_degraded = 0
l1_unc = False
nodes_src = f"{STAGE}/runs-s5-sm-{QID}.json"
T0 = int(os.environ.get("T0", "0"))
if os.path.exists(nodes_src) and int(os.stat(nodes_src).st_mtime) >= T0:
    nd = json.load(open(nodes_src))
    nodes = nd.get("nodes", [])
    n_nodes = len(nodes) or n_nodes
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
    # nodes 写进存档（自包含，事后复核 l1 判据不用依赖现场文件）
    run_data["nodes"] = nodes
    with open(dst, "w") as f:
        json.dump(run_data, f, ensure_ascii=False, indent=2)
else:
    print(f"[WARN] nodes 源文件缺失/过旧: {nodes_src} — l1 判据不可信", flush=True)

# results（去重后追加，防双记账）
results = json.load(open(RESULTS)) if os.path.exists(RESULTS) else {"runs": []}
results["runs"] = [r for r in results["runs"]
                   if not (r.get("qid") == QID and r.get("arm") == ARM and r.get("round") == ROUND)]
results["runs"].append({
    "qid": QID, "arm": ARM, "round": ROUND,
    "coverage": coverage, "depth": depth,
    "n_nodes": n_nodes, "n_verified": n_verified, "n_degraded": n_degraded,
    "l1_uncertainty": l1_unc,
    "run_file": f"{RUNS_DIR}/{RUN}.json",
    "judge_file": f"{RUNS_DIR}/{RUN}_judge.json" if judge_result else None,
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
