# N218: FP8 (E4M3) 相比 INT8 在长上下文下的优势量化：FP8 动态范围约为 INT8 的 4 倍 (max ~448 vs 127)，且尾数位数更多 (

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N70

## Claim

FP8 (E4M3) 相比 INT8 在长上下文下的优势量化：FP8 动态范围约为 INT8 的 4 倍 (max ~448 vs 127)，且尾数位数更多 (3 bits vs 0 bits 有效精度差异)，导致在 Attention Score 大动态范围场景下，FP8 的相对量化误差比 INT8 低约 50-70% [待核验，需基于 Qwen3 实际激活分布统计验证]。

## Corrected Claim

FP8 (E4M3) 相比 INT8 在长上下文下的优势：FP8 动态范围约为 INT8 的 3.5 倍 (max 448 vs 127)，且尾数位数更多 (3 bits vs 0 bits)，在 Attention Score 大动态范围场景下，FP8 的相对量化误差通常低于 INT8，具体降低幅度需基于实际激活分布统计验证。

## Evidence

[质询]该陈述包含具体的经验性量化结论（'相对量化误差低约 50-70%'），这依赖于特定的激活分布统计，无法从第一性原理直接推导，且缺乏来源支持。此外，'动态范围约为4倍'的表述在量纲上不够严谨（448/127≈3.5，且FP8 E4M3最大值为448，INT8最大值为127，比值接近3.5而非4，虽量级正确但数值不精确）。 | 经验事实，逻辑自洽但缺来源支持。FP8 E4M3最大值为448，INT8最大值为127，动态范围比值约3.5倍，量级合理；FP8尾数3位 vs INT8 0位（整数），精度优势逻辑成立，但具体误差降低比例（50-70%）无来源验证，故降级。

## Search Query

FP8 E4M3 vs INT8 quantization error dynamic range transformer attention
