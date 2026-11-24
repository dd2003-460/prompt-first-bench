# N371: Zipf 指数 α 的精确估计需通过幂律拟合日志数据获得，若缺乏数据，采用保守值 α=0.8 进行敏感性分析，此时 Hit_Rate 对 K 的变化敏感度为 d

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N129

## Claim

Zipf 指数 α 的精确估计需通过幂律拟合日志数据获得，若缺乏数据，采用保守值 α=0.8 进行敏感性分析，此时 Hit_Rate 对 K 的变化敏感度为 d(Hit_Rate)/dK ≈ -α/K^(α+1)。

## Corrected Claim

Zipf 指数 α 的精确估计需通过幂律拟合日志数据获得，若缺乏数据，采用保守值 α=0.8 进行敏感性分析，此时 Hit_Rate 对 K 的变化敏感度为 d(Hit_Rate)/dK ≈ -α/K^(α+1)。

## Evidence

先验知识/题面给定，逻辑校验通过：幂律分布下命中率对缓存大小K的导数形式符合微积分基本定理及Zipf分布性质，量纲与符号（负相关）合理。

## Search Query

Zipf exponent estimation content distribution
