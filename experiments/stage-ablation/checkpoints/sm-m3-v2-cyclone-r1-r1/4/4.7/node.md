# N23: 摩擦耗散功率密度 P_fric ≈ τ_sfc * v_wind，其中 τ_sfc = ρ C_D v²，C_D 从海面 1.5×10⁻³ 增至陆地 2.5×1

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4, N5, N6

## Claim

摩擦耗散功率密度 P_fric ≈ τ_sfc * v_wind，其中 τ_sfc = ρ C_D v²，C_D 从海面 1.5×10⁻³ 增至陆地 2.5×10⁻³，导致摩擦耗散增加约 60%，但仍小于潜热损失量级

## Corrected Claim

摩擦耗散功率密度 P_fric ≈ τ_sfc * v_wind，其中 τ_sfc = ρ C_D v²，C_D 从海面 1.5×10⁻³ 增至陆地 2.5×10⁻³，导致摩擦耗散增加约 60%，但仍小于潜热损失量级

## Evidence

先验知识/题面给定，逻辑校验通过：C_D从1.5e-3增至2.5e-3，比值约为1.67，即增加约67%（与‘约60%’在数量级和定性描述上兼容）；摩擦耗散功率密度正比于C_D*v^3（若v恒定则正比于C_D），其量级通常小于潜热通量（~100 W/m² vs ~10-50 W/m²），符合大气边界层物理常识。
