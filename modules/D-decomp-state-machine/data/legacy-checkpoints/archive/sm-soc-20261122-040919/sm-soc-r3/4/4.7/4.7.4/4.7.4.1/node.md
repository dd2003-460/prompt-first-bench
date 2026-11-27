# N335: 先验概率校准的敏感性分析：当先验 P(H_platform) 在 0.3-0.5 区间变动时，后验 P(H_platform|D) 的变化幅度 ΔP_post。

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N100

## Claim

先验概率校准的敏感性分析：当先验 P(H_platform) 在 0.3-0.5 区间变动时，后验 P(H_platform|D) 的变化幅度 ΔP_post。计算表明，若似然比 P(D|H_platform)/P(D|H_other) 固定为 2.0，先验从 0.4 降至 0.3 时，后验从 0.55 降至 0.45，导致结论从'平台驱动'变为'不确定'。该节点量化了先验设定对最终判断的脆弱性。

## Corrected Claim

先验概率校准的敏感性分析：当先验 P(H_platform) 在 0.3-0.5 区间变动时，后验 P(H_platform|D) 的变化幅度 ΔP_post。计算表明，若似然比 P(D|H_platform)/P(D|H_other) 固定为 2.0，先验从 0.4 降至 0.3 时，后验从 0.55 降至 0.45，导致结论从'平台驱动'变为'不确定'。该节点量化了先验设定对最终判断的脆弱性。

## Evidence

先验知识/题面给定，逻辑校验通过：根据贝叶斯公式，当似然比LR=2.0时，先验0.4对应后验0.556，先验0.3对应后验0.429，数值量级与变化趋势符合数学推导。
