# N167: Qwen3-27B 在 HumanEval 代码生成基准上，INT8 精度相比 BF16 的 Pass@1 下降幅度约为 2.0% - 4.0%，且错误类型主要

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N48

## Claim

Qwen3-27B 在 HumanEval 代码生成基准上，INT8 精度相比 BF16 的 Pass@1 下降幅度约为 2.0% - 4.0%，且错误类型主要集中在长依赖逻辑断裂，而非语法错误（定性结论需量化为具体测试集子集的平均分差）

## Corrected Claim

Qwen3-27B 在 HumanEval 代码生成基准上，INT8 精度相比 BF16 的 Pass@1 存在一定程度的下降，具体幅度取决于量化算法，且错误类型可能涉及逻辑连贯性而非单纯语法错误（需具体量化数据支持）。

## Evidence

[质询]该陈述包含具体的量化范围（2.0%-4.0%）和特定的错误类型分布（长依赖逻辑断裂 vs 语法错误），属于经验事实。在缺乏任何参考来源支持的情况下，无法验证这些具体数值和定性结论的准确性，且不同量化方案（如GPTQ, AWQ, SmoothQuant）对代码生成任务的影响差异可能较大，单一范围可能以偏概全。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）。

## Search Query

Qwen3-27B INT8 quantization HumanEval code generation accuracy loss
