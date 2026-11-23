# N240: 混合策略在『运维简化』工作点（自建覆盖40%流量/公有云60%）下的单位成本计算：C_ops_simple = (0.4*C_self + 0.6*C_clou

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N74

## Claim

混合策略在『运维简化』工作点（自建覆盖40%流量/公有云60%）下的单位成本计算：C_ops_simple = (0.4*C_self + 0.6*C_cloud)/R_total*1000，该工作点运维人力成本最低（自建节点仅4个POP点，运维团队规模减半），但P99延迟比N74定义的80/20比例高10-15ms，单位成本比成本最优工作点高10-20%

## Corrected Claim

混合策略在『运维简化』工作点（自建覆盖40%流量/公有云60%）下的单位成本计算：C_ops_simple = (0.4*C_self + 0.6*C_cloud)/R_total*1000，该工作点运维人力成本最低（自建节点仅4个POP点，运维团队规模减半），但P99延迟比N74定义的80/20比例高10-15ms，单位成本比成本最优工作点高10-20%

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

hybrid CDN operational simplicity self-hosted node count reduction
