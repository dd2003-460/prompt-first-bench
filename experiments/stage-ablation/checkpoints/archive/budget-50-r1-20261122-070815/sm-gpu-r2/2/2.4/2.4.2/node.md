# N66: NVFP4 量化在数学推理基准（GSM8K, MATH）上的分数下降幅度（Delta %）具体数值，需对比 BF16 基线，因为 4-bit 量化对逻辑链较长的

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N15, N16, N17

## Claim

NVFP4 量化在数学推理基准（GSM8K, MATH）上的分数下降幅度（Delta %）具体数值，需对比 BF16 基线，因为 4-bit 量化对逻辑链较长的任务敏感度远高于通用对话

## Corrected Claim

NVFP4量化在数学推理基准（如Math-500）上通常能保持极高的精度一致性（差异<1%或为0），具体GSM8K/MATH的Delta数值需视具体模型和量化配置而定，并非必然出现远高于通用对话的显著下降。

## Evidence

[质询]陈述声称4-bit量化对逻辑链较长的任务（如GSM8K, MATH）敏感度远高于通用对话，暗示会有显著分数下降；但参考来源[1]显示在DeepSeek-R1-0528模型上，NVFP4量化后Math-500（数学推理基准）结果保持完全一致，且其他基准差异在1%以内，这与‘敏感度远高于通用对话’或‘显著下降’的定性描述存在潜在冲突，且来源未提供GSM8K/MATH的具体Delta数值。 | 来源[1]间接支持NVFP4在数学基准（Math-500）上精度保持良好（差异为0或<1%），但未提供GSM8K/MATH的具体Delta数值，且‘敏感度远高于通用对话’这一比较性结论缺乏直接数据支持，属于经验事实且缺乏多源一致或直接支持，故降级。

## Search Query

Qwen3-27B 4-bit quantization GSM8K MATH benchmark score drop percentage vs BF16

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/1944504541950248086&rut=33cf0e3f80136bb00d6ec38a03b19592e2a370c03b3af8179d4149c3a96ab929', 'type': 'ddg', 'title': 'Nvfp4量化技术深度解析：4位精度下实现2.3倍推理加速 - 知乎'}
