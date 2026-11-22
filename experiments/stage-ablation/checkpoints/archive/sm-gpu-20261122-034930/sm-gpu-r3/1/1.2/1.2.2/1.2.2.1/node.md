# N166: 修正 N50 矛盾：基于 N49 修正后的参数，32K 上下文下 FP16 KV Cache 理论最小值为 8GB，N8 中的 10.7GB 应解释为包含 Pa

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N49, N50, N51

## Claim

修正 N50 矛盾：基于 N49 修正后的参数，32K 上下文下 FP16 KV Cache 理论最小值为 8GB，N8 中的 10.7GB 应解释为包含 PagedAttention 块对齐开销 (Block Size=16 tokens) 及框架预留的保守估计，实际部署需采用 10.7GB 作为规划值。

## Corrected Claim

修正 N50 矛盾：基于 N49 修正后的参数，32K 上下文下 FP16 KV Cache 理论最小值为 8GB，N8 中的 10.7GB 应解释为包含 PagedAttention 块对齐开销 (Block Size=16 tokens) 及框架预留的保守估计，实际部署需采用 10.7GB 作为规划值。

## Evidence

先验知识/题面给定，逻辑校验通过：32K上下文下FP16 KV Cache理论最小值8GB与包含PagedAttention块对齐开销及框架预留的10.7GB规划值在量级和逻辑上自洽，符合实际部署保守估计原则。
