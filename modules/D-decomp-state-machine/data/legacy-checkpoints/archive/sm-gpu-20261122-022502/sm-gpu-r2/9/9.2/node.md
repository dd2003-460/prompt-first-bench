# N90: RTX 5090 在 FP4 精度下的理论解码吞吐量：基于 1.8 TB/s GDDR7 带宽，假设计算-访存比 (Compute-to-Memory Rati

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N31

## Claim

RTX 5090 在 FP4 精度下的理论解码吞吐量：基于 1.8 TB/s GDDR7 带宽，假设计算-访存比 (Compute-to-Memory Ratio) 为 1:1 (大模型推理典型瓶颈)，理论最大吞吐量 ≈ 1.8 TB/s / (27B * 0.5 bytes) ≈ 133 tokens/s；实际受限于 SM 占用率和 PCIe 延迟，预计实测值为理论值的 50-60%，即 66-80 tokens/s。

## Corrected Claim

RTX 5090 在 FP4 精度下的理论解码吞吐量：基于 1.8 TB/s GDDR7 带宽，假设计算-访存比 (Compute-to-Memory Ratio) 为 1:1 (大模型推理典型瓶颈)，理论最大吞吐量 ≈ 1.8 TB/s / (27B * 0.5 bytes) ≈ 133 tokens/s；实际受限于 SM 占用率和 PCIe 延迟，预计实测值为理论值的 50-60%，即 66-80 tokens/s。

## Evidence

先验知识/题面给定，逻辑校验通过：1.8 TB/s / (27e9 * 0.5 bytes) ≈ 133.3 tokens/s，计算无误；50-60% 效率假设符合大模型推理经验规律。

## Search Query

RTX 5090 FP4 LLM inference benchmark tokens per second
