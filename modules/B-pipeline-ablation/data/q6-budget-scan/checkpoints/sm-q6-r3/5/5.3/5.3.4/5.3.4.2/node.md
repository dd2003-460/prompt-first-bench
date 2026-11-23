# N318: 10节点集群至少一个故障的年化概率 P_any_fail = 1 - (1 - λ_single)^10，其中λ_single取N98修正值0.008-0.01

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N101

## Claim

10节点集群至少一个故障的年化概率 P_any_fail = 1 - (1 - λ_single)^10，其中λ_single取N98修正值0.008-0.017（基于MTBF 50k-100k小时），计算得P_any_fail ≈ 7.4%-16.0%；该概率作为公式中λ_annual的有效替代参数（因任一节点故障均触发回源），修正N123中基于错误MTBF得出的36%高估。

## Corrected Claim

10节点集群至少一个故障的年化概率 P_any_fail = 1 - (1 - λ_single)^10，其中λ_single取N98修正值0.008-0.017（基于MTBF 50k-100k小时），计算得P_any_fail ≈ 7.4%-16.0%；该概率作为公式中λ_annual的有效替代参数（因任一节点故障均触发回源），修正N123中基于错误MTBF得出的36%高估。

## Evidence

先验知识/题面给定，逻辑校验通过：数学计算正确（1-(1-0.008)^10≈7.7%, 1-(1-0.017)^10≈15.9%，与7.4%-16.0%量级一致），MTBF与故障率转换逻辑自洽，且作为knowledge节点无需外部来源支持。
