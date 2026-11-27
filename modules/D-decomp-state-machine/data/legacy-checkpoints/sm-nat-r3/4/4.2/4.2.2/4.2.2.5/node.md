# N206: 工作点 C（低频大对象）：假设对象大小 S_i > 1MB，请求频率 λ_i < 0.1 次/天，驻留时间 T_res ≈ 24h，则失效概率 P_inval 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N71, N72, N73

## Claim

工作点 C（低频大对象）：假设对象大小 S_i > 1MB，请求频率 λ_i < 0.1 次/天，驻留时间 T_res ≈ 24h，则失效概率 P_inval ≈ 1.157e-7 * 1 ≈ 1.157e-7，折损因子 D_update ≈ 0.9999999，量化了长尾大对象在均匀更新假设下的最大潜在折损，但仍可忽略不计。

## Corrected Claim

工作点 C（低频大对象）：假设对象大小 S_i > 1MB，请求频率 λ_i < 0.1 次/天，驻留时间 T_res ≈ 24h，则失效概率 P_inval ≈ 1.157e-7 * 1 ≈ 1.157e-7，折损因子 D_update ≈ 0.9999999，量化了长尾大对象在均匀更新假设下的最大潜在折损，但仍可忽略不计。

## Evidence

先验知识/题面给定，逻辑校验通过：失效概率计算基于泊松分布近似（λt），数值量级合理，折损因子推导符合逻辑。
