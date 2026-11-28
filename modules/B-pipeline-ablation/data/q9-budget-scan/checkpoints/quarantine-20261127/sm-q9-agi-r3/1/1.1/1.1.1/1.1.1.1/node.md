# N122: 工作点A（最大吞吐）：max_num_seqs=8, chunked_prefill=False时，单卡激活内存峰值为 8 * (hidden_size * 2

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N37

## Claim

工作点A（最大吞吐）：max_num_seqs=8, chunked_prefill=False时，单卡激活内存峰值为 8 * (hidden_size * 2 * layers / 4) + 1.0GB ≈ 1.4GB，剩余KV显存 11.125-1.4=9.725GB

## Corrected Claim

工作点A（最大吞吐）：在假设单序列激活内存约为 50MB 且基础开销为 1.0GB 的经验估算下，max_num_seqs=8 时单卡激活内存峰值约为 1.4GB，若总可用显存为 11.125GB，则剩余 KV 显存约为 9.725GB。

## Evidence

[质询]公式中 `hidden_size * 2 * layers / 4` 的量纲和系数缺乏明确定义，且未包含 Attention Head 维度或 Batch Size 对激活内存的具体影响逻辑，属于经验估算而非严格推导；此外，11.125GB 的总显存假设未在陈述中明确界定（通常 A10 为 24GB，L4 为 24GB，T4 为 16GB，11.125GB 可能是特定配置下的可用显存，但未说明）。 | source=knowledge，逻辑上算术运算正确（8 * 0.05 + 1.0 = 1.4, 11.125 - 1.4 = 9.725），但激活内存计算公式过于简化，未体现 Transformer 激活内存的标准计算方式（通常涉及 seq_len, batch_size, hidden_dim 等），作为精确事实节点存在经验估算的不确定性，故降级。
