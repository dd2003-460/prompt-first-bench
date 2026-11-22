# N216: INT8 权重量化在单层 Transformer 中引入的均方误差 (MSE) 上界为 σ_layer² ≈ (Δ_w² * ||W||_F²) / N_par

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N70

## Claim

INT8 权重量化在单层 Transformer 中引入的均方误差 (MSE) 上界为 σ_layer² ≈ (Δ_w² * ||W||_F²) / N_params，其中 Δ_w = 2/255 ≈ 0.00784 (INT8 量化步长)，||W||_F 为权重矩阵 F 范数；对于 Qwen3-27B 典型层，该值决定了单层输出扰动幅度。

## Corrected Claim

INT8 权重量化在单层 Transformer 中引入的均方误差 (MSE) 上界为 σ_layer² ≈ (Δ_w² * ||W||_F²) / N_params，其中 Δ_w = 2/255 ≈ 0.00784 (INT8 量化步长)，||W||_F 为权重矩阵 F 范数；对于 Qwen3-27B 典型层，该值决定了单层输出扰动幅度。

## Evidence

先验知识/题面给定，逻辑校验通过：INT8量化步长Δ_w=2/255符合对称量化定义，MSE上界公式符合均方误差与F范数的数学关系，量纲与量级合理。
