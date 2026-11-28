# N158: 单卡 12.6 GB 可用 KV cache 空间的计算依据是：V100 16GB 总显存减去模型权重（TP=4 分片后约 3.5GB/卡）和激活值/临时缓冲区

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N55

## Claim

单卡 12.6 GB 可用 KV cache 空间的计算依据是：V100 16GB 总显存减去模型权重（TP=4 分片后约 3.5GB/卡）和激活值/临时缓冲区（约 0.4GB/卡），剩余约 12.1GB，向上取整或预留缓冲后定为 12.6GB。

## Corrected Claim

单卡 12.6 GB 可用 KV cache 空间是基于 V100 16GB 总显存，扣除模型权重（TP=4 分片后约 3.5GB/卡）和激活值/临时缓冲区（约 0.4GB/卡）后的估算值，具体数值取决于实际部署配置。

## Evidence

[质询]陈述中关于模型权重（3.5GB/卡）和激活值（0.4GB/卡）的具体数值缺乏来源支持，且‘向上取整或预留缓冲后定为 12.6GB’的解释在逻辑上略显牵强（通常预留缓冲会减少可用空间而非增加，或者12.1GB本身就是估算值，直接取整为12.6GB缺乏明确的工程惯例依据），属于经验事实且细节不可验证。 | 来源[1][2]确认了V100 16GB的总显存规格，支持了计算的基础前提，但未提供模型权重和激活值的具体占用数据，无法直接验证12.6GB这一具体数值的推导过程，属于经验事实缺来源支持。

## Search Query

V100 16GB memory breakdown model weights activation buffer vLLM

## Retrieval Sources

- {'url': 'https://www.techpowerup.com/gpu-specs/tesla-v100-pcie-16-gb.c2957&rut=8f7dcb4a99d4acfbfbdd4190693bc45e77267868e44738a15b54432b533433dc', 'type': 'ddg', 'title': 'NVIDIA Tesla V100 PCIe 16 GB Specs | TechPowerUp GPU Database'}
- {'url': 'https://www.techpowerup.com/gpu-specs/tesla-v100-sxm2-16-gb.c3018&rut=a47f18b50a50a5e62aee9efe0e38c9243d1182563870374f50e477082b8c012f', 'type': 'ddg', 'title': 'NVIDIA Tesla V100 SXM2 16 GB Specs - TechPowerUp'}
