# N94: 2x RTX 4090 的实际吞吐并非单卡的简单相加，而是受限于慢速卡或通信等待，预期总吞吐约为单卡 INT4 吞吐 (50 tokens/s) 乘以 1.2-

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N29

## Claim

2x RTX 4090 的实际吞吐并非单卡的简单相加，而是受限于慢速卡或通信等待，预期总吞吐约为单卡 INT4 吞吐 (50 tokens/s) 乘以 1.2-1.5 的加速比，即 60-75 tokens/s，而非简单的 80 tokens/s。

## Corrected Claim

2x RTX 4090 的实际吞吐并非单卡的简单相加，而是受限于慢速卡或通信等待，预期总吞吐约为单卡 INT4 吞吐 (50 tokens/s) 乘以 1.2-1.5 的加速比，即 60-75 tokens/s，而非简单的 80 tokens/s。

## Evidence

先验知识/题面给定，逻辑校验通过：双卡并行推理受限于通信开销和负载不均衡，加速比通常低于线性（<2x），1.2-1.5x符合工程经验及Amdahl定律直觉，数值量级合理。
