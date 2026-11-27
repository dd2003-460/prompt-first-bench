# N180: 工作点3（高溢价风险边界）：P_ask = P_market * 1.3，ΔV_signal = 0.2 * (0.3 * P_market) = 0.06 *

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N55

## Claim

工作点3（高溢价风险边界）：P_ask = P_market * 1.3，ΔV_signal = 0.2 * (0.3 * P_market) = 0.06 * P_market，V_item = V_base + 0.06 * P_market；但触发风险感知修正项 δ_risk = 0.1 * (P_ask/P_market - 1)^2 = 0.03，净感知价值 V_net = V_item - δ_risk * P_market = V_base + 0.03 * P_market，低于工作点2，导致成交概率 P_deal 下降 15%。

## Corrected Claim

工作点3（高溢价风险边界）：P_ask = P_market * 1.3，ΔV_signal = 0.06 * P_market，V_item = V_base + 0.06 * P_market；触发风险感知修正项 δ_risk = 0.03，净感知价值 V_net = V_base + 0.03 * P_market，低于工作点2，导致成交概率 P_deal 显著下降（具体幅度取决于模型参数，此处估算为15%）。

## Evidence

[质询]该陈述包含具体的经验性参数（如风险感知修正系数0.1、成交概率下降15%），这些并非数学恒等式或第一性原理可推导的必然结果，而是依赖于特定模型假设或经验数据。在缺乏来源支持的情况下，无法验证这些具体数值（特别是15%的下降幅度）的准确性。 | 经验事实，逻辑自洽但缺来源支持。数学计算部分（0.06-0.03=0.03）正确，但具体参数和最终概率变化幅度属于经验模型输出，无外部证据验证。

## Search Query

price premium risk perception buyer decision making second-hand goods
