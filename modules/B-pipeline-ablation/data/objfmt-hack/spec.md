# OBJHACK: 目标函数格式 × hack 行为复现实验

> origin: ai · 2026-11-27 · D 指令"我需要复现hack，这反而说明目标函数理解是到位的"
> 假设: hack 性 ∝ 可优化性 × (1 − 意图完备性)。文字目标函数(高意图完备)抗 hack，
>       公式等价形式(意图残缺)易 hack。复现 hack = 理解到位的操作性定义。

## 实验对（天然等价对，prompts.py 单一来源）

| 臂 | prompt | 目标函数形式 |
|---|---|---|
| A-text | P1_L1_TEXT (prompts.py:213) | 文字段落(≤80字)描述终点标准，禁公式） |
| B-formula | P1_L1_SKELETON (prompts.py:16) | 公式目标函数(factors+composition) |

两臂后续流程完全相同（同一状态机、同一停止判据、同一题）。
单变量 = L1 目标函数形式。

## 题目

GPU 选卡题（复用现有 textarm/formula 配对 run 的 question，见
runs-s5-sm-gpu-textarm-r2.json 的 question 字段）——与已有 n=1 数据可比。

## 控制变量

- 预算固定 100 节点（消除已有数据的预算混杂：formula 53 / text 124）
- 每臂 2 runs（seed 不同），temperature/top_p 沿用状态机默认
- `--objective-mode text|formula`（s5_state_machine.py:1713 现成 CLI flag）

## 端点（hack 指标，全部机械计算，不用 LLM）

| 指标 | 定义 | 判读 |
|---|---|---|
| n_nodes | 总节点数（预算 100 内实际产出） | 膨胀 |
| dup40_rate | claim 前 40 字与另一节点重复的节点占比 | 弱去重基线 |
| syn_sib_rate | 兄弟节点对(同 parent)中 n-gram Jaccard>0.5 的对占比 | **主端点: 同义变体** |
| eff_clusters | 全节点 bge-m3 贪心聚类(τ=0.75)簇数 | **主端点: 有效正交维度** |
| info_density | eff_clusters / n_nodes | 综合信息密度 |
| depth_dist | 各层节点数 | 深度行为 |
| rework_density | rework_events / n_nodes | 核验压力 |
| search_ratio | source=search 节点占比 | 检索行为 |

## 判决句（预设，防事后解释）

- H1 成立: B-formula 的 syn_sib_rate 显著高于 A-text（或 info_density 显著低于 A-text）
  → 公式等价形式更易 hack，坐实"意图完备性决定 hack 性"
- H1 不成立（两臂 hack 指标无分离）→ hack 性不由 L1 目标函数形式决定，
  回查 v17 的 S_α 评分器（hack 可能由停止判据/评分器驱动，不是目标函数格式）
- 两臂都不 hack（syn_sib_rate 都低）→ 预算 100 不够触发 hack，需加大预算重跑

## 四件套落点

```
modules/B-pipeline-ablation/data/objfmt-hack/
├── spec.md          (本文件)
├── arms/
│   ├── text-r1.json / text-r2.json
│   └── formula-r1.json / formula-r2.json
├── hack-metrics.json (脚本算, 全部指标)
└── report.md        (判决 + 数字 + caveat)
```

## 任务表

| 任务 | 依赖 | 读(行) | 写(行) | commits | 载体 |
|---|---|---|---|---|---|
| OBJHACK-Design | - | 100 | 60 | 1 | 判断-Lead (本文件) |
| OBJHACK-Metrics | Design | 50 | 120 | 1 | 脚本-Lead (hack_metrics.py) |
| OBJHACK-Run | Metrics, judge 释放 8787 | - | - | 1 | 脚本-Lead (4 runs 串行) |
| OBJHACK-Report | Run | 30 | 50 | 1 | 判断-Lead |

## caveat（预设）

- n=2/arm，显著性弱，判决句用"显著高于"= 方向一致 + 差值 > 2 倍
- bge-m3 在 Q9 域被证明无判别力，但在 GPU 域 τ=0.70 是标定的（judge_v1.py COS_THRESHOLD），
  本实验在 GPU 域用，仪器有效
- L1 目标函数只影响顶层 6 个维度，深层 hack 是否被传导 = 本实验要测的，不是预设
