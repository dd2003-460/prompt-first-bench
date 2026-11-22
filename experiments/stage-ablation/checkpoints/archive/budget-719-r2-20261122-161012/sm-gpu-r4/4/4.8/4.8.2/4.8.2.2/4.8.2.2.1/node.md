# N625: H100 SXM 单卡在 32K 上下文下的有效 Prefill FLOPs 同样需修正为 2 * N_params * L_context = 2 * 27e

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N260

## Claim

H100 SXM 单卡在 32K 上下文下的有效 Prefill FLOPs 同样需修正为 2 * N_params * L_context = 2 * 27e9 * 32768 ≈ 1.77e12 FLOPs（父节点 N260 中 2.25e15 的估算存在与 N259 相同的计算复杂度错误）

## Corrected Claim

H100 SXM 单卡在 32K 上下文下的有效 Prefill FLOPs 同样需修正为 2 * N_params * L_context = 2 * 27e9 * 32768 ≈ 1.77e12 FLOPs（父节点 N260 中 2.25e15 的估算存在与 N259 相同的计算复杂度错误）

## Evidence

先验知识/题面给定，逻辑校验通过：Prefill 阶段计算量公式为 2 * N_params * L_context，代入 27e9 和 32768 计算结果约为 1.77e12 FLOPs，量级与逻辑均正确。
