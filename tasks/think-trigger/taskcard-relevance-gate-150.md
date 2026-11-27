# origin: ai
# 任务卡: 相关性门禁 (relevance gate) 最小实验 — Q9 150 档 gated vs baseline
# 立项依据: mech-scan 解读 (2026-11-27 20:5x, decomposition) — 主杠杆=相关性门禁, 病根=漂移 (other 率 150 档 34%→300 档 41%)
# 假设: 生成 prompt 加"节点必须直接服务于 Q9 部署目标"约束 → 150 档漂移率 (other) 从 34% 显著下降, 机制率 (mech) 不降
# 设计: 单变量 = 逐层展开 prompt (P1H_INDEX) + gap 补全 prompt (P15B_GAP_FILL) 尾部追加相关性门禁段; 预算 150 × 2 reps; 对照 = 已有 baseline 150-r1/r2/r3 (不重跑)
# 注 (2026-11-27 21:3x 修正): 初版注入点 P1_DECOMPOSE 是死路径 (SM 主循环不调 decompose())。真实路径: L1 骨架=P1_L1_SKELETON (只出 3-7 顶层维度, 不加门禁), 逐层展开=_decompose_layer→P1H_INDEX (L544, 函数内 import, patch s5_pipeline.P1H_INDEX 生效), gap 补全=gap_check→P15B_GAP_FILL (顶部 from-import, patch s5_pipeline.P15B_GAP_FILL 生效)
# 验收: ① 2 个 gated run json 落盘 (节点数 ~150) ② 漂移率 (脚本算 other 占比) < baseline 均值 34% ③ 1 commit
# 边界: 不改 s5_pipeline.py/prompts.py/s5_state_machine.py 本体 (monkeypatch 注入); 不碰 baseline 数据; 评分 (mech 重扫) 后置由 Lead 做

## 执行步骤 (纯执行, 按序)

### S1: 写 wrapper (monkeypatch 注入, 不改本体)
新建 `experiments/stage-ablation/run_q9_gated.py`:
```python
#!/usr/bin/env python3
"""Q9 相关性门禁臂: monkeypatch 逐层展开/gap 补全 prompt 加节点相关性约束, 不改本体.
入口: __main__ 内联块 (无 main()), 故 patch 后用 runpy 执行原文件.
注入点 (2026-11-27 21:3x 修正, P1_DECOMPOSE 是死路径):
  - P1H_INDEX: _decompose_layer 函数内 import (运行时读 s5_pipeline 模块属性) → 逐层展开 L2/L3/L4 节点 (大头)
  - P15B_GAP_FILL: gap_check 用 → gap 补全节点
  - P1_L1_SKELETON (L1 骨架, 只出 3-7 顶层维度) 不加门禁
"""
import sys, os, runpy
sys.path.insert(0, '/Users/a1-6/Desktop/workspace/pfb-thinkmech/modules/D-decomp-state-machine/scripts')
import s5_pipeline

GATE = (
    "\n\n【节点相关性门禁（硬性约束）】每个子节点必须直接服务于本题的部署目标："
    "Qwen3.8-27B 在 4×V100-SXM2-32GB (TP=4, NVFP4/W4A16) 上的推理性能与显存。"
    "只允许以下三类节点：① 硬件参数及其对推理的影响（显存/带宽/L2/量化位宽/指令集）；"
    "② 推理计算或访存的逐步分解（KV cache/attention/TP 切分/decode 流水线）；"
    "③ 量化指标（tok/s/延迟/显存占用/吞吐的数值估计）。"
    "禁止与本题部署无关的子问题（其他硬件平台的性能、通用软件框架内部机制、"
    "任务队列/调度系统、与本部署无关的成本或工具链话题）。"
    "违反门禁的节点视为无效，宁可不生成。"
)

s5_pipeline.P1H_INDEX = s5_pipeline.P1H_INDEX + GATE
s5_pipeline.P15B_GAP_FILL = s5_pipeline.P15B_GAP_FILL + GATE
assert "相关性门禁" in s5_pipeline.P1H_INDEX and "相关性门禁" in s5_pipeline.P15B_GAP_FILL, "GATE INJECT FAILED"

os.chdir('/Users/a1-6/Desktop/workspace/pfb-thinkmech/experiments/stage-ablation')
sys.argv = ['s5_state_machine.py'] + sys.argv[1:]  # 透传 --question-file/--qid/--max-nodes/--max-depth
runpy.run_path('/Users/a1-6/Desktop/workspace/pfb-thinkmech/experiments/stage-ablation/s5_state_machine.py', run_name='__main__')
```
验证注入生效 (1 条命令, 不跑 run):
`cd /Users/a1-6/Desktop/workspace/pfb-thinkmech/experiments/stage-ablation && python3 -c "
import sys; sys.path.insert(0,'/Users/a1-6/Desktop/workspace/pfb-thinkmech/modules/D-decomp-state-machine/scripts')
import s5_pipeline; s5_pipeline.P1H_INDEX += 'GATE'; s5_pipeline.P15B_GAP_FILL += 'GATE'
print('GATE OK' if 'GATE' in s5_pipeline.P1H_INDEX and 'GATE' in s5_pipeline.P15B_GAP_FILL else 'GATE MISSING')"
`
应输出 `GATE OK`。注意: `_decompose_layer` 在 s5_state_machine.py L544 用函数内 `from s5_pipeline import P1H_INDEX` (运行时读模块属性), `gap_check` 在 s5_pipeline.py 内读模块全局 P15B_GAP_FILL——两者 patch `s5_pipeline` 模块属性均生效。

