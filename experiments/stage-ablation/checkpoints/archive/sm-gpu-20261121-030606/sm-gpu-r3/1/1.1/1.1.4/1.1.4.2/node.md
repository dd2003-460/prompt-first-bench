# N198: INT8 精度下 Qwen3-27B 总显存下限修正为 33.5 GB（计算式：27.0 GB 权重 + 3.98 GB KV + 2.5 GB 激活），N83

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N83, N84, N85

## Claim

INT8 精度下 Qwen3-27B 总显存下限修正为 33.5 GB（计算式：27.0 GB 权重 + 3.98 GB KV + 2.5 GB 激活），N83 声称的 34.2 GB 因 KV Cache 高估而偏高，但结论不变：24GB 显存不可行（33.5 > 24）

## Corrected Claim

INT8 精度下 Qwen3-27B 总显存下限修正为 33.5 GB（计算式：27.0 GB 权重 + 3.98 GB KV + 2.5 GB 激活），N83 声称的 34.2 GB 因 KV Cache 高估而偏高，但结论不变：24GB 显存不可行（33.5 > 24）

## Evidence

先验知识/题面给定，逻辑校验通过：INT8权重27GB + KV Cache约4GB + 激活2.5GB ≈ 33.5GB，量级合理且结论（>24GB）稳健
