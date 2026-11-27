# N371: TCO 交叉点吞吐量阈值 T_break-even 的计算公式：设硬件差价 ΔC_hw = C_hw_L4 - C_hw_4090，年电力节省 ΔC_power

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N116

## Claim

TCO 交叉点吞吐量阈值 T_break-even 的计算公式：设硬件差价 ΔC_hw = C_hw_L4 - C_hw_4090，年电力节省 ΔC_power = C_power_4090 - C_power_L4，则 L4 方案在 N 年 TCO 内优于 4090 的条件为 ΔC_hw < N * ΔC_power + N * (T_4090 - T_L4) * V_time，其中 V_time 为每 token 的时间价值。若忽略时间价值，仅考虑电力，交叉点年运行小时数 T_hours_be = ΔC_hw / (ΔP * E_price)。

## Corrected Claim

TCO 交叉点吞吐量阈值 T_break-even 的计算公式：设硬件差价 ΔC_hw = C_hw_L4 - C_hw_4090，年电力节省 ΔC_power = C_power_4090 - C_power_L4，则 L4 方案在 N 年 TCO 内优于 4090 的条件为 ΔC_hw < N * ΔC_power + N * (T_4090 - T_L4) * V_time，其中 V_time 为每 token 的时间价值。若忽略时间价值，仅考虑电力，交叉点年运行小时数 T_hours_be = ΔC_hw / (ΔP * E_price)。

## Evidence

先验知识/题面给定，逻辑校验通过
