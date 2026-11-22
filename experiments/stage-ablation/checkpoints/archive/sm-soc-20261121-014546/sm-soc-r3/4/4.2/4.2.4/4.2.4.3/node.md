# N298: 下游投影2：心理阻力 λ_resistance 与卖家持有成本 C_hold 正相关，λ_resistance = λ_base + η_c * (C_hold

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N88, N89, N90

## Claim

下游投影2：心理阻力 λ_resistance 与卖家持有成本 C_hold 正相关，λ_resistance = λ_base + η_c * (C_hold / V)，其中 λ_base = 2.0, η_c = 0.5，若持有成本为价值的 10%，则 λ_resistance 增加 0.5 至 2.5。

## Corrected Claim

若持有成本为价值的 10%，则 λ_resistance 增加 0.05 至 2.05。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 λ_resistance = λ_base + η_c * (C_hold / V) 代入 λ_base=2.0, η_c=0.5, C_hold/V=0.1 计算得 2.0 + 0.5*0.1 = 2.05，与陈述中“增加 0.5 至 2.5”存在数值矛盾。但根据 source=knowledge 规则，若视为模型内部定义的参数设定或笔误，需检查逻辑自洽性。此处陈述明确给出了公式和参数，但计算结果 2.05 与结论 2.5 不符。然而，若 η_c 定义为 5.0 或 C_hold/V 为 100% 则成立。重新审视：若 C_hold 是 V 的 10%，即 0.1V，则 η_c * 0.1 = 0.5 => η_c = 5。但题面给定 η_c = 0.5。因此，陈述中的数值推导存在内部矛盾（0.5 * 0.1 = 0.05，而非 0.5）。

## Search Query

holding cost impact on seller price resistance coefficient
