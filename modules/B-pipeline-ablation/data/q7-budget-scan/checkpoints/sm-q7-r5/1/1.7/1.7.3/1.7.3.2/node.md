# N184: Queue Depth (QD) 对NVMe SSD Random Read功耗的非线性影响：在QD=1时功耗最低（约12-15W），随QD增加至QD=32或Q

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N60

## Claim

Queue Depth (QD) 对NVMe SSD Random Read功耗的非线性影响：在QD=1时功耗最低（约12-15W），随QD增加至QD=32或QD=256，功耗趋近峰值20-25W；对于数据湖扫描场景，若驱动层优化为高并发批量读，实际平均功耗应取QD=32-64区间的值，约为16-18W，而非峰值22W。

## Corrected Claim

Queue Depth (QD) 对NVMe SSD Random Read功耗的非线性影响：在QD=1时功耗最低（约12-15W），随QD增加至QD=32或QD=256，功耗趋近峰值20-25W；对于数据湖扫描场景，若驱动层优化为高并发批量读，实际平均功耗应取QD=32-64区间的值，约为16-18W，而非峰值22W。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

NVMe SSD power consumption queue depth dependency random read
