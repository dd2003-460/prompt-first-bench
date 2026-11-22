# N221: RTX 5090 单卡 BF16 不可行工作点：显存需求 55GB (权重 54GB + KV 1GB) 超出 32GB 物理显存，缺口 23GB，导致单卡 B

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N105

## Claim

RTX 5090 单卡 BF16 不可行工作点：显存需求 55GB (权重 54GB + KV 1GB) 超出 32GB 物理显存，缺口 23GB，导致单卡 BF16 吞吐量为 0 tokens/s，必须触发量化或 Offload 机制。

## Corrected Claim

RTX 5090 单卡 BF16 不可行工作点：显存需求 55GB (权重 54GB + KV 1GB) 超出 32GB 物理显存，缺口 23GB，导致单卡 BF16 吞吐量为 0 tokens/s，必须触发量化或 Offload 机制。

## Evidence

先验知识/题面给定，逻辑校验通过：54GB+1GB=55GB > 32GB，缺口23GB，单卡无法容纳导致吞吐为0，逻辑自洽且符合硬件物理限制。
