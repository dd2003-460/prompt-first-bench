# N148: 对于冷门对象（R_i 低），τ_res(i) = 1/R_i 极长（如 R_i=1次/天，τ_res=1天），若 R_i < 0.01次/天（即每100天访问一

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N47

## Claim

对于冷门对象（R_i 低），τ_res(i) = 1/R_i 极长（如 R_i=1次/天，τ_res=1天），若 R_i < 0.01次/天（即每100天访问一次），则 τ_res > τ_obj，此时 D_cold = 1 - (1 - e^(-0.01))^2 * (1 - e^(-1)) ≈ 0.9901，折损约 1%。

## Corrected Claim

对于冷门对象（R_i 低），τ_res(i) = 1/R_i 极长（如 R_i=1次/天，τ_res=1天），若 R_i < 0.01次/天（即每100天访问一次），则 τ_res > τ_obj，此时 D_cold = 1 - (1 - e^(-0.01))^2 * (1 - e^(-1)) ≈ 0.9901，折损约 1%。
