# N344: H100 上 FP8 与 BF16 的质量损失对比基准：在 LLM 推理场景中，FP8 (E4M3) 量化导致的 MMLU 准确率下降通常 < 0.5 个百分点

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N136

## Claim

H100 上 FP8 与 BF16 的质量损失对比基准：在 LLM 推理场景中，FP8 (E4M3) 量化导致的 MMLU 准确率下降通常 < 0.5 个百分点，HumanEval 下降 < 1 个百分点，远低于 W4 量化 (>5 个百分点)；因此对于 H100，FP8 是质量与速度平衡的最优精度，无需考虑 NVFP4。

## Corrected Claim

在 LLM 推理场景中，FP8 (E4M3) 量化导致的 MMLU 准确率下降通常较小（文献报道多在 0.5 个百分点以内），HumanEval 下降也相对有限，显著优于 W4 量化（通常 >5 个百分点）。对于 H100，FP8 是质量与速度平衡的常用高精度选择，但 NVFP4 在特定低精度需求场景下仍具探索价值，并非完全无需考虑。

## Evidence

[质询]该陈述包含具体的经验性数值阈值（MMLU < 0.5%, HumanEval < 1%）和绝对化的结论（'无需考虑 NVFP4'），这些属于经验事实而非第一性原理可推导内容。此外，'无需考虑 NVFP4'的结论过于绝对，忽略了NVFP4在特定低延迟或高吞吐场景下的潜在优势，且缺乏来源支持该绝对化判断。 | 经验事实，逻辑自洽但缺来源支持；检索无可用来源，无法验证具体数值阈值及绝对化结论。

## Search Query

LLM FP8 quantization accuracy loss MMLU HumanEval benchmark
