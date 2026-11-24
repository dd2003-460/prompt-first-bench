# N204: 混合策略核心区域自建部分带宽成本计算：Cost_Core_Self = Core_Region_Traffic_TB * Self_Built_Price_Pe

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N66

## Claim

混合策略核心区域自建部分带宽成本计算：Cost_Core_Self = Core_Region_Traffic_TB * Self_Built_Price_Per_TB，其中Core_Region_Traffic_TB = 2TB * 0.8 = 1.6TB，Self_Built_Price_Per_TB为自建节点内部服务用户的边际带宽成本（近似为0，因带宽已包含在固定CapEx/OpEx中，仅计算回源部分）

## Corrected Claim

混合策略核心区域自建部分带宽成本计算：Cost_Core_Self = Core_Region_Traffic_TB * Self_Built_Price_Per_TB，其中Core_Region_Traffic_TB = 2TB * 0.8 = 1.6TB，Self_Built_Price_Per_TB为自建节点内部服务用户的边际带宽成本（近似为0，因带宽已包含在固定CapEx/OpEx中，仅计算回源部分）

## Evidence

先验知识/题面给定，逻辑校验通过
