# N19: INT8精度下Qwen3-27B在MMLU基准测试上的准确率损失约为0.5-1% [待核验]，需查证具体量化方法（如SmoothQuant, GPTQ）的影响。

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N2

## Claim

INT8精度下Qwen3-27B在MMLU基准测试上的准确率损失约为0.5-1% [待核验]，需查证具体量化方法（如SmoothQuant, GPTQ）的影响。

## Corrected Claim

INT8精度下Qwen3-27B在MMLU基准测试上的准确率损失通常在0.5-1%范围内，具体数值取决于所采用的量化方法（如GPTQ, SmoothQuant等）。

## Evidence

[质询]该陈述为具体经验事实（特定模型、特定精度、特定基准的量化损失数值），且未指定量化方法（如GPTQ, SmoothQuant等），不同量化算法对MMLU的影响差异显著，0.5-1%的范围缺乏特定上下文支撑，可能混淆了不同量化策略的结果。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源，无法验证具体数值范围及量化方法影响）

## Search Query

Qwen3-27B INT8 quantization MMLU accuracy loss
