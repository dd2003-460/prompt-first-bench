# N158: 工作点2（中性价比/标准 LRU）：在标准 LRU 策略下，冷门对象驻留时间极短（T_res_cold ≈ 0），更新后需重新加载。D_cold = 1 - e

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N55

## Claim

工作点2（中性价比/标准 LRU）：在标准 LRU 策略下，冷门对象驻留时间极短（T_res_cold ≈ 0），更新后需重新加载。D_cold = 1 - e^{-λ_upd * 0} ≈ 0，折损可忽略。但需考虑重新加载延迟 L_reload 对有效命中率的影响，有效折损因子 D_eff_cold = 1 - P_stale * (L_reload / T_res_cold)。

## Corrected Claim

工作点2（中性价比/标准 LRU）：在标准 LRU 策略下，冷门对象驻留时间极短（T_res_cold ≈ 0），更新后需重新加载。D_cold = 1 - e^{-λ_upd * 0} ≈ 0，折损可忽略。重新加载延迟 L_reload 会增加访问延迟，但不直接改变数据陈旧度折损因子 D_cold；有效性能需通过延迟模型单独评估，而非通过 D_eff_cold = 1 - P_stale * (L_reload / T_res_cold) 计算。

## Evidence

[质询]公式 D_eff_cold = 1 - P_stale * (L_reload / T_res_cold) 存在量纲和逻辑错误：当 T_res_cold ≈ 0 时，该表达式趋向于无穷大或无定义，无法得出'折损可忽略'的结论；且 L_reload 是时间，T_res_cold 是时间，比值无量纲，但 1 - 无量纲数 作为'折损因子'在物理意义上不成立（折损因子通常应为概率或比例，且不应超过1或为负）。 | 先验知识/题面给定，逻辑校验失败：公式在 T_res_cold ≈ 0 时发散，且量纲/物理意义不自洽。
