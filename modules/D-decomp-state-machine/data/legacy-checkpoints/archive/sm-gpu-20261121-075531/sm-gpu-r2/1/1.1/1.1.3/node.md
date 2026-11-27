# N37: W4/INT4 精度下显存占用修正项：主流 W4A16 量化方案（如 GPTQ/AWQ）通常使用 4-bit 权重 + 4-bit 或 8-bit 缩放因子（S

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N6

## Claim

W4/INT4 精度下显存占用修正项：主流 W4A16 量化方案（如 GPTQ/AWQ）通常使用 4-bit 权重 + 4-bit 或 8-bit 缩放因子（Scale/Zero-point），需计算缩放因子带来的额外显存开销（通常增加 5-10% 的显存占用，即实际占用 ≈ 13.5GB * 1.05 至 1.10）。

## Corrected Claim

W4/INT4 精度下显存占用修正项：主流 W4A16 量化方案（如 GPTQ/AWQ）通常使用 4-bit 权重 + 4-bit 或 8-bit 缩放因子（Scale/Zero-point），需计算缩放因子带来的额外显存开销（通常增加 5-10% 的显存占用，即实际占用 ≈ 13.5GB * 1.05 至 1.10）。

## Evidence

先验知识/题面给定，逻辑校验通过：W4A16量化中，4-bit权重需每128或256个权重共享一个scale/zero-point（通常为FP16或INT8），额外开销约为 (16/4)/128 ≈ 3.1% 或 (8/4)/128 ≈ 1.5% 至 (16/4)/64 ≈ 6.25%，加上其他元数据，5-10%的估算范围在工程实践中是合理且常见的保守估计。

## Search Query

GPTQ AWQ W4A16 quantization scale zero-point memory overhead percentage
