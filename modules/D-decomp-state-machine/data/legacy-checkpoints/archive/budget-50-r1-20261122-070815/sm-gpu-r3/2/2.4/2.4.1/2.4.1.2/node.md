# N225: GPTQ 算法在 NVFP4 量化 Qwen3-27B 时的校准数据集大小通常为 128 个样本（每个样本约 2048 tokens），来自 C4 或 RedP

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N65

## Claim

GPTQ 算法在 NVFP4 量化 Qwen3-27B 时的校准数据集大小通常为 128 个样本（每个样本约 2048 tokens），来自 C4 或 RedPajama 数据集，总计算量约为 262K tokens；AWQ 算法通常使用 128 个样本，但更侧重于识别关键通道，校准时间约为 GPTQ 的 1/5

## Corrected Claim

GPTQ 算法在量化大模型时通常使用 128 至 512 个样本进行校准（每个样本约 2048 tokens），数据常来自 C4 或 RedPajama；AWQ 算法同样使用类似规模的样本，但因其仅识别关键通道而无需复杂的矩阵分解，校准速度通常显著快于 GPTQ。

## Evidence

[质询]GPTQ 校准样本数通常为 128-512 不等，且 NVFP4 是 NVIDIA 较新的量化格式，其标准校准流程是否严格固定为 128 样本且总计算量精确为 262K tokens 缺乏通用共识支持；AWQ 校准时间仅为 GPTQ 1/5 的说法过于绝对，实际耗时取决于硬件和实现细节，通常 AWQ 因无需求解 Hessian 矩阵而更快，但比例并非固定常数。 | 先验知识/题面给定，逻辑校验通过，但具体数值（如 262K tokens、1/5 时间比）属于经验性参数，缺乏通用标准支持，故降级为定性表述。
