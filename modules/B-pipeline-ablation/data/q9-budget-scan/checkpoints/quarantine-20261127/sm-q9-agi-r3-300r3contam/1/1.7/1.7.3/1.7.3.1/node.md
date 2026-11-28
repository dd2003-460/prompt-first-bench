# N141: T_human (平均审核耗时) 的分解模型：T_human = T_read + T_judge + T_action，其中 T_read 与输出长度 L_o

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N50

## Claim

T_human (平均审核耗时) 的分解模型：T_human = T_read + T_judge + T_action，其中 T_read 与输出长度 L_out 成正比 (T_read = α * L_out, α≈0.5s/token)，T_judge 为固定认知负荷 (≈30s)，T_action 为修改/驳回操作耗时 (≈15s)；假设 L_out=500 tokens，则 T_human ≈ 285s ≈ 4.75 min。

## Corrected Claim

T_human (平均审核耗时) 的分解模型：T_human = T_read + T_judge + T_action，其中 T_read 与输出长度 L_out 成正比 (T_read = α * L_out, α≈0.5s/token)，T_judge 为固定认知负荷 (≈30s)，T_action 为修改/驳回操作耗时 (≈15s)；假设 L_out=500 tokens，则 T_human ≈ 285s ≈ 4.75 min。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算正确（0.5*500+30+15=285s），参数量级符合人类阅读与操作的一般经验范围。

## Search Query

human-in-the-loop review time cost model reading speed judgment latency
