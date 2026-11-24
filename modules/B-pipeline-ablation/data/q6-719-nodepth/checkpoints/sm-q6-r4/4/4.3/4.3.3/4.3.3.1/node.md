# N358: 混合策略路由决策逻辑中，Core_Zones 的地理边界定义：Core_Zones = {Province_i | Population_i > P_pop_t

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N111

## Claim

混合策略路由决策逻辑中，Core_Zones 的地理边界定义：Core_Zones = {Province_i | Population_i > P_pop_threshold AND GDP_i > Gdp_threshold}，具体阈值需基于用户地理分布数据（如 80% 核心/20% 长尾）反推，确保覆盖 80% 的 DAU 流量。

## Corrected Claim

混合策略路由决策逻辑中，Core_Zones 的地理边界定义：Core_Zones = {Province_i | Population_i > P_pop_threshold AND GDP_i > Gdp_threshold}，具体阈值需基于用户地理分布数据（如 80% 核心/20% 长尾）反推，确保覆盖 80% 的 DAU 流量。

## Evidence

先验知识/题面给定，逻辑校验通过