### S2: 跑 2 reps (~9.5min/run, 前台阻塞)
runner 把 run json 写到 cwd 的 `runs-s5-sm-{qid}.json` (baseline 队列同款机制), 每 rep 跑完 cp 到 OUT:
```bash
cd /Users/a1-6/Desktop/workspace/pfb-thinkmech/experiments/stage-ablation
OUT=/Users/a1-6/Desktop/workspace/pfb-thinkmech/modules/B-pipeline-ablation/data/q9-budget-scan-gated
mkdir -p "$OUT"
echo "=== q9-gated queue started $(date '+%F %T') ===" > /tmp/q9-gated-queue.log
for rep in 1 2; do
  ts=$(date '+%Y%m%d-%H%M%S')
  t0=$(date +%s)
  SM_CKPT_DIR="$OUT/checkpoints" python3 run_q9_gated.py \
    --question-file /Users/a1-6/Desktop/workspace/pfb-thinkmech/experiments/stage-ablation/questions/Q9-agi-pure.txt \
    --qid q9-agi-gated --max-nodes 150 --max-depth 10 > "$OUT/q9-gated-r${rep}-${ts}.stdout" 2>&1
  rc=$?
  t1=$(date +%s)
  if [ -f runs-s5-sm-q9-agi-gated.json ]; then
    cp runs-s5-sm-q9-agi-gated.json "$OUT/q9-gated-r${rep}-${ts}.json"
    nn=$(python3 -c "import json;print(json.load(open('$OUT/q9-gated-r${rep}-${ts}.json'))['n_nodes'])" 2>/dev/null || echo "?")
    echo "rep=$rep rc=$rc wall_s=$((t1-t0)) n_nodes=$nn out=q9-gated-r${rep}-${ts}.json" | tee -a /tmp/q9-gated-queue.log
  else
    echo "rep=$rep rc=$rc wall_s=$((t1-t0)) out=MISSING" | tee -a /tmp/q9-gated-queue.log
  fi
done
echo "=== q9-gated queue DONE $(date '+%F %T') ===" | tee -a /tmp/q9-gated-queue.log
```
(每 rep 结束检查 rc=0; 两 rep 都 rc=0 才进 S3。)

### S3: 验证 + 落盘
- 确认 $OUT 下有 2 个 run json (q9-agi-gated-*.json), 各节点数 ~150 (读 json 的 nodes 长度)
- 漂移率初测 (粗判, 精确 mech 重扫由 Lead 后置): 对每个 gated run 的 nodes, 统计 claim 含以下无关关键词的比例: `Celery|队列|M1 Max|Apple|JSON schema|schema 开销|Docker|Kubernetes|CI/CD|GitHub Action` — 与 baseline 150 档对照 (baseline 漂移率 34%, 来自 mech-scan)
- git add 新文件 (run_q9_gated.py + 2 个 run json + stdout), commit: `feat(q9): 相关性门禁臂 150×2 (monkeypatch P1_DECOMPOSE)`

### S4: 汇报 (1 行)
`gated 2 runs: 节点数 X/Y, 粗漂移率 A%/B% (baseline 34%), json 路径, commit hash`

## 失败处理
- GATE MISSING → 检查 s5_pipeline 是否 from-import (若是, 还需 patch s5_pipeline.P1_DECOMPOSE, 已含在 wrapper)
- run json 节点数 <100 → 门禁过严, 如实汇报不重跑
- LLM 端点 8787 不可用 → 汇报阻塞, 不重试
