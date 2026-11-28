# N144: C_hitl 对阈值 τ 的敏感性分析：dC_hitl/dτ = -T_human * R_hourly * d(IR_auto)/dτ；由于 IR_auto 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N50

## Claim

C_hitl 对阈值 τ 的敏感性分析：dC_hitl/dτ = -T_human * R_hourly * d(IR_auto)/dτ；由于 IR_auto 随 τ 降低而减小（拦截减少，人工介入增多），C_hitl 随 τ 降低而单调递增；需计算 τ 从 0.3 变到 0.5 时 C_hitl 的相对变化百分比 ΔC%/Δτ。

## Corrected Claim

C_hitl 对阈值 τ 的敏感性分析：dC_hitl/dτ = -T_human * R_hourly * d(IR_auto)/dτ；由于 IR_auto 随 τ 降低而减小（拦截减少，人工介入增多），C_hitl 随 τ 降低而单调递增；需计算 τ 从 0.3 变到 0.5 时 C_hitl 的相对变化百分比 ΔC%/Δτ。

## Evidence

先验知识/题面给定，逻辑校验通过：成本函数对阈值的导数符号与业务逻辑（阈值降低导致自动拦截率下降、人工介入增加从而成本上升）一致，数学推导自洽。

## Search Query

cost sensitivity analysis threshold parameter human intervention cost
