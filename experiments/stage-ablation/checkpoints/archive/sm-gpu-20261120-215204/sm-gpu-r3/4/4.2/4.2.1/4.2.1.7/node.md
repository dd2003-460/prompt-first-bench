# N284: 静态量化 (Static FP8) 的校准数据集规模要求：Qwen3-27B 需至少 512-1024 条代表性样本（覆盖数学、代码、通用对话）进行校准，以计算

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N98, N99, N100

## Claim

静态量化 (Static FP8) 的校准数据集规模要求：Qwen3-27B 需至少 512-1024 条代表性样本（覆盖数学、代码、通用对话）进行校准，以计算每层 Activation 的 Scale Factor；数据量少于 256 条时，校准误差导致 MMLU 下降 >2%

## Corrected Claim

静态量化 (Static FP8) 的校准数据集规模要求：Qwen3-27B 建议至少使用 512-1024 条代表性样本（覆盖数学、代码、通用对话）进行校准，以计算每层 Activation 的 Scale Factor；数据量过少（如少于 256 条）可能导致校准误差，进而引起 MMLU 等基准测试性能下降。

## Evidence

[质询]具体数值阈值（512-1024条、256条、MMLU下降>2%）缺乏通用标准支持，属于特定实验条件下的经验性结论，不同模型架构或量化实现（如SmoothQuant vs 原生FP8）对校准数据量的敏感度差异巨大，直接断言Qwen3-27B的硬性阈值存在过度泛化风险。 | 先验知识/题面给定，逻辑校验通过（静态量化确实需要校准数据计算Scale，数据量不足会导致统计偏差从而降低精度，量级符合工程直觉），但具体数值为经验事实且无外部来源直接支持，故降级。

## Search Query

FP8 static quantization calibration dataset size requirement LLM
