# N92: Qwen3-27B 在 NVFP4/W4 精度下，在代码生成基准 (HumanEval/MBPP) 上的得分，及相对 BF16 的得分下降百分比，用于评估长尾任

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N21, N22, N23

## Claim

Qwen3-27B 在 NVFP4/W4 精度下，在代码生成基准 (HumanEval/MBPP) 上的得分，及相对 BF16 的得分下降百分比，用于评估长尾任务崩塌风险。

## Corrected Claim

Qwen3-27B 在 NVFP4/W4 精度下存在代码生成基准（HumanEval/MBPP）的性能评估需求，但具体得分及相对 BF16 的下降百分比需查阅具体评测报告，当前来源未提供确切数值。

## Evidence

[质询]参考来源仅提供了模型名称和量化方法，未包含任何具体的基准测试得分（HumanEval/MBPP）或相对BF16的性能下降数据，无法验证具体数值。 | 来源[1]确认了Qwen3-27B NVFP4模型的存在，但未提供代码生成基准的具体得分或下降百分比，属于经验事实且缺乏直接数据支持。

## Search Query

Qwen3-27B W4 HumanEval MBPP code generation benchmark

## Retrieval Sources

- {'url': 'https://huggingface.co/nvidia/Qwen3.8-27B-NVFP4&rut=8619c6f7e5f11d335c66ffe0751c944d8b4eaa41fab91e35dcba7c4f04699719', 'type': 'ddg', 'title': 'nvidia/Qwen3.8-27B-NVFP4 · Hugging Face'}
