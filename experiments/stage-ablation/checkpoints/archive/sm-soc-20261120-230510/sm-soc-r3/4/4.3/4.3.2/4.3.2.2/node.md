# N229: 阈值效应系数 γ 的校准方法：γ 可通过观察 Q 在 Q_min 附近微小变化时成交概率的跳跃幅度来估计；若 Q 从 Q_min*1.1 降至 Q_min*0.

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N74

## Claim

阈值效应系数 γ 的校准方法：γ 可通过观察 Q 在 Q_min 附近微小变化时成交概率的跳跃幅度来估计；若 Q 从 Q_min*1.1 降至 Q_min*0.9 导致成交概率下降 50%，则 γ ≈ 2.5；该系数通常大于 1，反映了非线性区间的陡峭程度，具体值需依赖平台日志回归验证。

## Corrected Claim

阈值效应系数 γ 的校准通常需通过观察 Q 在 Q_min 附近变化时成交概率的跳跃幅度来估计，具体数值需依赖平台日志回归验证，不同场景下 γ 值可能不同。

## Evidence

[质询]该陈述包含具体的经验性数值推导（γ≈2.5）和工程实践建议（依赖平台日志回归），属于经验事实而非第一性原理可推导的数学或物理定律。在缺乏外部来源支持的情况下，无法验证该特定数值校准方法的准确性和通用性。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

search threshold effect coefficient gamma transaction probability drop below minimum exposure
