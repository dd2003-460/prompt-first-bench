# N82: 定义卖家'价格锚定惯性'的量化指标 $I_{anchor}$ 为卖家设定挂价 $P_{ask}$ 时对'历史最高成交价 $P_{max}$'与'近期成交均价 $

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N23

## Claim

定义卖家'价格锚定惯性'的量化指标 $I_{anchor}$ 为卖家设定挂价 $P_{ask}$ 时对'历史最高成交价 $P_{max}$'与'近期成交均价 $P_{ref}$'的加权系数比。若 $I_{anchor} > 0.7$（即权重主要偏向 $P_{max}$），则判定存在强锚定惯性；若 $I_{anchor} < 0.3$，则判定为理性定价。

## Corrected Claim

定义卖家'价格锚定惯性'的量化指标 $I_{anchor}$ 为卖家设定挂价 $P_{ask}$ 时对'历史最高成交价 $P_{max}$'与'近期成交均价 $P_{ref}$'的加权系数比。若 $I_{anchor} > 0.7$（即权重主要偏向 $P_{max}$），则判定存在强锚定惯性；若 $I_{anchor} < 0.3$，则判定为理性定价。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

second-hand market seller pricing anchor bias historical max vs recent average
