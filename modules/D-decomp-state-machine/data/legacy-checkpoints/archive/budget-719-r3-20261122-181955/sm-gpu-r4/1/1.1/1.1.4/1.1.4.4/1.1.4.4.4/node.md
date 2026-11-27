# N432: W3 量化（3-bit）相比 BF16/INT8 的精度损失量化基准：在 MMLU 基准上，W3 量化通常导致 3-6% 的性能下降；在 HumanEval (

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N144

## Claim

W3 量化（3-bit）相比 BF16/INT8 的精度损失量化基准：在 MMLU 基准上，W3 量化通常导致 3-6% 的性能下降；在 HumanEval (代码生成) 上，下降幅度通常为 5-10%。若 N119 设定的可接受阈值为 MMLU 下降 <2% 或 HumanEval 下降 <5%，则 W3 方案确实被排除。

## Corrected Claim

W3 量化相比 BF16/INT8 通常会导致显著的精度损失，在 MMLU 和 HumanEval 等基准上，性能下降幅度往往超过 2% 和 5% 的常见可接受阈值，具体数值取决于模型架构和量化算法。

## Evidence

[质询]数值量级与具体基准的对应关系缺乏普遍共识，不同模型架构（如LLaMA vs Mistral）和量化算法（如GPTQ vs AWQ）下，W3量化在MMLU和HumanEval上的精度损失波动较大，'通常导致3-6%'和'5-10%'的断言可能过于绝对，且未指明具体模型规模。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且该具体数值范围属于经验规格，无法从第一性原理严格推出）

## Search Query

Qwen3 27B W3 quantization accuracy loss MMLU HumanEval benchmark
