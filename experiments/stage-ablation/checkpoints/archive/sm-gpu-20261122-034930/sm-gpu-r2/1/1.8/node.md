# N14: 多卡拓扑可行性：2x RTX 4090 (48GB total) 在INT8下满足41.7GB需求；2x A100 40GB (80GB total) 满足需求

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

多卡拓扑可行性：2x RTX 4090 (48GB total) 在INT8下满足41.7GB需求；2x A100 40GB (80GB total) 满足需求。需考虑PCIe带宽对多卡推理延迟的影响。

## Corrected Claim

多卡拓扑可行性：2x RTX 4090 (48GB total) 在INT8下满足41.7GB需求；2x A100 40GB (80GB total) 满足需求。需考虑PCIe带宽对多卡推理延迟的影响。

## Evidence

先验知识/题面给定，逻辑校验通过：2x48GB=96GB > 41.7GB，2x40GB=80GB > 41.7GB，数值计算正确且符合硬件常识。
