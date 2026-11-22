# N143: NVFP4/W4精度质量损失量化：Qwen3-27B在W4下MMLU得分从85%降至81.5%（-4.1%），GSM8K从82%降至77.5%（-5.5%），H

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N24

## Claim

NVFP4/W4精度质量损失量化：Qwen3-27B在W4下MMLU得分从85%降至81.5%（-4.1%），GSM8K从82%降至77.5%（-5.5%），HumanEval从68%降至61.5%（-9.5%），最大损失9.5%，代码任务损失最大

## Corrected Claim

Qwen3-27B在NVFP4/W4量化下存在精度损失，通常代码类任务（如HumanEval）损失较大，但具体数值（如MMLU -4.1%等）缺乏当前来源支持。

## Evidence

[质询]参考来源仅提供了模型量化后的存储大小和量化方法（NVFP4/W4A4），完全未包含任何具体的基准测试分数（MMLU, GSM8K, HumanEval）或精度损失数据，无法验证具体的数值变化。 | 来源[1]确认了存在Qwen3-27B的NVFP4量化版本，但未提供具体的精度损失数值，属于经验事实且缺乏直接来源支持，逻辑上量化导致精度下降是合理的，但具体数值无法核验。

## Search Query

Qwen3-27B W4A16 quantization benchmark MMLU GSM8K HumanEval

## Retrieval Sources

- {'url': 'https://huggingface.co/kelnei/Qwen3.8-27B-NVFP4&rut=e5c44637812d55b5ee34be92b87e9132956009f9f53f9a6c621f7e3223b77e66', 'type': 'ddg', 'title': 'kelnei/Qwen3.8-27B-NVFP4 · Hugging Face'}
