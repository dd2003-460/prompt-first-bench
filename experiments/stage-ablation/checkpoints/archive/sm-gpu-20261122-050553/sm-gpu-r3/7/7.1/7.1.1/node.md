# N299: 工作点A（标准 FP8 权重 + BF16 KV, 32K ctx）：显存占用 = 27GB (Weights) + 16GB (KV) = 43GB > 32

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N102

## Claim

工作点A（标准 FP8 权重 + BF16 KV, 32K ctx）：显存占用 = 27GB (Weights) + 16GB (KV) = 43GB > 32GB，方案不可行；若强制运行需启用 PagedAttention 并依赖 CPU Swap，导致吞吐下降 > 80%，仅作为兼容性验证而非生产方案。

## Corrected Claim

工作点A（标准 FP8 权重 + BF16 KV, 32K ctx）：显存占用预计超过 32GB（具体数值取决于模型参数量，估算约为 43GB），方案在单卡 32GB 显存下不可行；若强制运行需启用 PagedAttention 并依赖 CPU Swap，将导致显著吞吐下降，仅作为兼容性验证而非生产方案。

## Evidence

[质询]显存占用数值（27GB+16GB=43GB）及性能下降幅度（>80%）属于特定模型规模下的经验估算，缺乏具体模型参数量、KV Cache 计算公式及硬件基准测试数据支持，存在数值量级不准确或过度简化的风险。 | source=knowledge，逻辑自洽（43GB>32GB 导致不可行，启用 Swap 导致性能下降符合常识），但具体数值为经验估算，无来源直接支持，依据经验事实排除条款降级。
