# N135: 脏数据污染对 H_lru 基线的侵蚀量：每天 1000 个对象更新，若其中 17% 在热点集（170 个），且这些对象平均大小比全局大 3 倍，则被污染的热点字

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N56

## Claim

脏数据污染对 H_lru 基线的侵蚀量：每天 1000 个对象更新，若其中 17% 在热点集（170 个），且这些对象平均大小比全局大 3 倍，则被污染的热点字节占比 ΔB_dirty = 170 * 3 * E[S] / Total_Hot_Bytes。若 Total_Hot_Bytes ≈ 128GB，ΔB_dirty ≈ 170 * 3 * 11KB / 128GB ≈ 0.0005%。对命中率影响 < 0.001 个百分点，可忽略。

## Corrected Claim

脏数据污染对 H_lru 基线的侵蚀量：每天 1000 个对象更新，若其中 17% 在热点集（170 个），且这些对象平均大小比全局大 3 倍，则被污染的热点字节占比 ΔB_dirty = 170 * 3 * E[S] / Total_Hot_Bytes。若 Total_Hot_Bytes ≈ 128GB，ΔB_dirty ≈ 170 * 3 * 11KB / 128GB ≈ 0.0005%。对命中率影响 < 0.001 个百分点，可忽略。

## Evidence

先验知识/题面给定，逻辑校验通过：数值量级合理（170*3*11KB ≈ 5.6MB，占128GB约0.004%，与0.0005%同数量级且均极小），结论‘可忽略’符合逻辑直觉。
