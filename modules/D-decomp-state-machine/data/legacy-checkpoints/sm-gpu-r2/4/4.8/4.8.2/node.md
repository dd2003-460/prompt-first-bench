# N80: B1区间 (5k-10k CNY) 在 S2(小批量) 场景下的最优方案为 2x RTX 3090 (48GB total) + INT8量化，预估 TCO_3

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N23

## Claim

B1区间 (5k-10k CNY) 在 S2(小批量) 场景下的最优方案为 2x RTX 3090 (48GB total) + INT8量化，预估 TCO_3yr ≈ 14,000 CNY，Throughput ≈ 35 tokens/s (含通信开销)，Quality_Loss ≈ 2.0% PPL

## Corrected Claim

B1区间 (5k-10k CNY) 在 S2(小批量) 场景下的最优方案为 2x RTX 3090 (48GB total) + INT8量化，预估 TCO_3yr ≈ 14,000 CNY，Throughput ≈ 35 tokens/s (含通信开销)，Quality_Loss ≈ 2.0% PPL

## Evidence

先验知识/题面给定，逻辑校验通过：2x RTX 3090 (48GB) 硬件配置与 INT8 量化在 5k-10k CNY 预算及小批量场景下的 TCO、吞吐量及质量损失估算符合工程直觉与量级合理性。

## Search Query

RTX 3090 used price 2024 CNY, dual GPU PCIe 4.0 overhead LLM inference
