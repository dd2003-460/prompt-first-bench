# N75: N21 中 0.82 的下界对应于‘请求命中率’而非‘字节命中率’：在字节命中率口径下，需计算加权项 Σ(R_i*S_i)/Σ(R_j*S_j)，由于热门对象通

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N21

## Claim

N21 中 0.82 的下界对应于‘请求命中率’而非‘字节命中率’：在字节命中率口径下，需计算加权项 Σ(R_i*S_i)/Σ(R_j*S_j)，由于热门对象通常较小（ρ<0），字节命中率下界通常低于请求命中率下界 0.82。

## Corrected Claim

N21 中 0.82 的下界对应于‘请求命中率’而非‘字节命中率’：在字节命中率口径下，需计算加权项 Σ(R_i*S_i)/Σ(R_j*S_j)，由于热门对象通常较小（ρ<0），字节命中率下界通常低于请求命中率下界 0.82。

## Evidence

先验知识/题面给定，逻辑校验通过：在缓存系统中，若热门对象尺寸较小（ρ<0，即尺寸与热度负相关），字节命中率确实通常低于请求命中率，因为小对象虽然命中率高但贡献的字节数少，导致加权后的字节命中率下界低于请求命中率下界。

## Search Query

byte hit ratio vs request hit ratio Pareto distribution
