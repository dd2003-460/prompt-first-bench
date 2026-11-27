# N156: FFN (MLP) 模块参数量公式展开：Params_FFN = (Up_proj + Down_proj)，其中 Up_proj = hidden_dim *

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N35

## Claim

FFN (MLP) 模块参数量公式展开：Params_FFN = (Up_proj + Down_proj)，其中 Up_proj = hidden_dim * intermediate_dim, Down_proj = intermediate_dim * hidden_dim。对于 SwiGLU 结构，实际包含 3 个矩阵，总参数 = 3 * hidden_dim * intermediate_dim。

## Corrected Claim

FFN (MLP) 模块参数量公式展开：Params_FFN = (Up_proj + Down_proj)，其中 Up_proj = hidden_dim * intermediate_dim, Down_proj = intermediate_dim * hidden_dim。对于 SwiGLU 结构，实际包含 3 个矩阵，总参数 = 3 * hidden_dim * intermediate_dim。

## Evidence

先验知识/题面给定，逻辑校验通过
