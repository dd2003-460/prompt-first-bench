# N293: 工作点A（Prefill/短上下文高算力负载）：在输入长度 < 2K 且 Batch Size ≥ 4 时，计算单元（Tensor Core）利用率 > 70%

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N97

## Claim

工作点A（Prefill/短上下文高算力负载）：在输入长度 < 2K 且 Batch Size ≥ 4 时，计算单元（Tensor Core）利用率 > 70%，功耗接近 TDP 上限 450W；此时 TCO 电力成本项应按 450W 计算，误差 < 5%。

## Corrected Claim

工作点A（Prefill/短上下文高算力负载）：在输入长度 < 2K 且 Batch Size ≥ 4 时，计算单元（Tensor Core）利用率 > 70%，功耗接近 TDP 上限 450W；此时 TCO 电力成本项应按 450W 计算，误差 < 5%。

## Evidence

先验知识/题面给定，逻辑校验通过
