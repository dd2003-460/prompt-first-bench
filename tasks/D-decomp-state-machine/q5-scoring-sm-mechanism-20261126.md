# D 五问调研（评分机制 + 状态机机制）

> origin: ai · 2026-11-26 · D 连问五题：①逐点overall 是什么 ②为什么 prompt 堆叠比状态机强，状态机有 rework 吗 ③评分具体怎么算，对不上就没分还是分解不完整/冗余才没分 ④深层节点（微架构效率）有出现和计算吗 ⑤有限制节点或其他没控制的变量吗

## 分解树

1. **评分机制**（sub A）— ①③：judge prompt 原文 + 聚合代码（point_scores→overall 怎么算）+ rubric 罚项（冗余/不完整罚不罚）+ r03 伪影成因
2. **状态机机制与数据**（sub B）— ②④⑤：v18 各阶段 prompt vs S5 六阶段注入对比、runs 节点层级分布（L4 深节点实际内容）、REWORK 实证、未控变量清单
3. **Q2 方向判断**（Lead 保留）— "prompt 堆叠更强"是否成立：当前数据口径混杂（题集/判分/8787 漂移），AC4 未启动，结论方向可信但比较不干净

## 任务表

| # | 任务 | 执行 | 验收 |
|---|------|------|------|
| Q1 | 评分机制落盘报告 | sub A ✅ 2026-11-26 | `experiments/stage-ablation/scoring-mechanism-20261126.md`：逐点 overall=要点连续深度分等权平均（judge_v2_depth.py:465）；冗余罚在目标函数层 β·red·n_nodes（β=3 默认，--beta 0 关）；judge 给部分分非二值；r03=judge 退化 100ptN 全 0.33 + 修复前 .get(...,0) 兜底伪影（a8ae30551 已修，数据未重判）；canonical n=90 六维加权 vs v18 逐点 overall 公式/题集均不同 |
| Q2 | 状态机机制+深节点+未控变量落盘报告 | sub B | commit + L4 节点计数/样例 + 未控变量清单 |

## 边界

- 只读代码/数据 + 写报告 + commit，不跑实验（8787 被 t-repair1 占用）
- 大 json 用 python 解析提字段，不全文读
- 不 stash/checkout/切分支
