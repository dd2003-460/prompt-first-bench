# N257: 计算ρ=-0.3下的缓存覆盖对象数 K_eff：由于热门对象更小，头部对象平均大小 E[S|Top K] ≈ 8.5KB（N97），则 K_eff = 128G

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N96

## Claim

计算ρ=-0.3下的缓存覆盖对象数 K_eff：由于热门对象更小，头部对象平均大小 E[S|Top K] ≈ 8.5KB（N97），则 K_eff = 128GB / 8.5KB ≈ 154,150。同样受限于 N=100,000，故 K_eff_eff = 100,000。结论：在 N=100,000 规模下，ρ 的相关性不改变缓存覆盖上限，瓶颈仍为对象总数。

## Corrected Claim

计算ρ=-0.3下的缓存覆盖对象数 K_eff：由于热门对象更小，头部对象平均大小 E[S|Top K] ≈ 8.5KB（N97），则 K_eff = 128GB / 8.5KB ≈ 154,150。同样受限于 N=100,000，故 K_eff_eff = 100,000。结论：在 N=100,000 规模下，ρ 的相关性不改变缓存覆盖上限，瓶颈仍为对象总数。

## Evidence

先验知识/题面给定，逻辑校验通过：128GB/8.5KB ≈ 154,150 > 100,000，取最小值逻辑自洽
