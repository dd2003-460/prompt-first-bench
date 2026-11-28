# N81: 高并发场景 (Batch Size > Batch_Saturation) 下，总吞吐量受限于 GPU FLOPS，公式为 Total_Throughput ≈

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N23

## Claim

高并发场景 (Batch Size > Batch_Saturation) 下，总吞吐量受限于 GPU FLOPS，公式为 Total_Throughput ≈ GPU_FLOPS / (Model_Size * Seq_Len * 2) * Batch_Efficiency，H100 在此场景下单位 Token 成本优势扩大。

## Corrected Claim

高并发场景 (Batch Size > Batch_Saturation) 下，总吞吐量受限于 GPU FLOPS，公式为 Total_Throughput ≈ GPU_FLOPS / (Model_Size * Seq_Len * 2) * Batch_Efficiency，H100 在此场景下单位 Token 成本优势扩大。

## Evidence

先验知识/题面给定，逻辑校验通过：在高并发大Batch场景下，计算密度高，GPU算力成为瓶颈，吞吐量近似等于算力除以单Token计算量（FLOPs/Token），符合硬件性能模型第一性原理。
