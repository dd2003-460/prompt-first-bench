# N17: 匹配算法调整干预：将推荐权重从‘最新上架’调整为‘性价比指数’ $CPI = \frac{MarketAvgPrice}{AskPrice} \times Qu

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

匹配算法调整干预：将推荐权重从‘最新上架’调整为‘性价比指数’ $CPI = \frac{MarketAvgPrice}{AskPrice} \times QualityScore$。最小干预定义为仅调整排序算法中的 $CPI$ 权重系数 $w$ 从 0.1 提升至 0.3。

## Corrected Claim

匹配算法调整干预：将推荐权重从‘最新上架’调整为‘性价比指数’ $CPI = \frac{MarketAvgPrice}{AskPrice} \times QualityScore$。最小干预定义为仅调整排序算法中的 $CPI$ 权重系数 $w$ 从 0.1 提升至 0.3。

## Evidence

先验知识/题面给定，逻辑校验通过：CPI公式量纲合理（价格比无量纲乘以质量分），权重调整0.1至0.3符合最小干预定义，无内部矛盾。

## Search Query

recommendation algorithm weight adjustment cost performance index e-commerce platform
