# N199: 2x RTX 4090 通信瓶颈对实际吞吐的影响：若通信占比 25.6% (BF16)，有效吞吐 = 1 / (T_compute + T_comm) = 1 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N75

## Claim

2x RTX 4090 通信瓶颈对实际吞吐的影响：若通信占比 25.6% (BF16)，有效吞吐 = 1 / (T_compute + T_comm) = 1 / (5ms + 1.28ms) ≈ 159 tokens/s。若无通信开销，理论吞吐 = 1 / 5ms = 200 tokens/s。通信导致吞吐下降 ≈ 20.6%。若采用 FP8，通信占比 12.8%，有效吞吐 = 1 / (2.5ms + 0.64ms) ≈ 318 tokens/s，理论吞吐 = 1 / 2.5ms = 400 tokens/s，下降 ≈ 20.5%。结论：PCIe 通信开销对 2x RTX 4090 吞吐影响约 20%，不可忽略

## Corrected Claim

2x RTX 4090 通信瓶颈对实际吞吐的影响：若通信占比 25.6% (BF16)，有效吞吐 = 1 / (T_compute + T_comm) = 1 / (5ms + 1.28ms) ≈ 159 tokens/s。若无通信开销，理论吞吐 = 1 / 5ms = 200 tokens/s。通信导致吞吐下降 ≈ 20.6%。若采用 FP8，通信占比 12.8%，有效吞吐 = 1 / (2.5ms + 0.64ms) ≈ 318 tokens/s，理论吞吐 = 1 / 2.5ms = 400 tokens/s，下降 ≈ 20.5%。结论：PCIe 通信开销对 2x RTX 4090 吞吐影响约 20%，不可忽略

## Evidence

先验知识/题面给定，逻辑校验通过：数学计算自洽（1/6.28ms≈159, 1/3.14ms≈318），百分比推导正确（1-159/200≈20.5%），符合并行计算中通信开销对吞吐影响的物理直觉。
