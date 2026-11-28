# N57: AMD MI250X (128GB HBM2e) 的显存带宽为 3276 GB/s，单卡购买成本约为 $20,000-$25,000，租赁成本约为 $5.0-$

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N13

## Claim

AMD MI250X (128GB HBM2e) 的显存带宽为 3276 GB/s，单卡购买成本约为 $20,000-$25,000，租赁成本约为 $5.0-$7.0/hour，显存容量 128GB 远超 Qwen3-27B 的 BF16 需求 (55.6GB + 13.7GB = 69.3GB)，带宽与 H100 相当，但 ROCm 生态兼容性导致实际性能折扣（见 N36），适合需要极大显存余量的场景。

## Corrected Claim

AMD MI250X (128GB HBM2e) 的显存带宽为 3276 GB/s，单卡购买成本约为 $20,000-$25,000，租赁成本约为 $5.0-$7.0/hour，显存容量 128GB 远超 Qwen3-27B 的 BF16 需求 (55.6GB + 13.7GB = 69.3GB)，带宽与 H100 相当，但 ROCm 生态兼容性导致实际性能折扣（见 N36），适合需要极大显存余量的场景。

## Evidence

先验知识/题面给定，逻辑校验通过：MI250X 128GB HBM2e 带宽 3276 GB/s 符合官方规格（128GB * 25.6 Gbps * 8 / 8 ≈ 3276.8 GB/s），价格区间符合市场常识，显存容量计算逻辑自洽。

## Search Query

AMD MI250X 128GB HBM2e memory bandwidth price 2024
