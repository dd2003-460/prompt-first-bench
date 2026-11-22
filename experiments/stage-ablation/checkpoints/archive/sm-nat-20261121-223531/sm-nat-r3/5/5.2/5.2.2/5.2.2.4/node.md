# N189: LFU 实际增益 $\Delta H_{act}$ 的保守下界：$\Delta H_{act} = H_{LFU}^{act} - H_{LRU}^{act}$

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N66

## Claim

LFU 实际增益 $\Delta H_{act}$ 的保守下界：$\Delta H_{act} = H_{LFU}^{act} - H_{LRU}^{act}$。若 $H_{LRU}^{act} \approx H_{LRU}^{max}$（LRU 无频率估计误差），则 $\Delta H_{act} \approx 0.8 H_{LFU}^{max} - 0.02 - H_{LRU}^{max}$。在 $H_{LFU}^{max} = H_{LRU}^{max} = 100\%$ 时，$\Delta H_{act} \approx -22\%$，表明 LFU 可能劣于 LRU。

## Corrected Claim

LFU 实际增益 ΔH_act 的保守下界需基于具体工作负载特征和缓存替换策略的实证数据确定，不能简单通过 0.8 系数线性推导得出 -22% 的结论

## Evidence

[质询]数值推导存在内部矛盾：若 H_LFU^max = H_LRU^max = 100%，代入公式 0.8*100% - 0.02 - 100% 应得 -22%（即 -0.22），但 0.8 - 0.02 - 1.0 = -0.22 在数学上成立，然而前提假设 H_LRU^act ≈ H_LRU^max 且 H_LFU^act ≈ 0.8 H_LFU^max 缺乏理论依据，0.8 系数来源不明，属于经验性假设而非第一性原理推导。 | 先验知识/题面给定，逻辑校验未通过：0.8 系数无理论支撑，且将 H_LFU^act 简化为 0.8 H_LFU^max 缺乏依据，导致推导链条断裂
