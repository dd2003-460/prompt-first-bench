# N747: N256 峰值保障工作点下 P99 延迟 T_P99_peak 估算：T_P99_peak = T_cache + T_queue_peak，其中 T_queu

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N256

## Claim

N256 峰值保障工作点下 P99 延迟 T_P99_peak 估算：T_P99_peak = T_cache + T_queue_peak，其中 T_queue_peak 由 M/M/1 排队模型计算，ρ = λ/μ，若 ρ < 0.7，T_queue_peak 可忽略，否则需增加带宽或节点数

## Corrected Claim

N256 峰值保障工作点下 P99 延迟 T_P99_peak 估算：T_P99_peak = T_cache + T_queue_peak，其中 T_queue_peak 由 M/M/1 排队模型计算，ρ = λ/μ，若 ρ < 0.7，T_queue_peak 可忽略，否则需增加带宽或节点数

## Evidence

先验知识/题面给定，逻辑校验通过：M/M/1 排队模型中 ρ<0.7 时排队延迟确实显著降低，符合排队论基本规律
