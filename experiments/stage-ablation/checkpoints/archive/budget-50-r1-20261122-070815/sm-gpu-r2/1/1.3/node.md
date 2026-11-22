# N8: 硬件显存硬性下限 = 模型权重显存 + KV Cache 显存 + 激活值/碎片开销 (通常为 10-20%)，此总和必须小于等于 GPU 显存容量，否则不可行

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

硬件显存硬性下限 = 模型权重显存 + KV Cache 显存 + 激活值/碎片开销 (通常为 10-20%)，此总和必须小于等于 GPU 显存容量，否则不可行

## Corrected Claim

硬件显存硬性下限 = 模型权重显存 + KV Cache 显存 + 激活值/碎片开销 (通常为 10-20%)，此总和必须小于等于 GPU 显存容量，否则不可行

## Evidence

先验知识/题面给定，逻辑校验通过
