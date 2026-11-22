# N150: 中间过渡对象（100KB < S < 1MB）的缓存容量竞争强度指标：竞争比 R_comp = (N_mid / C_mid_eff) * (λ_mid_avg

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N67

## Claim

中间过渡对象（100KB < S < 1MB）的缓存容量竞争强度指标：竞争比 R_comp = (N_mid / C_mid_eff) * (λ_mid_avg / λ_global_avg)，其中 N_mid 是该区间对象数，C_mid_eff 是 LRU 分配给该区间的实际有效缓存字节数，λ_mid_avg 是该区间平均请求频率。R_comp > 1 表明容量竞争主导折损，需计算 R_comp 在 C=128GB 下的具体值以验证 '15% 折损贡献' 的来源。

## Corrected Claim

中间过渡对象（100KB < S < 1MB）的缓存容量竞争强度指标：竞争比 R_comp = (N_mid / C_mid_eff) * (λ_mid_avg / λ_global_avg)，其中 N_mid 是该区间对象数，C_mid_eff 是 LRU 分配给该区间的实际有效缓存字节数，λ_mid_avg 是该区间平均请求频率。R_comp > 1 表明容量竞争主导折损，需计算 R_comp 在 C=128GB 下的具体值以验证 '15% 折损贡献' 的来源。

## Evidence

先验知识/题面给定，逻辑校验通过
