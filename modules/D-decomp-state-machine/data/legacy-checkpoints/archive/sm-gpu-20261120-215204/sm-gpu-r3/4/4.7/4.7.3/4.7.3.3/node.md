# N329: Qwen3-27B 64 层模型在 TP=2 下的总同步数据量估算：(Attention 同步量 + FFN 同步量) * 64 层，基于 N135 和 N13

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N116

## Claim

Qwen3-27B 64 层模型在 TP=2 下的总同步数据量估算：(Attention 同步量 + FFN 同步量) * 64 层，基于 N135 和 N136 的数值，总同步量约为 (0.54 + 2.1) * 64 ≈ 169 GB，这与 N116 中假设的 32GB 存在巨大差异，需重新核验同步策略是否仅同步部分层或使用了更高效的通信原语（如 AllGather+ReduceScatter 代替 AllReduce 减半带宽需求）。

## Corrected Claim

基于假设的每层同步量（Attention 0.54GB + FFN 2.1GB），Qwen3-27B 64层模型在 TP=2 下的理论总同步量估算约为 169 GB。此数值与 32GB 的假设存在显著差异，提示需重新评估同步策略（如是否仅同步部分层或采用更高效的通信原语），但具体数值需结合实际通信原语和硬件实现进一步核验。

## Evidence

[质询]该陈述依赖于未提供的内部节点（N135, N136, N116）的具体数值，且将复杂的分布式通信优化（如AllGather+ReduceScatter）简化为简单的带宽减半，忽略了实际通信模式（如Ring AllReduce）和硬件拓扑对同步量的非线性影响，存在口径混淆风险。 | 无可用外部证据；逻辑上算术运算 (0.54 + 2.1) * 64 ≈ 169 成立，但作为经验事实（具体模型通信量估算），缺乏来源直接支持，且依赖未验证的前置节点数值，故降级。

## Search Query

Qwen3-27B tensor parallelism communication volume allreduce per layer
