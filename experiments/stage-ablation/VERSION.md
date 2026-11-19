# PFB 版本线（权威映射）

> origin: ai · 2026-11-19 · D指令「务必保证完整版本连续性命名」
> 本文件是版本号的唯一权威来源。exploration-history.md §5 有完整编号纪律。

## 版本线（v1→v19，连续不断档）

| 版本 | 代码文件 | 诞生日期 | 核心变更 | 实验数据目录 |
|------|---------|---------|---------|-------------|
| v1-v2 | s5_pipeline.py | 11-06~07 | P1 分解 + P2 搜索 + P3 核验 + P4 综合（初始版） | runs-s5-smoke/ |
| v3 | s5_pipeline.py | 11-08 | P1 迭代分解（3 层树 8→25 节点）+ JSON retry | runs-s5-gpu-v3/ |
| v4 | s5_pipeline.py | 11-08 | P1.5 两遍 gap check + 来源标签强制 | runs-s5-gpu-v4/ |
| v5-v9 | s5_pipeline.py | 11-08 | 规则堆叠期（P1 rule 6/7/8/9, P4 rule 5/6） | runs-s5-gpu-v5~v9/ |
| v10 | s5_pipeline.py | 11-08 | exclusion 修复（排除性结果不终止树） | runs-s5-gpu-v10/ |
| v11 | s5_pipeline.py | 11-08 | P4 rule 6 口径分离 | runs-s5-gpu-v11/ |
| v12 | s5_pipeline.py | 11-08 | 规则堆叠后期 | runs-s5-gpu-v12/ |
| v13 | s5_pipeline.py | 11-08 | 50-rep 稳定性 runner + early-stop 修复 | runs-s5-gpu-v13/（34 reps） |
| v14 | s5_pipeline.py | 11-09 | nat 101 reps 量产 + rule 9b 变形 | runs-s5-nat-v14/（101 reps） |
| v15 | s5_pipeline.py | 11-09 | 阶段分离原则（P1 纯分解, P4 分析层） | runs-s5-nat-v15-smoke/ |
| v16 | s5_pipeline.py | 11-09 | P1e 状态机臂（多轮回退 + S_α 边际停止） | runs-s5-v16-smoke/ |
| v16.3 | s5_pipeline.py | 11-09 | R2 软约束 + R4 防御硬帽 | runs-s5-v16.3-smoke/ |
| v17 | s5_pipeline.py | 11-09 | 层级 INDEX 分解（逐层展开, 无限预算） | runs-s5-v17-hier-smoke/ |
| **v18** | **s5_state_machine.py** | **11-11** | **T53 目标函数驱动状态机**（{IDLE,DECOMPOSE,VERIFY,REWORK,STOP}） | **ablation-runs/gpu_{prompt}_r{NN}** + **checkpoints/sm-{qid}-r{N}/** |
| **v19** | **langgraph-pfb-full.py** | **11-19** | **langgraph 控制流**（sqlite checkpoint + 5 轮循环） | **runs-langgraph-pfb-{qid}.json** |

## 基座（prompt 版本，作为子标签，不变版本号）

| 基座 | 说明 | 使用版本 |
|------|------|---------|
| formula | 数学公式目标函数（S_α = Σ[n·ln kₙ + α·kₙ·ln n]） | v18, v19 |
| text | 纯文本描述（无公式） | v18 |
| minimal | 最小 prompt（只有目标 + 约束） | v18 |
| method | 方法论描述（含质询方法） | v18 |
| method_challenge | 方法论 + 质询挑战 | v18 |

## 实验数据目录映射（旧名→新名）

**新命名规范：`v{N}/{qid}-{prompt}-rep{M}/`**

### v18（T53 状态机）

| 旧路径 | 新路径 | 说明 |
|--------|--------|------|
| ablation-runs/gpu_formula_r01.json | v18/gpu-formula-rep01/ | formula 臂 rep1 |
| ablation-runs/gpu_formula_r02.json | v18/gpu-formula-rep02/ | formula 臂 rep2 |
| ... | ... | ... |
| ablation-runs/gpu_formula_r09.json | v18/gpu-formula-rep09/ | formula 臂 rep9 |
| ablation-runs/gpu_text_r01.json | v18/gpu-text-rep01/ | text 臂 rep1 |
| checkpoints/sm-gpu-r1/ | v18/gpu-formula-rep01/checkpoints/ | rep1 checkpoint |
| checkpoints/sm-gpu-r2/ | v18/gpu-formula-rep02/checkpoints/ | rep2 checkpoint |
| checkpoints/sm-gpu-r3/ | v18/gpu-formula-rep03/checkpoints/ | rep3 checkpoint |
| checkpoints/sm-nat-r5/ | v18/nat-formula-rep05/checkpoints/ | nat rep5 checkpoint |

### v19（langgraph）

| 旧路径 | 新路径 | 说明 |
|--------|--------|------|
| runs-langgraph-pfb-nat.json | v19/nat-formula-rep01/ | nat rep1（559 节点, verified_rate 70.5%） |
| （gpu 在跑） | v19/gpu-formula-rep01/ | gpu rep1（预计 20-40 分钟出） |

### gptr（独立框架，不归 v 版本线）

| 旧路径 | 新路径 | 说明 |
|--------|--------|------|
| runs-gptr-official/ | gptr-official/{qid}-rep{M}/ | GPT-5.2 直接回答 |
| runs-gptr-pfb/ | gptr-pfb/{qid}-rep{M}/ | gpt_researcher + pfb prompt |

### 历史版本（v3-v17，保留原名）

v3-v17 的目录名已经是 `runs-s5-{qid}-v{N}` 格式，符合新规范的精神（版本号在目录名里），**不改名**。

## 轮次命名规则

- **rep**（重复实验）：同一配置独立跑 N 次，编号 rep01, rep02, ...
- **round**（管线内部轮次）：状态机内部循环轮次，编号 r1, r2, ...（在 checkpoint 目录里）
- **工程迭代轮**：代码修改批次，编号 r1-r6（在 sm-modification-log.md 里）

**rep 和 round 的区别**：rep 是独立实验（不同随机种子/不同时刻），round 是同一次实验内部的循环轮次。

## 版本连续性检查

- v1→v17：s5_pipeline.py 内部迭代，版本号连续 ✓
- v17→v18：s5_state_machine.py 新文件，版本号延续 ✓
- v18→v19：langgraph-pfb-full.py 新文件，版本号延续 ✓
- **无断档** ✓
