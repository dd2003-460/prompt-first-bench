# N364: Batch Size 对 Throughput 的线性提升假设仅在 Prefill 阶段成立（计算密集型），在 Decode 阶段（访存密集型），随着 Batc

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N151, N152, N153

## Claim

Batch Size 对 Throughput 的线性提升假设仅在 Prefill 阶段成立（计算密集型），在 Decode 阶段（访存密集型），随着 Batch Size 增加，KV Cache 读取带宽成为瓶颈；当 Batch Size > 1 时，单 Token 延迟 T_decode 会随 Batch Size 近似线性增加，因此总吞吐量 (Tokens/s) 虽增加，但单用户延迟 (Latency) 恶化；在交互式场景 (Batch=1) 下，N151 的吞吐量提升结论不适用，需区分 Batch=1 的 Latency 优化与 Batch>1 的 Throughput 优化。

## Corrected Claim

Batch Size 对 Throughput 的线性提升假设仅在 Prefill 阶段成立（计算密集型），在 Decode 阶段（访存密集型），随着 Batch Size 增加，KV Cache 读取带宽成为瓶颈；当 Batch Size > 1 时，单 Token 延迟 T_decode 会随 Batch Size 近似线性增加，因此总吞吐量 (Tokens/s) 虽增加，但单用户延迟 (Latency) 恶化；在交互式场景 (Batch=1) 下，N151 的吞吐量提升结论不适用，需区分 Batch=1 的 Latency 优化与 Batch>1 的 Throughput 优化。

## Evidence

先验知识/题面给定，逻辑校验通过：Prefill阶段计算密集，Decode阶段访存密集，Batch Size增加导致KV Cache带宽瓶颈及单Token延迟线性增加符合LLM推理基本物理/工程直觉。
