# N28: Qwen3.8-27B NVFP4 量化在长链科研任务（>8k tokens 推理链）中的实际表现未知。[待核验] 假设量化导致的精度损失 ΔAccuracy 

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N6

## Claim

Qwen3.8-27B NVFP4 量化在长链科研任务（>8k tokens 推理链）中的实际表现未知。[待核验] 假设量化导致的精度损失 ΔAccuracy ≈ 2-5%，需通过对比 FP16 与 NVFP4 在 GSM8K/HumanEval 等基准上的得分差异来量化，并评估其对多步逻辑推理失败率的放大效应。

## Corrected Claim

Qwen3.8-27B NVFP4 量化在长链科研任务（>8k tokens 推理链）中的实际表现未知。需通过对比 FP16 与 NVFP4 在 GSM8K/HumanEval 等基准上的得分差异来量化精度损失，并评估其对多步逻辑推理失败率的影响。

## Evidence

[质询]该陈述包含具体的经验性数值假设（ΔAccuracy ≈ 2-5%），这属于特定模型版本（Qwen3.8-27B）和特定量化格式（NVFP4）下的实证数据，无法从第一性原理或数学公理中严格推导得出，且当前无可用来源支持该具体数值范围。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且具体精度损失百分比属经验参数，不适用第一性原理推导条款）

## Search Query

Qwen3.8-27B NVFP4 quantization impact on long chain of thought reasoning accuracy benchmark
