# N326: 硬件故障率 p_hw 的修正：考虑到 POP 节点部署环境（如温度、湿度、电压稳定性），实际 MTBF 可能低于实验室值 50000 小时，保守估计 MTBF_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N107

## Claim

硬件故障率 p_hw 的修正：考虑到 POP 节点部署环境（如温度、湿度、电压稳定性），实际 MTBF 可能低于实验室值 50000 小时，保守估计 MTBF_field = 30000 小时，则 p_hw_field = 1 - exp(-720/30000) ≈ 0.0233/月，比原假设高 37%。

## Corrected Claim

硬件故障率 p_hw 的修正：考虑到 POP 节点部署环境（如温度、湿度、电压稳定性），实际 MTBF 可能低于实验室值 50000 小时，保守估计 MTBF_field = 30000 小时，则 p_hw_field = 1 - exp(-720/30000) ≈ 0.0233/月，比原假设高 37%。

## Evidence

先验知识/题面给定，逻辑校验通过：数学计算 1-exp(-720/30000)≈0.0233 正确，且 (0.0233-0.0170)/0.0170≈37% 推导自洽，符合工程保守估计逻辑。
