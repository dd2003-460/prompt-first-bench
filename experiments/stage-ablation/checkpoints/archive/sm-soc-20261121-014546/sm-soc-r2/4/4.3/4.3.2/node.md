# N90: 高挂价卖家最终成交价 P_final 的下降幅度计算公式：ΔP_pct = 1 - (P_anchor / P_ask_old) × (1 + (1/ε_s) 

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N21, N22, N23

## Claim

高挂价卖家最终成交价 P_final 的下降幅度计算公式：ΔP_pct = 1 - (P_anchor / P_ask_old) × (1 + (1/ε_s) × ΔQ_pct)，其中 ε_s 为供给价格弹性（假设与需求弹性同区间0.5-0.8），ΔQ_pct 为成交量变化率（假设5-10%）。

## Corrected Claim

高挂价卖家最终成交价 P_final 的下降幅度可近似估算为：ΔP_pct ≈ 1 - (P_anchor / P_ask_old) × (1 + (1/ε_s) × ΔQ_pct)，其中 ε_s 为供给价格弹性（假设0.5-0.8），ΔQ_pct 为成交量变化率（假设5-10%）。注意：此为基于特定假设的近似估算模型，非严格经济学恒等式。

## Evidence

[质询]公式推导存在逻辑跳跃：该公式隐含假设价格变动完全由成交量变化通过弹性传导引起，且忽略了锚定效应（P_anchor）本身对成交价的独立影响或非线性调整机制；此外，将供给弹性直接用于推导卖家最终成交价的下降幅度在微观经济学上缺乏严谨的因果链条，通常成交价由供需均衡决定，而非单纯由供给弹性乘以成交量变化得出。 | 先验知识/题面给定，逻辑校验通过（量纲一致，数值量级合理），但公式推导过程存在简化假设，缺乏外部来源直接支持其作为通用计算公式的准确性。

## Search Query

supply price elasticity seller response to price transparency
