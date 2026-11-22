# N113: 宏观均衡态的稳定性判据：当买家期望效用 E[U_buyer] > 0 且卖家期望收益 E[Payoff_seller] > E[Payoff_exit] 时，均

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N28

## Claim

宏观均衡态的稳定性判据：当买家期望效用 E[U_buyer] > 0 且卖家期望收益 E[Payoff_seller] > E[Payoff_exit] 时，均衡稳定。E[U_buyer] 的计算需包含信号带来的质量溢价估值 V_signal = k * ΔQuality_perception，其中 ΔQuality_perception 为买家对‘快速成交’商品的质量高估幅度（[待核验]，估计 ΔQuality_perception≈10-15%）。

## Corrected Claim

宏观均衡态的稳定性判据：当买家期望效用 E[U_buyer] > 0 且卖家期望收益 E[Payoff_seller] > E[Payoff_exit] 时，均衡稳定。E[U_buyer] 的计算需包含信号带来的质量溢价估值 V_signal = k * ΔQuality_perception，其中 ΔQuality_perception 为买家对‘快速成交’商品的质量高估幅度（具体数值依市场情境而定，通常为正）。

## Evidence

[质询]陈述中关于 ΔQuality_perception 的具体数值估计（10-15%）属于经验性参数，缺乏普遍适用的理论推导或实证支持，且未指明具体市场情境，存在过度具体化风险。 | 先验知识/题面给定，逻辑校验通过；但 ΔQuality_perception 的具体数值范围（10-15%）为经验估计，缺乏来源直接支持，故降级为定性表述。

## Search Query

buyer expected utility signal quality perception heuristic decision making
