# N42: Mac Studio M2 Ultra 192GB 统一内存在 W4 量化下运行 Qwen3-27B 32K 上下文的显存占用为 13.5GB(权重) + 4.

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7

## Claim

Mac Studio M2 Ultra 192GB 统一内存在 W4 量化下运行 Qwen3-27B 32K 上下文的显存占用为 13.5GB(权重) + 4.5GB(KV Cache) + 2GB(激活/框架) ≈ 20GB，小于 192GB 统一内存，无需 Offload，可完整驻留内存

## Corrected Claim

Mac Studio M2 Ultra 192GB 统一内存在 W4 量化下运行 Qwen3-27B 32K 上下文的显存占用为 13.5GB(权重) + 4.5GB(KV Cache) + 2GB(激活/框架) ≈ 20GB，小于 192GB 统一内存，无需 Offload，可完整驻留内存

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B在W4量化下权重约13.5GB，32K上下文KV Cache约4.5GB，加上激活/框架开销约2GB，总显存占用约20GB，远小于192GB统一内存，无需Offload，可完整驻留内存。
