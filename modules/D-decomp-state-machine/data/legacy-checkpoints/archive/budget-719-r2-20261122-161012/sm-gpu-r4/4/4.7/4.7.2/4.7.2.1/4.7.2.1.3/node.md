# N607: 显存可行性边界：Qwen3-27B BF16 权重 (54GB) + KV Cache (34.36GB) + Activation (~2GB) ≈ 90.3

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N253

## Claim

显存可行性边界：Qwen3-27B BF16 权重 (54GB) + KV Cache (34.36GB) + Activation (~2GB) ≈ 90.36GB。结论：单卡 24GB/32GB 显存无法运行 BF16 32K 上下文；需至少 96GB 显存 (如 A100/H100) 或启用 KV Cache 量化/Offload。

## Corrected Claim

显存可行性边界：Qwen3-27B BF16 权重 (54GB) + KV Cache (34.36GB) + Activation (~2GB) ≈ 90.36GB。结论：单卡 24GB/32GB 显存无法运行 BF16 32K 上下文；需至少 96GB 显存 (如 A100/H100) 或启用 KV Cache 量化/Offload。

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数BF16权重约54GB，32K上下文KV Cache约34GB，总和约90GB，远超24/32GB显存，需96GB+显存，数值量级与工程常识一致。
