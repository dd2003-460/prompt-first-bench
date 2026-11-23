# N84: 失效条件量化：若市场价格波动系数 CV_price > 0.15 或电力单价 > $0.15/kWh，则 B1 区间推荐方案 TCO 上升 >20%，需降级为 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N23

## Claim

失效条件量化：若市场价格波动系数 CV_price > 0.15 或电力单价 > $0.15/kWh，则 B1 区间推荐方案 TCO 上升 >20%，需降级为 CPU+GPU 混合方案或等待价格回调

## Corrected Claim

失效条件量化：若市场价格波动系数 CV_price > 0.15 或电力单价 > $0.15/kWh，则 B1 区间推荐方案 TCO 上升 >20%，需降级为 CPU+GPU 混合方案或等待价格回调

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

GPU price volatility 2024, electricity cost sensitivity LLM inference TCO
