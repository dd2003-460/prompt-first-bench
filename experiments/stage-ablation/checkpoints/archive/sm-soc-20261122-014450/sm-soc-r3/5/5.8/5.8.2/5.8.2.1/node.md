# N344: 基准状态下的买家搜索成本 C_search_base = α * (1 - β * 0.3^γ)，假设 α = 100, β = 0.8, γ = 1.5（需根

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N110

## Claim

基准状态下的买家搜索成本 C_search_base = α * (1 - β * 0.3^γ)，假设 α = 100, β = 0.8, γ = 1.5（需根据文献校准），计算 C_search_base 的具体数值。

## Corrected Claim

基准状态下的买家搜索成本 C_search_base = α * (1 - β * 0.3^γ)，假设 α = 100, β = 0.8, γ = 1.5（需根据文献校准），计算 C_search_base 的具体数值。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 C = α * (1 - β * 0.3^γ) 代入 α=100, β=0.8, γ=1.5，计算得 100 * (1 - 0.8 * 0.1643) ≈ 86.86，数值量级合理且无内部矛盾。
