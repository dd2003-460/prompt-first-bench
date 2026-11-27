# N505: RTX 5090 与 H100 SXM 的 FP8 理论计算峰值比值为 105.9% (1048.6/989.4)，表明在纯计算受限（Compute-Bound

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N155

## Claim

RTX 5090 与 H100 SXM 的 FP8 理论计算峰值比值为 105.9% (1048.6/989.4)，表明在纯计算受限（Compute-Bound/Prefill）场景下，RTX 5090 的理论算力上限略高于 H100，而非 N155 声称的 52%。

## Corrected Claim

RTX 5090 与 H100 SXM 的 FP8 理论计算峰值比值为 105.9% (1048.6/989.4)，表明在纯计算受限（Compute-Bound/Prefill）场景下，RTX 5090 的理论算力上限略高于 H100，而非 N155 声称的 52%。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 5090 FP8 算力约 1048.6 TFLOPS，H100 SXM FP8 算力约 989.4 TFLOPS，比值计算正确且符合硬件规格常识。
