# N44: Qwen3-27B 在 4-bit 量化 (W4A8/W4A16) 下，推理所需的总硬性显存需求为 54.46-57.96 GB，由 13.5-17 GB 权重

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N8

## Claim

Qwen3-27B 在 4-bit 量化 (W4A8/W4A16) 下，推理所需的总硬性显存需求为 54.46-57.96 GB，由 13.5-17 GB 权重显存与 40.96 GB KV Cache 显存相加得出，需额外预留约 2-5 GB 用于激活值缓冲和框架开销。

## Corrected Claim

Qwen3-27B 在 4-bit 量化 (W4A8/W4A16) 下，推理所需的总硬性显存需求为 54.46-57.96 GB，由 13.5-17 GB 权重显存与 40.96 GB KV Cache 显存相加得出，需额外预留约 2-5 GB 用于激活值缓冲和框架开销。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B参数量约27B，4-bit量化权重约13.5GB，KV Cache 40.96GB，总显存需求54.46-57.96GB，数值量级合理且内部自洽
