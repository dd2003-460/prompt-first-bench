# N42: 消费级 GPU 推理吞吐量瓶颈分析：对于 27B 模型，decode 阶段是 Memory-Bound 操作。理论最大 Token/s ≈ Memory_Ban

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7

## Claim

消费级 GPU 推理吞吐量瓶颈分析：对于 27B 模型，decode 阶段是 Memory-Bound 操作。理论最大 Token/s ≈ Memory_Bandwidth / Model_Size_In_GB。对于 INT4 (13.5 GB)，RTX 4090 理论上限 ≈ 1008/13.5 ≈ 74.6 tokens/s (理想情况)，实际受限于 Kernel Launch Overhead 和 PCIe 传输，通常在 40-60 tokens/s 范围。

## Corrected Claim

消费级 GPU 推理吞吐量瓶颈分析：对于 27B 模型，decode 阶段是 Memory-Bound 操作。理论最大 Token/s ≈ Memory_Bandwidth / Model_Size_In_GB。对于 INT4 (13.5 GB)，RTX 4090 理论上限 ≈ 1008/13.5 ≈ 74.6 tokens/s (理想情况)，实际受限于 Kernel Launch Overhead 和 PCIe 传输，通常在 40-60 tokens/s 范围。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090显存带宽1008GB/s，INT4下27B模型约13.5GB，理论上限74.6 tokens/s符合Memory-Bound计算逻辑，实际40-60 tokens/s符合工程经验。

## Search Query

LLM inference throughput bound by memory bandwidth formula
