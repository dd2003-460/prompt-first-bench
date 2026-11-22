# N179: 价格调整幅度 ΔP_adjust 的最优策略：卖家为消除偏离度 δ，需将 P_list 降至 P_market * (1 + δ_threshold)，调整幅度

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N61

## Claim

价格调整幅度 ΔP_adjust 的最优策略：卖家为消除偏离度 δ，需将 P_list 降至 P_market * (1 + δ_threshold)，调整幅度为 ΔP_adjust = P_list * (1 - (1 + δ_threshold)/(1 + δ_current))，若 δ_current=20%, δ_threshold=5%，则 ΔP_adjust ≈ 12.5%，需评估该降价幅度对卖家短期利润的冲击是否超过其留存意愿。

## Corrected Claim

价格调整幅度 ΔP_adjust 的最优策略：卖家为消除偏离度 δ，需将 P_list 降至 P_market * (1 + δ_threshold)，调整幅度为 ΔP_adjust = P_list * (1 - (1 + δ_threshold)/(1 + δ_current))，若 δ_current=20%, δ_threshold=5%，则 ΔP_adjust ≈ 12.5%，需评估该降价幅度对卖家短期利润的冲击是否超过其留存意愿。

## Evidence

先验知识/题面给定，逻辑校验通过：数学推导正确（1 - 1.05/1.20 = 0.125），且符合定价调整的基本逻辑。
