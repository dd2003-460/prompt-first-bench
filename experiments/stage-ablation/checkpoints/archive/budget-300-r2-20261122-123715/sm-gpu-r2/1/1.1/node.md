# N5: 候选硬件集合包含 NVIDIA GeForce RTX 4090 (24GB GDDR6X, ~$1600-2000), RTX 3090 (24GB GDDR

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N1

## Claim

候选硬件集合包含 NVIDIA GeForce RTX 4090 (24GB GDDR6X, ~$1600-2000), RTX 3090 (24GB GDDR6, ~$800-1200), RTX 4060 Ti 16GB (~$450), AMD Radeon RX 7900 XTX (24GB GDDR6, ~$900-1100), Intel Arc A770 16GB (~$350-450) 等消费级 GPU，需验证其显存容量是否满足 32K 上下文推理需求。

## Corrected Claim

候选硬件集合包含 NVIDIA GeForce RTX 4090 (24GB GDDR6X), RTX 3090 (24GB GDDR6), RTX 4060 Ti 16GB, AMD Radeon RX 7900 XTX (24GB GDDR6), Intel Arc A770 16GB 等消费级 GPU，需验证其显存容量是否满足 32K 上下文推理需求。

## Evidence

[质询]该陈述包含多个具体硬件型号及其对应的市场价格区间（如RTX 4090 ~$1600-2000, RTX 3090 ~$800-1200等），这些属于随时间波动且依赖具体市场渠道的经验事实，无法从第一性原理推导，且参考来源仅覆盖RTX 4090的显存规格，未提供价格或其他型号信息，存在来源覆盖不足的风险。 | 来源[1]直接支持RTX 4090拥有24GB GDDR6X显存，逻辑上24GB显存对于32K上下文推理（取决于模型大小和精度）是合理的量级，但其他型号的价格和规格缺乏来源支持，且价格属于经验事实，故降级。

## Search Query

NVIDIA RTX 4090 24GB price 2024

## Retrieval Sources

- {'url': 'https://www.nvidia.com/en-us/geforce/graphics-cards/40-series/rtx-4090/&rut=707b2673e1a87858a2ce7540842e866d4a9fe1b1dbf63d8ece6f498597558888', 'type': 'ddg', 'title': 'GeForce RTX 4090 Graphics Cards for Gaming | NVIDIA'}
