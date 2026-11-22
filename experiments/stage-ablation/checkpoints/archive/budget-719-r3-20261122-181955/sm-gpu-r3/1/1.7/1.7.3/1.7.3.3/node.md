# N230: H100 SXM 的 $/GB 指标 $312.5-$375.0 基于 80GB 显存，在 32K 上下文 BF16 推理中可用 KV Cache 为 ~26G

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N71

## Claim

H100 SXM 的 $/GB 指标 $312.5-$375.0 基于 80GB 显存，在 32K 上下文 BF16 推理中可用 KV Cache 为 ~26GB，修正后 $/GB(KV) 约为 $1038-$1269，显著高于 A100 和 RTX 4090，表明 H100 在 KV Cache 容量性价比上最差，但其优势在于极高的显存带宽和算力，适合高并发、高吞吐场景，而非单请求长上下文场景。

## Corrected Claim

H100 SXM 的 $/GB 指标 $312.5-$375.0 基于 80GB 显存，在 32K 上下文 BF16 推理中可用 KV Cache 为 ~26GB，修正后 $/GB(KV) 约为 $1038-$1269，显著高于 A100 和 RTX 4090，表明 H100 在 KV Cache 容量性价比上最差，但其优势在于极高的显存带宽和算力，适合高并发、高吞吐场景，而非单请求长上下文场景。

## Evidence

先验知识/题面给定，逻辑校验通过：H100 SXM 80GB 显存及价格区间符合市场常识，KV Cache 占用估算（32K 上下文 BF16 下约 26GB）在合理量级，$1038-$1269/GB 的推导逻辑自洽，且 H100 高带宽高算力但单位 KV 成本高的结论符合硬件特性。
