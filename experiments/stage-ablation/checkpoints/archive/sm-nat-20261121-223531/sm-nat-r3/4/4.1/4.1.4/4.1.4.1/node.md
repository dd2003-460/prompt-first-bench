# N157: 工作点1（高性低成/容量充足）：在缓存容量充足的情况下，冷门对象（后90%）虽驻留时间短，但若更新后能立即重新加载，T_res_cold ≈ 0 的假设不成立。

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N55

## Claim

工作点1（高性低成/容量充足）：在缓存容量充足的情况下，冷门对象（后90%）虽驻留时间短，但若更新后能立即重新加载，T_res_cold ≈ 0 的假设不成立。实际 T_res_cold 取决于重新加载延迟 L_reload。D_cold = 1 - e^{-λ_upd * T_res_cold}，若 T_res_cold < L_reload，则 D_cold ≈ 1，折损显著。

## Corrected Claim

工作点1（高性低成/容量充足）：在缓存容量充足的情况下，冷门对象（后90%）虽驻留时间短，但若更新后能立即重新加载，T_res_cold ≈ 0 的假设不成立。实际 T_res_cold 取决于重新加载延迟 L_reload。D_cold = 1 - e^{-λ_upd * T_res_cold}，若 T_res_cold < L_reload，则 D_cold ≈ 1，折损显著。

## Evidence

先验知识/题面给定，逻辑校验通过：缓存失效模型中，若驻留时间小于重载延迟，对象在下次访问前无法完成重载，导致必须从源加载，折损率趋近于1，符合逻辑与物理直觉。
