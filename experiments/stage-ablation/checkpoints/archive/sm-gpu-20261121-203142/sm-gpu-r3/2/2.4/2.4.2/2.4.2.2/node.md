# N195: NVFP4 (4-bit) 量化相比 BF16 在 GPQA 上的准确率绝对下降值 (ΔGPQA)，基于 NVIDIA TensorRT-LLM 官方基准或 Q

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N59

## Claim

NVFP4 (4-bit) 量化相比 BF16 在 GPQA 上的准确率绝对下降值 (ΔGPQA)，基于 NVIDIA TensorRT-LLM 官方基准或 Qwen 社区复现数据，预期范围 1.0%-2.5%，需确认具体数值 [待核验]

## Corrected Claim

NVFP4 (4-bit) 量化相比 BF16 在 GPQA 上的准确率存在一定程度的下降，具体数值需参考 NVIDIA TensorRT-LLM 官方基准或 Qwen 社区复现数据确认。

## Evidence

[质询]该陈述包含具体的经验数值范围（1.0%-2.5%），属于硬件/模型性能指标，无法从第一性原理推导，且缺乏来源支持，存在数值偏差风险。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

Qwen3-27B NVFP4 4-bit quantization GPQA accuracy drop TensorRT-LLM
