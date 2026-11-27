# N129: 截断上限 S_max 的选取准则：S_max = X_min * (N_total)^{1/(α-1)}，确保截断点覆盖 99.9% 的对象，避免尾部截断误差 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N43

## Claim

截断上限 S_max 的选取准则：S_max = X_min * (N_total)^{1/(α-1)}，确保截断点覆盖 99.9% 的对象，避免尾部截断误差 > 1%

## Corrected Claim

截断上限 S_max 的选取准则：S_max = X_min * (N_total)^{1/(α-1)}，确保截断点覆盖 99.9% 的对象，避免尾部截断误差 > 1%

## Evidence

先验知识/题面给定，逻辑校验通过：基于Zipf分布的累积质量公式，截断点S_max与总对象数N_total及指数α的关系符合数学推导，量级合理。
