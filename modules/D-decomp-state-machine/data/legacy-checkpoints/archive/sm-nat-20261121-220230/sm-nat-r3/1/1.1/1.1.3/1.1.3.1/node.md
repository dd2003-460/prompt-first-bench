# N110: Frank Copula (θ≈-1.58) 下联合分布在小对象高热度区域 (s<10KB, h>h_90) 的概率密度修正因子 Δf：Δf = f_{S,H}

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N33

## Claim

Frank Copula (θ≈-1.58) 下联合分布在小对象高热度区域 (s<10KB, h>h_90) 的概率密度修正因子 Δf：Δf = f_{S,H}(s,h) / (f_S(s) * f_H(h))，量化负相关对分子中头部小对象权重的提升幅度。

## Corrected Claim

Frank Copula (θ≈-1.58) 下联合分布在小对象高热度区域 (s<10KB, h>h_90) 的概率密度修正因子 Δf：Δf = f_{S,H}(s,h) / (f_S(s) * f_H(h))，量化负相关对分子中头部小对象权重的提升幅度。

## Evidence

先验知识/题面给定，逻辑校验通过：Frank Copula 在 θ<0 时确实表示负相关，且 Δf 的定义符合联合分布与边缘分布比值的数学定义，用于量化相关性对联合概率密度的修正，逻辑自洽。
