# N138: 有效缓存容量 C_eff 的计算：C_eff = C * K_ρ = 128GB * 1.22 ≈ 156.2GB，该值用于替代原始缓存容量 C 计算 LRU 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N53

## Claim

有效缓存容量 C_eff 的计算：C_eff = C * K_ρ = 128GB * 1.22 ≈ 156.2GB，该值用于替代原始缓存容量 C 计算 LRU 命中率下界，显著提升对头部对象的覆盖能力

## Corrected Claim

有效缓存容量 C_eff 的计算：C_eff = C * K_ρ = 128GB * 1.22 ≈ 156.2GB，该值用于替代原始缓存容量 C 计算 LRU 命中率下界，显著提升对头部对象的覆盖能力

## Evidence

先验知识/题面给定，逻辑校验通过：128 * 1.22 = 156.16，数值计算准确，且符合缓存容量修正因子的常规逻辑。
