# N137: 在大对象主导场景（工作点 3），P_invalidate = 63.2% 假设所有驻留对象具有相同的更新率 u=1%/天。实际上，由于大小-热度负相关，大对象往

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N61

## Claim

在大对象主导场景（工作点 3），P_invalidate = 63.2% 假设所有驻留对象具有相同的更新率 u=1%/天。实际上，由于大小-热度负相关，大对象往往热度较低，其驻留时间 T_res 更长，导致有效更新率 u_eff = u * (T_obj/T_res) 降低。修正后的失效概率 P_invalidate_corr = 1 - exp(-T_res / T_update_avg)，其中 T_update_avg 需根据大对象子集的更新分布（可能低于 1%/天）重新估算。若大对象更新率仅为 0.1%/天，则 P_invalidate 将显著低于 63.2%。

## Corrected Claim

在大对象主导场景（工作点 3），P_invalidate = 63.2% 假设所有驻留对象具有相同的更新率 u=1%/天。实际上，由于大小-热度负相关，大对象往往热度较低，其驻留时间 T_res 更长，导致有效更新率 u_eff = u * (T_obj/T_res) 降低。修正后的失效概率 P_invalidate_corr = 1 - exp(-T_res / T_update_avg)，其中 T_update_avg 需根据大对象子集的更新分布（可能低于 1%/天）重新估算。若大对象更新率仅为 0.1%/天，则 P_invalidate 将显著低于 63.2%。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 P=1-exp(-T_res/T_update) 符合指数分布失效模型，且大对象热度低导致更新率降低从而降低失效概率的推导符合逻辑直觉。

## Search Query

cache invalidation rate heterogeneous object update frequency
