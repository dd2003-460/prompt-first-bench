# N207: 临界点移动的绝对值计算公式为 ΔP_critical = P_avg × Δδ，其中 Δδ 需通过演化压力变化 ΔP_evo 与弹性系数 ε_{δ,P} 计算得

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N72

## Claim

临界点移动的绝对值计算公式为 ΔP_critical = P_avg × Δδ，其中 Δδ 需通过演化压力变化 ΔP_evo 与弹性系数 ε_{δ,P} 计算得出：Δδ = ε_{δ,P} × (ΔP_evo / P_evo) × δ_current。基于 N71 的 ε_{δ,P}=0.875，若 P_evo 从 0.5 降至 0.4（ΔP_evo/P_evo = -0.2），则 Δδ = 0.875 × (-0.2) × 0.15 = -0.02625，即临界点下降 2.625% × P_avg。

## Corrected Claim

临界点移动的绝对值计算公式为 ΔP_critical = P_avg × Δδ，其中 Δδ 需通过演化压力变化 ΔP_evo 与弹性系数 ε_{δ,P} 计算得出：Δδ = ε_{δ,P} × (ΔP_evo / P_evo) × δ_current。基于 N71 的 ε_{δ,P}=0.875，若 P_evo 从 0.5 降至 0.4（ΔP_evo/P_evo = -0.2），则 Δδ = 0.875 × (-0.2) × 0.15 = -0.02625，即临界点下降 2.625% × P_avg。

## Evidence

先验知识/题面给定，逻辑校验通过：公式推导符合弹性系数定义，数值计算 0.875 * (-0.2) * 0.15 = -0.02625 准确无误。
