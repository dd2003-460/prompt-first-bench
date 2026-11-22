# N147: 多卡方案 (2x GPU) 的系统级故障率计算：假设单卡故障相互独立，双卡系统 AFR_sys = 1 - (1 - AFR_single)^2。若单卡 AFR

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N33

## Claim

多卡方案 (2x GPU) 的系统级故障率计算：假设单卡故障相互独立，双卡系统 AFR_sys = 1 - (1 - AFR_single)^2。若单卡 AFR=10%，则双卡 AFR_sys ≈ 19%，即系统年故障概率翻倍，需据此计算年均预期故障次数。

## Corrected Claim

多卡方案 (2x GPU) 的系统级故障率计算：假设单卡故障相互独立，双卡系统 AFR_sys = 1 - (1 - AFR_single)^2。若单卡 AFR=10%，则双卡 AFR_sys ≈ 19%，即系统年故障概率翻倍，需据此计算年均预期故障次数。

## Evidence

先验知识/题面给定，逻辑校验通过：基于独立事件概率公式 P(A∪B) = 1 - (1-p)^2，当 p=0.1 时，1 - 0.9^2 = 0.19，计算无误且符合可靠性工程基本原理。
