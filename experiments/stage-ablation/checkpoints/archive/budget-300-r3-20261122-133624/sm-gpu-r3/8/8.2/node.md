# N167: 吞吐量对比修正：RTX 4090 (INT8) 与 H100 (BF16) 的吞吐量比值约为 1:2.5 (Decode) 和 1:3.5 (Prefill)。

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N41

## Claim

吞吐量对比修正：RTX 4090 (INT8) 与 H100 (BF16) 的吞吐量比值约为 1:2.5 (Decode) 和 1:3.5 (Prefill)。在低负载场景下，H100 的单位 token 成本优势被其高昂的硬件 TCO 抵消；在高并发或长上下文 Prefill 密集场景下，H100 的性价比优势逐渐显现。

## Corrected Claim

吞吐量对比修正：RTX 4090 (INT8) 与 H100 (BF16) 的吞吐量比值约为 1:2.5 (Decode) 和 1:3.5 (Prefill)。在低负载场景下，H100 的单位 token 成本优势被其高昂的硬件 TCO 抵消；在高并发或长上下文 Prefill 密集场景下，H100 的性价比优势逐渐显现。

## Evidence

先验知识/题面给定，逻辑校验通过
