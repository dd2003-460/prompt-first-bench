# N259: P_LFU_miss_on_hot 的噪声下界：LFU 对热门对象的 miss 率受计数器噪声影响，其下界由计数误差导致，P_LFU_miss_on_hot >

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N89

## Claim

P_LFU_miss_on_hot 的噪声下界：LFU 对热门对象的 miss 率受计数器噪声影响，其下界由计数误差导致，P_LFU_miss_on_hot >= P_noise = P(Count_LFU < Threshold | True_Rate = r_i)，在 r_i 较高时，该值趋近于 0，但比 LRU 的 miss 率多出一个与计数器更新延迟相关的项 δ_lag ≈ T_update / τ_residence。

## Corrected Claim

P_LFU_miss_on_hot 的噪声下界：LFU 对热门对象的 miss 率受计数器噪声影响，其下界由计数误差导致，P_LFU_miss_on_hot >= P_noise = P(Count_LFU < Threshold | True_Rate = r_i)，在 r_i 较高时，该值趋近于 0，但比 LRU 的 miss 率多出一个与计数器更新延迟相关的项 δ_lag ≈ T_update / τ_residence。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LFU miss rate counter noise lower bound update lag
