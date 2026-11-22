# N345: 在 batch_size>8 的高并发场景下，T_compute 随 batch_size 线性增长，但 T_comm 仅随 batch_size 线性增长（每

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N111

## Claim

在 batch_size>8 的高并发场景下，T_compute 随 batch_size 线性增长，但 T_comm 仅随 batch_size 线性增长（每层通信量与 batch_size 成正比），η_comm 保持恒定或略有下降，实际吞吐损失约为 10-20% (而非 5-10%)，需修正高并发场景下的 η_comm 估计

## Corrected Claim

在 batch_size>8 的高并发场景下，T_compute 和 T_comm 均随 batch_size 线性增长，导致 η_comm 保持恒定或略有下降，实际吞吐损失需根据具体硬件和网络环境评估，通常高于低并发场景（如5-10%），建议通过实测修正 η_comm 估计。

## Evidence

[质询]该陈述包含具体的经验数值（吞吐损失10-20%、η_comm变化趋势），属于经验事实而非第一性原理可严格推导的数学/物理定律。虽然通信量随batch_size线性增长是逻辑自洽的，但具体的性能损失百分比高度依赖于硬件架构、网络带宽、计算密度等具体环境参数，无法仅凭逻辑推导得出唯一确定的数值范围。 | 经验事实，逻辑自洽但缺来源支持（source=knowledge，但具体数值缺乏通用性保证，且无外部来源验证特定场景下的10-20%损失范围）
