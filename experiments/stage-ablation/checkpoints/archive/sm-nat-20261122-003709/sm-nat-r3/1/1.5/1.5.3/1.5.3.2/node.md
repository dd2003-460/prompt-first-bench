# N126: 量化负相关ρ=-0.3对R_byte的非线性放大效应：由于热门对象更小且更频繁，R_byte在ρ=-0.3下相比ρ=0假设值提升约15%-20%，具体提升幅度取

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N40

## Claim

量化负相关ρ=-0.3对R_byte的非线性放大效应：由于热门对象更小且更频繁，R_byte在ρ=-0.3下相比ρ=0假设值提升约15%-20%，具体提升幅度取决于K/N比例，公式为ΔR ≈ -ρ * (E[S|Hot] - E[S|Cold]) / E[S]^2。

## Corrected Claim

量化负相关ρ=-0.3对R_byte存在非线性放大效应：由于热门对象通常更小且更频繁，R_byte在ρ=-0.3下相比ρ=0假设值会有所提升，具体提升幅度取决于K/N比例及对象大小分布，需通过具体模型计算而非简单线性公式确定。

## Evidence

[质询]公式量纲错误：ρ是无量纲相关系数，(E[S|Hot] - E[S|Cold]) / E[S]^2 的量纲是 1/Size，乘积后量纲不为1，无法直接表示R_byte的相对提升比例（无量纲）；且该线性近似公式缺乏理论推导支持，15%-20%的具体数值范围缺乏通用性，高度依赖特定分布参数。 | 先验知识/题面给定，但逻辑校验发现公式量纲不自洽（左端无量纲，右端含1/Size量纲），且具体数值缺乏普适性，故降级。

## Search Query

size popularity negative correlation impact on byte hit rate CDN simulation
