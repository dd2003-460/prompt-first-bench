# N616: 边际递减函数 ΔL_per_pop(N) = ΔL_base * exp(-N / N_decay) 的失效条件：当 N > N_decay 时，指数衰减模型预

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N203

## Claim

边际递减函数 ΔL_per_pop(N) = ΔL_base * exp(-N / N_decay) 的失效条件：当 N > N_decay 时，指数衰减模型预测的 ΔL_per_pop 趋近于 0，但实际中由于用户分布不均匀（东部高密度、西部低密度），新增 POP 在东部密集区的边际收益显著高于西部稀疏区，需引入空间权重修正项 W_region

## Corrected Claim

边际递减函数 ΔL_per_pop(N) = ΔL_base * exp(-N / N_decay) 的失效条件：当 N > N_decay 时，指数衰减模型预测的 ΔL_per_pop 趋近于 0，但实际中由于用户分布不均匀（东部高密度、西部低密度），新增 POP 在东部密集区的边际收益显著高于西部稀疏区，需引入空间权重修正项 W_region

## Evidence

先验知识/题面给定，逻辑校验通过：指数衰减模型在N>N_decay时确实趋近于0，而地理分布不均导致边际收益差异是空间经济学常识，引入空间权重修正项符合逻辑。

## Search Query

CDN POP placement user density non-uniform marginal benefit
