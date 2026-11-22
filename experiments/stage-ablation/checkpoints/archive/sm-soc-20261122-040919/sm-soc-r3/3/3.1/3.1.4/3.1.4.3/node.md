# N251: 下游投影2：新信号权重 w_signal_new 的计算。w_signal_new = w_signal_old * (1 + β * ΔCTR)。若 w_si

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N68

## Claim

下游投影2：新信号权重 w_signal_new 的计算。w_signal_new = w_signal_old * (1 + β * ΔCTR)。若 w_signal_old = 1.0，β=0.1，ΔCTR=-0.05（下降），则 w_signal_new = 0.995。需评估该微小变化对整体流量分配的影响。

## Corrected Claim

下游投影2：新信号权重 w_signal_new 的计算。w_signal_new = w_signal_old * (1 + β * ΔCTR)。若 w_signal_old = 1.0，β=0.1，ΔCTR=-0.05（下降），则 w_signal_new = 0.995。需评估该微小变化对整体流量分配的影响。

## Evidence

先验知识/题面给定，逻辑校验通过：1.0 * (1 + 0.1 * -0.05) = 1.0 * 0.995 = 0.995，计算无误。
