# N10: NVMe RAID方案工作点A(高性能低冗余)：12盘RAID6，逻辑容量=物理容量×0.833，IOPS上限≈12×单盘IOPS(≈200k)，适用场景为温数

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

NVMe RAID方案工作点A(高性能低冗余)：12盘RAID6，逻辑容量=物理容量×0.833，IOPS上限≈12×单盘IOPS(≈200k)，适用场景为温数据高频随机读。

## Corrected Claim

NVMe RAID方案工作点A(高性能低冗余)：12盘RAID6，逻辑容量=物理容量×0.833，IOPS上限≈12×单盘IOPS(≈200k)，适用场景为温数据高频随机读。

## Evidence

父节点级核验未通过：不完备（父节点定义了高性能低冗余方案的工作点A，涵盖了容量计算、IOPS上限及适用场景。子节点仅提供了成本效益分析（折旧、单位成本），虽然与性能指标正交（不矛盾），但严重缺失了父节点中明确提到的'IOPS上限'和'适用场景'等关键性能与业务维度，导致分解不完备。）
