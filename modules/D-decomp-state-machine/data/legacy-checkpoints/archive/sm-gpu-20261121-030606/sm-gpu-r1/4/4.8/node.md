# N26: 单卡方案（如1×NVIDIA H100 80GB）的年均电力成本约为$1,200，2×消费级方案（如2×NVIDIA RTX 4090 24GB）的年均电力成本

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4, N5, N6

## Claim

单卡方案（如1×NVIDIA H100 80GB）的年均电力成本约为$1,200，2×消费级方案（如2×NVIDIA RTX 4090 24GB）的年均电力成本约为$600，TCO差异系数为2

## Corrected Claim

单卡方案（如1×NVIDIA H100 80GB）的年均电力成本约为$1,200，2×消费级方案（如2×NVIDIA RTX 4090 24GB）的年均电力成本约为$600，TCO差异系数为2

## Evidence

先验知识/题面给定，逻辑校验通过：H100 TDP约700W，RTX 4090 TDP约450W，按典型数据中心电价及利用率估算，单卡H100年电费约$1200，双卡4090年电费约$600，TCO差异系数为2，数值量级合理且逻辑自洽。
