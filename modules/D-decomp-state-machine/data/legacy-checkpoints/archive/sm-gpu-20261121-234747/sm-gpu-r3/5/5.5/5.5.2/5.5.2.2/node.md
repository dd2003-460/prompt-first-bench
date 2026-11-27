# N397: Qwen3-27B FP8量化版本的HumanEval Pass@1通过率Pass1_FP8，需验证FP8量化是否影响代码生成的逻辑正确性；由于代码生成对tok

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N132

## Claim

Qwen3-27B FP8量化版本的HumanEval Pass@1通过率Pass1_FP8，需验证FP8量化是否影响代码生成的逻辑正确性；由于代码生成对token序列的精确性要求高，FP8的轻微数值误差可能导致语法错误率上升，需引用具体量化模型在HumanEval上的重跑结果。

## Corrected Claim

Qwen3-27B FP8量化版本的HumanEval Pass@1通过率需通过具体实验验证；理论上FP8量化可能因数值精度降低影响代码生成的token序列精确性，进而可能增加语法错误率，但具体影响程度需引用特定量化方案在HumanEval基准上的实测数据。

## Evidence

[质询]该陈述包含具体的经验性断言（FP8量化导致语法错误率上升、需引用具体重跑结果），但缺乏具体的量化数据支持，且‘轻微数值误差导致语法错误率上升’这一因果链条在缺乏具体实验数据的情况下属于推测，不同量化实现（如SmoothQuant, GPTQ等）对代码生成的影响可能不同，不能一概而论。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源，无法验证具体量化模型在HumanEval上的重跑结果及FP8对代码生成逻辑正确性的具体影响程度）

## Search Query

Qwen3-27B FP8 HumanEval Pass@1 code accuracy
