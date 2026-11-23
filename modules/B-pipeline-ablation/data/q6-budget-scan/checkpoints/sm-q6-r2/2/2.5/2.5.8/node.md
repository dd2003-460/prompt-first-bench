# N81: N_unique_objects的估算：N_unique_objects = R_daily * (1 - w_repeat) / f_access_per_o

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N15, N16, N17

## Claim

N_unique_objects的估算：N_unique_objects = R_daily * (1 - w_repeat) / f_access_per_object；其中w_repeat为重复访问比例，f_access_per_object为每个对象的平均访问次数；对于图片+短视频平台，N_unique_objects通常与日活用户数同数量级，例如500万DAU对应N_unique_objects ≈ 100万-500万。

## Corrected Claim

N_unique_objects的估算：N_unique_objects = R_daily * (1 - w_repeat) / f_access_per_object；其中w_repeat为重复访问比例，f_access_per_object为每个对象的平均访问次数；对于图片+短视频平台，N_unique_objects通常与日活用户数同数量级，例如500万DAU对应N_unique_objects ≈ 100万-500万。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

CDN unique object count estimation model
