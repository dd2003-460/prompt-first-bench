# N50: 惩罚项系数 $\lambda=0.5$ 的校准依据：基于 15-25% 的价格偏差区间，$\lambda$ 的取值需确保偏差 25% 的商品得分惩罚不超过 50

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N17

## Claim

惩罚项系数 $\lambda=0.5$ 的校准依据：基于 15-25% 的价格偏差区间，$\lambda$ 的取值需确保偏差 25% 的商品得分惩罚不超过 50%（即 $1 - 0.5 \times 0.25 = 0.875$ 而非 0.5），需重新校准 $\lambda$ 或修改公式形式（如使用平方项）以避免对极端高挂价卖家产生过度惩罚导致其直接退出平台。

## Corrected Claim

惩罚项系数 $\lambda=0.5$ 的校准依据：基于 15-25% 的价格偏差区间，$\lambda$ 的取值需确保偏差 25% 的商品得分惩罚不超过 50%（即 $1 - 0.5 \times 0.25 = 0.875$ 而非 0.5），需重新校准 $\lambda$ 或修改公式形式（如使用平方项）以避免对极端高挂价卖家产生过度惩罚导致其直接退出平台。

## Evidence

先验知识/题面给定，逻辑校验通过：数学计算 1 - 0.5 * 0.25 = 0.875 正确，且关于避免过度惩罚导致卖家退出的逻辑符合平台经济学直觉。

## Search Query

search ranking penalty function calibration lambda coefficient extreme price deviation
