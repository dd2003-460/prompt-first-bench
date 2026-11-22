# N277: 2x RTX 4090 3 年故障成本 C_failure_2x4090 估算：基于 P_fail_sys ≈ 24.2%（假设 MTBF=100k），单次故障

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N80

## Claim

2x RTX 4090 3 年故障成本 C_failure_2x4090 估算：基于 P_fail_sys ≈ 24.2%（假设 MTBF=100k），单次故障平均修复成本（含更换卡/主板/电源）$2,500 + 停机损失（重新部署 4h * $50/h = $200），期望成本 = 24.2% * ($2,500 + $200) ≈ $653。

## Corrected Claim

2x RTX 4090 3 年故障成本 C_failure_2x4090 估算：基于 P_fail_sys ≈ 24.2%（假设 MTBF=100k），单次故障平均修复成本（含更换卡/主板/电源）$2,500 + 停机损失（重新部署 4h * $50/h = $200），期望成本 = 24.2% * ($2,500 + $200) ≈ $653。

## Evidence

[质询]MTBF=100k小时（约11.4年）对于双卡系统而言假设过于乐观，实际故障率可能更高，导致期望成本被低估；但作为估算模型，逻辑结构本身无误。 | 先验知识/题面给定，逻辑校验通过：期望成本计算公式 E[C] = P_fail * (C_repair + C_downtime) 正确，数值代入 0.242 * (2500 + 200) = 653.4 计算无误，量级合理。
