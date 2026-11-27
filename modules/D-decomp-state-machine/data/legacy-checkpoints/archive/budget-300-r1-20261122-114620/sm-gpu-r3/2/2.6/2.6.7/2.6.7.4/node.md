# N276: Decode 阶段吞吐与 Batch Size 的非线性关系修正：在 Batch Size=1 时，Decode 吞吐受限于显存带宽 (Memory-Bandw

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N85

## Claim

Decode 阶段吞吐与 Batch Size 的非线性关系修正：在 Batch Size=1 时，Decode 吞吐受限于显存带宽 (Memory-Bandwidth Bound)，理论吞吐 ≈ Memory_Bandwidth / Model_Size。RTX 4090 带宽 1008 GB/s，W4 模型 13.5GB，理论上限 ≈ 74.6 tokens/s。当 Batch Size 增加时，若 KV Cache 未超出显存，吞吐随 Batch Size 线性增长直到计算单元 (Compute) 成为瓶颈或显存耗尽。对于 W4 单卡，Batch Size=1 已是上限，故无线性增长空间。

## Corrected Claim

Decode 阶段吞吐与 Batch Size 的非线性关系修正：在 Batch Size=1 时，Decode 吞吐受限于显存带宽 (Memory-Bandwidth Bound)，理论吞吐 ≈ Memory_Bandwidth / Model_Size。RTX 4090 带宽 1008 GB/s，W4 模型 13.5GB，理论上限 ≈ 74.6 tokens/s。当 Batch Size 增加时，若 KV Cache 未超出显存，吞吐随 Batch Size 线性增长直到计算单元 (Compute) 成为瓶颈或显存耗尽。对于 W4 单卡，Batch Size=1 已是上限，故无线性增长空间。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 带宽 1008 GB/s 与 W4 模型 13.5GB 的算术推导（1008/13.5 ≈ 74.6）正确，且符合 LLM 推理中 Decode 阶段受显存带宽限制及 Batch Size 对吞吐影响的工程常识。

## Search Query

LLM inference decode throughput memory bandwidth bound batch size
