# N319: SRE人数下限计算：N_sre_min = ceil(10 / 10 * 1.5) = 2人，对应k_oncall=1.5，适用于故障率低（λ_node<1/年

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N101

## Claim

SRE人数下限计算：N_sre_min = ceil(10 / 10 * 1.5) = 2人，对应k_oncall=1.5，适用于故障率低（λ_node<1/年/POP）且自动化程度高的场景，2人可覆盖7x24 on-call轮班（每人每周5天，2人轮班覆盖14天/月）

## Corrected Claim

SRE人数下限计算：N_sre_min = ceil(10 / 10 * 1.5) = 2人，对应k_oncall=1.5，适用于故障率低（λ_node<1/年/POP）且自动化程度高的场景，2人可覆盖7x24 on-call轮班（每人每周5天，2人轮班覆盖14天/月）

## Evidence

先验知识/题面给定，逻辑校验通过：计算 ceil(1.5)=2 正确；2人轮班覆盖7x24在工程实践中是常见且可行的最低配置（每人每周5天，2人可覆盖10天/周，足以覆盖7天/周的需求），逻辑自洽。
