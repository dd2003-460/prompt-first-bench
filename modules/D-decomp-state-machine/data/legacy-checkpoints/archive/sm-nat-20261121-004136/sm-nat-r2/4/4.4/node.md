# N18: 更新率对命中率的影响机制：当对象更新时，旧版本从缓存驱逐，新版本需重新获取；若更新对象占缓存比例高，则额外带宽开销 ≈ λ_update * R * E[Siz

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

更新率对命中率的影响机制：当对象更新时，旧版本从缓存驱逐，新版本需重新获取；若更新对象占缓存比例高，则额外带宽开销 ≈ λ_update * R * E[Size_of_updated_objects]，其中 E[Size_of_updated_objects] 受热度与大小负相关 ρ=-0.3 影响（热门对象小，更新代价低）。

## Corrected Claim

更新率对命中率的影响机制：当对象更新时，旧版本从缓存驱逐，新版本需重新获取；若更新对象占缓存比例高，则额外带宽开销 ≈ λ_update * R * E[Size_of_updated_objects]，其中 E[Size_of_updated_objects] 受热度与大小负相关 ρ=-0.3 影响（热门对象小，更新代价低）。

## Evidence

先验知识/题面给定，逻辑校验通过
