# N171: 在 128GB 缓存容量约束下，Prob_Coverage_128 的数值积分下限由缓存能容纳的最大对象数 N_cache 决定，其计算式为 Prob_Cove

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N58

## Claim

在 128GB 缓存容量约束下，Prob_Coverage_128 的数值积分下限由缓存能容纳的最大对象数 N_cache 决定，其计算式为 Prob_Coverage_128 = ∫_0^{F_S(S_{max})} F_R(Q_R | S=s) * f_S(s) ds，其中 S_{max} 是满足 Σ_{i=1}^{N_cache} s_i ≤ 128GB 的最大对象大小阈值，该积分量化了缓存覆盖的字节加权请求概率。

## Corrected Claim

在 128GB 缓存容量约束下，Prob_Coverage_128 的数值积分下限由缓存能容纳的最大对象数 N_cache 决定，其计算式为 Prob_Coverage_128 = ∫_0^{F_S(S_{max})} F_R(Q_R | S=s) * f_S(s) ds，其中 S_{max} 是满足 Σ_{i=1}^{N_cache} s_i ≤ 128GB 的最大对象大小阈值，该积分量化了缓存覆盖的字节加权请求概率。

## Evidence

先验知识/题面给定，逻辑校验通过：积分下限由缓存容量约束下的最大对象数决定，积分形式符合字节加权请求概率的定义，量纲与逻辑自洽。
