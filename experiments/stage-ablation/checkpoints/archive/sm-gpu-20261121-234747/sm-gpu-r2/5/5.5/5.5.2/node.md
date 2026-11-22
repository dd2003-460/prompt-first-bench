# N132: HumanEval代码生成基准测试中，Qwen3-27B在不同精度下的通过率下降ΔHumanEval = Pass@1_BF16 - Pass@1_quanti

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N25

## Claim

HumanEval代码生成基准测试中，Qwen3-27B在不同精度下的通过率下降ΔHumanEval = Pass@1_BF16 - Pass@1_quantized，需量化各精度对代码生成能力的影响，特别是W4量化是否导致逻辑错误率上升

## Corrected Claim

HumanEval代码生成基准测试中，Qwen3-27B在不同精度下的通过率下降ΔHumanEval = Pass@1_BF16 - Pass@1_quantized，需量化各精度对代码生成能力的影响，特别是W4量化是否导致逻辑错误率上升（具体数值待验证）

## Evidence

[质询]该陈述包含具体的经验性数值结论（Qwen3-27B在W4量化下的具体通过率下降幅度及逻辑错误率变化），属于硬件/模型性能经验事实，无法从第一性原理推导，且当前无可用来源支持具体数值。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）

## Search Query

Qwen3-27B HumanEval pass@1 FP8 INT8 W4 quantization impact
