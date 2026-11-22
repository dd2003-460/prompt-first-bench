# N311: Decode 阶段内存带宽利用率 80%-95% 的区间下限（80%）对应于存在显著 CPU-GPU 数据拷贝或 PCIe 传输瓶颈的场景，上限（95%）对应于

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N111

## Claim

Decode 阶段内存带宽利用率 80%-95% 的区间下限（80%）对应于存在显著 CPU-GPU 数据拷贝或 PCIe 传输瓶颈的场景，上限（95%）对应于纯 HBM/GDDR 访问且无同步等待的理想场景。

## Corrected Claim

Decode 阶段内存带宽利用率 80%-95% 的区间下限（80%）对应于存在显著 CPU-GPU 数据拷贝或 PCIe 传输瓶颈的场景，上限（95%）对应于纯 HBM/GDDR 访问且无同步等待的理想场景。

## Evidence

先验知识/题面给定，逻辑校验通过
