# N523: 在 Batch_Size=4 且每序列 64K tokens 的配置下，4 张 V100 集群总 KV Cache 占用 = 2GB × 4 (TP=4 分布式

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N186

## Claim

在 Batch_Size=4 且每序列 64K tokens 的配置下，4 张 V100 集群总 KV Cache 占用 = 2GB × 4 (TP=4 分布式) = 8GB，每卡占用 2GB，剩余显存 14GB 用于激活值和中间计算

## Corrected Claim

在 Batch_Size=4 且每序列 64K tokens 的配置下，假设单卡 KV Cache 占用为 2GB，则 4 张 V100 集群总 KV Cache 占用为 8GB，每卡剩余显存约 14GB 用于激活值和中间计算（具体数值需根据实际模型结构确认）。

## Evidence

[质询]KV Cache 的具体数值（2GB/卡）高度依赖于具体的模型架构（如层数、隐藏维度、注意力头数）和精度（FP16/BF16/INT8），仅凭 Batch_Size=4 和 64K tokens 无法唯一确定该数值，存在参数缺失导致的数值不确定性。 | source=knowledge，逻辑自洽（总显存16GB - KV Cache 2GB = 剩余14GB，算术正确），但具体KV Cache占用量为经验参数，缺乏特定模型上下文支持，故降级。
