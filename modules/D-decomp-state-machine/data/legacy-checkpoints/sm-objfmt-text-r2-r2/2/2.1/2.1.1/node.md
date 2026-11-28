# N50: NVIDIA RTX 4090 (24GB GDDR6X) 的显存带宽为 1008 GB/s，新品市场价约为 $1,600-$1,800，二手市场价约为 $1,

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N12

## Claim

NVIDIA RTX 4090 (24GB GDDR6X) 的显存带宽为 1008 GB/s，新品市场价约为 $1,600-$1,800，二手市场价约为 $1,200-$1,400，显存容量 24GB 足以容纳 Qwen3-27B 的 INT8 量化权重 (27.8GB) 和 KV Cache (13.7GB BF16) 的组合，但 BF16 权重 (55.6GB) 超出单卡容量。

## Corrected Claim

NVIDIA RTX 4090 (24GB GDDR6X) 的显存带宽为 1008 GB/s，新品市场价约为 $1,600-$1,800，二手市场价约为 $1,200-$1,400。其 24GB 显存不足以同时容纳 Qwen3-27B 的 INT8 量化权重 (27.8GB) 和 KV Cache (13.7GB BF16) 的组合（总计约 41.5GB），也无法容纳 BF16 权重 (55.6GB)。

## Evidence

[质询]显存容量计算存在严重逻辑错误：INT8 量化权重 (27.8GB) 加上 KV Cache (13.7GB) 总计约 41.5GB，远超 RTX 4090 的 24GB 显存容量，因此‘足以容纳’这一结论在物理上不可能成立。 | 逻辑校验失败：27.8GB + 13.7GB = 41.5GB > 24GB，陈述内部数据自相矛盾，违背基本算术和硬件限制。

## Search Query

NVIDIA RTX 4090 memory bandwidth price 2024
