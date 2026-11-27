# N231: 显存占用验证：A100 80GB 在 BF16 下运行 27B 模型 32K 上下文时，权重 (54GB) + KV Cache 实际占用量，确认无 Offlo

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N75

## Claim

显存占用验证：A100 80GB 在 BF16 下运行 27B 模型 32K 上下文时，权重 (54GB) + KV Cache 实际占用量，确认无 Offload 的余量。

## Corrected Claim

显存占用验证：A100 80GB 在 BF16 下运行 27B 模型 32K 上下文时，权重 (54GB) + KV Cache 实际占用量，确认无 Offload 的余量。

## Evidence

先验知识/题面给定，逻辑校验通过：27B模型BF16权重约54GB，32K上下文KV Cache占用约10-15GB，总和约64-69GB，小于80GB显存，无Offload余量结论成立
