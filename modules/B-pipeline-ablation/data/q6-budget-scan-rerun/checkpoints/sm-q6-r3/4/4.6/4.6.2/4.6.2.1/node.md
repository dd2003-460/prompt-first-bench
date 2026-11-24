# N278: 工作点A（高可靠低抖动）：采用智能路由（BGP/Anycast）切换机制，T_switch = 5s，P99 延迟抖动 ΔP99_A = (5s / T_tar

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N89

## Claim

工作点A（高可靠低抖动）：采用智能路由（BGP/Anycast）切换机制，T_switch = 5s，P99 延迟抖动 ΔP99_A = (5s / T_target) × 100%，当 T_target=100ms 时 ΔP99_A = 5000%（超出目标，需验证实际 T_target 值或修正公式单位），此工作点提供最低切换延迟但可能增加路由配置复杂度成本

## Corrected Claim

工作点A（高可靠低抖动）：采用智能路由（BGP/Anycast）切换机制，T_switch = 5s。需注意：原公式 ΔP99_A = (T_switch / T_target) × 100% 缺乏标准定义，若 T_target=100ms，计算结果 5000% 可能因单位或公式误用导致，建议重新定义抖动指标（如绝对延迟增加量或相对基线的百分比）并验证实际 T_target 值。此工作点提供较低切换延迟但可能增加路由配置复杂度成本。

## Evidence

[质询]公式 ΔP99_A = (T_switch / T_target) × 100% 缺乏明确的物理或统计定义依据，将切换时间直接除以目标延迟并乘以100%作为“P99延迟抖动”在量纲和逻辑上均不严谨，且5000%的抖动数值在实际网络工程中极不合理，疑似单位混淆或公式误用。 | 先验知识/题面给定，但逻辑校验发现公式定义模糊且数值量级异常，无法排除公式错误的可能性，故降级。
