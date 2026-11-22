# N28: 演化定向压力量化：在二手市场，买家面临‘柠檬市场’风险，演化形成的‘质量筛选压力’导致买家对高价商品的容忍阈值 $T_{tol}$ 并非固定值，而是随近期同类商

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

演化定向压力量化：在二手市场，买家面临‘柠檬市场’风险，演化形成的‘质量筛选压力’导致买家对高价商品的容忍阈值 $T_{tol}$ 并非固定值，而是随近期同类商品平均成交价 $P_{ref}$ 动态调整。具体公式为 $T_{tol} = P_{ref} 	imes (1 + \beta \cdot \sigma_{quality})$，其中 $\beta$ 为质量不确定性系数。当卖家挂价 $P_{ask}$ 落入 $[P_{ref}, T_{tol}]$ 区间时，买家将其视为‘高质量信号’而非‘过高价格’，从而维持高咨询率并缩短成交周期 $T_{sale}$。

## Corrected Claim

演化定向压力量化：在二手市场，买家面临‘柠檬市场’风险，演化形成的‘质量筛选压力’导致买家对高价商品的容忍阈值 $T_{tol}$ 并非固定值，而是随近期同类商品平均成交价 $P_{ref}$ 动态调整。具体公式为 $T_{tol} = P_{ref} 	imes (1 + \beta \cdot \sigma_{quality})$，其中 $\beta$ 为质量不确定性系数。当卖家挂价 $P_{ask}$ 落入 $[P_{ref}, T_{tol}]$ 区间时，买家将其视为‘高质量信号’而非‘过高价格’，从而维持高咨询率并缩短成交周期 $T_{sale}$。

## Evidence

检索失败: no sources from any channel (all 5 failed)
