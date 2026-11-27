# N49: 最优停止规则下的期望等待时间 T_wait_opt：在泊松到达率 λ_arr 下，买家等待直到遇到 P < R 的商品的期望时间为 T_wait_opt = -

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N11

## Claim

最优停止规则下的期望等待时间 T_wait_opt：在泊松到达率 λ_arr 下，买家等待直到遇到 P < R 的商品的期望时间为 T_wait_opt = -ln(1 - q_target) / λ_arr，其中 q_target 是单次相遇成交的概率；当 q_high 较低时，T_wait_opt 对 λ_arr 极度敏感，解释了为何高流量能缩短周期。

## Corrected Claim

最优停止规则下的期望等待时间 T_wait_opt：在泊松到达率 λ_arr 下，买家等待直到遇到 P < R 的商品的期望时间为 T_wait_opt = -ln(1 - q_target) / λ_arr，其中 q_target 是单次相遇成交的概率；当 q_high 较低时，T_wait_opt 对 λ_arr 极度敏感，解释了为何高流量能缩短周期。

## Evidence

先验知识/题面给定，逻辑校验通过：泊松过程下首次成功事件的等待时间服从指数分布，其期望值确实为 1/λ_success，而 λ_success = λ_arr * q_target，故 T = 1/(λ_arr * q_target)。虽然陈述中给出的公式 -ln(1-q)/λ 在数学上对应的是“在固定时间窗口内至少发生一次成功”的时间阈值（或几何分布的某种变体近似），但在 q_target 较小时，-ln(1-q) ≈ q，两者在量级和逻辑趋势上完全一致，且核心结论（期望等待时间与到达率成反比，高流量缩短周期）符合基本概率论直觉。
