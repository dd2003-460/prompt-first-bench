# N191: 容量修正因子 η_cap 的分母项 Σ_{i>K} s_i * (λ_i/λ_K) 代表冷大对象对缓存空间的“虚拟占用”或竞争权重，其中 s_i 为对象 i 的

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N83

## Claim

容量修正因子 η_cap 的分母项 Σ_{i>K} s_i * (λ_i/λ_K) 代表冷大对象对缓存空间的“虚拟占用”或竞争权重，其中 s_i 为对象 i 的大小，λ_i 为对象 i 的访问频率，λ_K 为第 K 个对象的访问频率，需通过积分近似 Σ_{i=K+1}^{N} s_i * (i/K)^β 计算。

## Corrected Claim

容量修正因子 η_cap 的分母项 Σ_{i>K} s_i * (λ_i/λ_K) 代表冷大对象对缓存空间的“虚拟占用”或竞争权重，其中 s_i 为对象 i 的大小，λ_i 为对象 i 的访问频率，λ_K 为第 K 个对象的访问频率，需通过积分近似 Σ_{i=K+1}^{N} s_i * (i/K)^β 计算。

## Evidence

先验知识/题面给定，逻辑校验通过
