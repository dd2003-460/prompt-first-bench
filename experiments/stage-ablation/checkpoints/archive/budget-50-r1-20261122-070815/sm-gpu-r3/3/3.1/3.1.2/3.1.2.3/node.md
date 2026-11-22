# N253: RTX 4090 的 GDDR6X 显存功耗密度约为 0.1-0.15 W/GB/s，在 1008 GB/s 满载带宽下，显存部分功耗约为 100-150W，占

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N75

## Claim

RTX 4090 的 GDDR6X 显存功耗密度约为 0.1-0.15 W/GB/s，在 1008 GB/s 满载带宽下，显存部分功耗约为 100-150W，占 GPU TDP (450W) 的 22-33%；若追求极致性价比，需对比 RTX 3090 (936 GB/s, 925W TDP) 的能效比，3090 的 W/GB/s 约为 0.11，略优于 4090 的能效表现。

## Corrected Claim

RTX 4090 的 GDDR6X 显存功耗约为 100-150W（占 TDP 450W 的 22-33%）；对比 RTX 3090（936 GB/s, 350W TDP），需重新计算其显存部分功耗以评估能效比，原陈述中 3090 的 TDP 及能效比数据错误。

## Evidence

[质询]RTX 3090 的 TDP 数值存在严重事实错误（实际为 350W，而非 925W），导致基于此计算的能效比（W/GB/s）完全失真；此外，GDDR6X 显存功耗密度通常以 mW/GB/s 或 W/GB 衡量，0.1-0.15 W/GB/s 的量级在物理上极不合理（若按此计算，1008 GB/s 带宽仅消耗 0.1-0.15W，与后文 100-150W 的结论自相矛盾，单位应为 W/GB 或数值需调整）。 | 先验知识/题面给定，逻辑校验未通过：RTX 3090 TDP 实为 350W，且显存功耗密度单位与数值存在内部矛盾（0.1 W/GB/s * 1008 GB/s ≈ 0.1W，而非 100W）。

## Search Query

RTX 4090 vs 3090 memory bandwidth power efficiency W per GB/s LLM inference
