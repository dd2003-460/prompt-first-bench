# N179: 人均日请求数 R_per_user 的高频激进估计：R_high = 50 次/人/天，对应总请求数 R_total_high = 5,000,000 × 50

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N51

## Claim

人均日请求数 R_per_user 的高频激进估计：R_high = 50 次/人/天，对应总请求数 R_total_high = 5,000,000 × 50 = 250,000,000 次/天，适用于重度用户或高频刷新场景

## Corrected Claim

人均日请求数 R_per_user 的高频激进估计：R_high = 50 次/人/天，对应总请求数 R_total_high = 5,000,000 × 50 = 250,000,000 次/天，适用于重度用户或高频刷新场景

## Evidence

父节点级核验未通过：不完备（子节点1关注请求行为的内部构成（Browse/Interaction/Background），子节点2关注该流量假设与后端资源（回源量/缓存命中率）的一致性校验。两者维度不同（微观行为 vs 宏观系统约束），无重叠且无矛盾，故正交。然而，父节点仅定义了R_high的数值及其适用场景，未明确提及需要验证其内部构成或与其系统容量（如Origin Traffic）的约束关系。因此，子节点引入了父节点未涵盖的新维度（行为分解和系统一致性），导致父节点定义过于单薄，无法完全覆盖子节点所隐含的前提条件，完备性不足。）

## Search Query

heavy user daily request count video streaming platform
