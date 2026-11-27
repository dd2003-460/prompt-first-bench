# N69: INT8 精度下 Qwen3-27B 的质量退化基准数据：引用 GPTQ/AWQ 或 SmoothQuant 算法量化后的 Qwen3-27B 在标准基准（MM

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N16, N17, N18

## Claim

INT8 精度下 Qwen3-27B 的质量退化基准数据：引用 GPTQ/AWQ 或 SmoothQuant 算法量化后的 Qwen3-27B 在标准基准（MMLU, HumanEval）上的准确率下降幅度，并与 BF16 基线对比，确认是否超过 2-5% 的容忍阈值。

## Corrected Claim

INT8 精度下 Qwen3-27B 的质量退化基准数据：引用 GPTQ/AWQ 或 SmoothQuant 算法量化后的 Qwen3-27B 在标准基准（MMLU, HumanEval）上的准确率下降幅度，并与 BF16 基线对比，需进一步实验确认是否超过 2-5% 的容忍阈值。

## Evidence

[质询]该陈述包含具体的经验性数值结论（准确率下降幅度是否超过2-5%），属于硬件/模型性能经验事实，无法从第一性原理推导，且缺乏具体基准测试数据支持。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法验证具体量化退化幅度）

## Search Query

Qwen3-27B INT8 GPTQ AWQ quantization benchmark accuracy degradation
