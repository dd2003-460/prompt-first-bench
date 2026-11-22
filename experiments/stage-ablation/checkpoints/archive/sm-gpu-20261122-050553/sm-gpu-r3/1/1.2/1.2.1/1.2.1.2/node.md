# N130: 修正自矛盾检测：RTX 4060 Ti 16GB 在 W4 量化下（权重 13.5GB）剩余显存仅为 16GB - 13.5GB - 1.5GB (CUDA C

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N40

## Claim

修正自矛盾检测：RTX 4060 Ti 16GB 在 W4 量化下（权重 13.5GB）剩余显存仅为 16GB - 13.5GB - 1.5GB (CUDA Context/Activations) ≈ 1.0GB，远低于 32K BF16 KV Cache 所需的 16GB，缺口达 15GB，证明单卡方案在容量上绝对不可行。

## Corrected Claim

修正自矛盾检测：RTX 4060 Ti 16GB 在 W4 量化下（权重 13.5GB）剩余显存仅为 16GB - 13.5GB - 1.5GB (CUDA Context/Activations) ≈ 1.0GB，远低于 32K BF16 KV Cache 所需的 16GB，缺口达 15GB，证明单卡方案在容量上绝对不可行。

## Evidence

先验知识/题面给定，逻辑校验通过：16GB总显存减去13.5GB权重和1.5GB开销后剩余1GB，确实远小于32K BF16 KV Cache所需的16GB，数学推导自洽且符合硬件常识。
