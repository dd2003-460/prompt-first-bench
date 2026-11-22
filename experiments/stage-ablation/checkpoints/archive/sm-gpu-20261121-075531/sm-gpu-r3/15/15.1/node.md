# N381: RTX 4090/5090 在满负载（INT8推理）下的风扇噪音实测值通常超过 60-70 dBA（距离1米），而 Mac Studio M2 Ultra/M3

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N130

## Claim

RTX 4090/5090 在满负载（INT8推理）下的风扇噪音实测值通常超过 60-70 dBA（距离1米），而 Mac Studio M2 Ultra/M3 Ultra 在同等负载下噪音低于 30 dBA，噪音差值 >30 dBA 构成硬性排除条件。

## Corrected Claim

RTX 4090/5090 在满负载（INT8推理）下的风扇噪音实测值通常显著高于 Mac Studio M2 Ultra/M3 Ultra（后者通常低于 30 dBA），两者噪音差值往往超过 30 dBA，这在许多对静音有严格要求的场景中构成排除 GPU 方案的关键因素。

## Evidence

[质询]数值量级与具体阈值缺乏统一标准：RTX 4090/5090 在满负载下的噪音因品牌（AIB vs 公版）、风扇曲线设置及测试环境差异极大，部分高端三风扇型号在优化模式下可能低于 60 dBA；同时，'噪音差值 >30 dBA 构成硬性排除条件'属于主观工程决策或特定场景约束，并非物理定律或通用事实，将其表述为绝对事实存在以偏概全的风险。 | 先验知识/题面给定，逻辑校验通过：GPU 高功耗散热噪音通常显著高于 Mac Studio 的被动/低噪散热设计，量级对比（>60 vs <30 dBA）符合工程直觉，但具体数值阈值和'硬性排除'的定性描述缺乏通用标准支持，故降级为定性表述。
