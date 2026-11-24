# N326: 故障影响范围修正系数 F_impact：全平台故障时F_impact=1.0；若为单POP故障（如自建策略），F_impact = Traffic_Share_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N95

## Claim

故障影响范围修正系数 F_impact：全平台故障时F_impact=1.0；若为单POP故障（如自建策略），F_impact = Traffic_Share_i ≈ 0.1（10个POP均匀分布），则实际每分钟损失降至50元，这决定了冗余投资的成本效益边界。

## Corrected Claim

故障影响范围修正系数 F_impact：全平台故障时F_impact=1.0；若为单POP故障（如自建策略），F_impact = Traffic_Share_i ≈ 0.1（10个POP均匀分布），则实际每分钟损失降至50元，这决定了冗余投资的成本效益边界。

## Evidence

先验知识/题面给定，逻辑校验通过：10个POP均匀分布时单POP流量占比为1/10=0.1，全平台损失500元（隐含）则单POP损失50元，数学推导自洽。
