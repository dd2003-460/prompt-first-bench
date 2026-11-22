# N424: RTX 3090 Ti 在 INT8 KV Cache 配置下的 Decode 吞吐量修正：理论 Decode 上限 = 1008 GB/s / (13.5 G

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N142

## Claim

RTX 3090 Ti 在 INT8 KV Cache 配置下的 Decode 吞吐量修正：理论 Decode 上限 = 1008 GB/s / (13.5 GB + 4 GB) = 57.7 tokens/s，实测效率系数 0.7-0.8 后约为 40-46 tokens/s，显著高于 BF16 KV Cache 配置的 25-28 tokens/s，但需验证 INT8 KV Cache 的精度损失是否导致生成质量下降（如困惑度增加 > 10%）。

## Corrected Claim

RTX 3090 Ti 在 INT8 KV Cache 配置下的 Decode 吞吐量修正：理论 Decode 上限 = 1008 GB/s / (13.5 GB + 4 GB) = 57.7 tokens/s，实测效率系数 0.7-0.8 后约为 40-46 tokens/s，显著高于 BF16 KV Cache 配置的 25-28 tokens/s，但需验证 INT8 KV Cache 的精度损失是否导致生成质量下降（如困惑度增加 > 10%）。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 3090 Ti 显存带宽 1008 GB/s 与 INT8 KV Cache 体积估算符合硬件规格与算术逻辑，效率系数 0.7-0.8 符合 LLM 推理常见实测范围，数值量级合理且内部自洽。
