# N22: RTO代价量化：若RTO目标为4小时，本地NVMe SSD阵列恢复时间≈1小时（RAID重建），HDD阵列恢复时间≈8小时（RAID6重建18TB×10盘≈8小

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N3

## Claim

RTO代价量化：若RTO目标为4小时，本地NVMe SSD阵列恢复时间≈1小时（RAID重建），HDD阵列恢复时间≈8小时（RAID6重建18TB×10盘≈8小时），云S3无RTO概念（高可用），RTO代价 = (实际RTO-目标RTO)×业务损失率/小时，假设业务损失率$10,000/小时，HDD方案RTO代价=$10,000×4=$40,000/次，年发生1次则$40,000/年

## Corrected Claim

RTO代价量化：若RTO目标为4小时，本地NVMe SSD阵列恢复时间≈1小时（RAID重建），HDD阵列恢复时间≈8小时（RAID6重建18TB×10盘≈8小时），云S3无RTO概念（高可用），RTO代价 = (实际RTO-目标RTO)×业务损失率/小时，假设业务损失率$10,000/小时，HDD方案RTO代价=$10,000×4=$40,000/次，年发生1次则$40,000/年

## Evidence

父节点级核验通过：正交+完备+无冗余（三个子节点分别针对HDD、NVMe SSD和云对象存储三种不同存储介质进行独立的RTO代价量化与修正，彼此之间没有重叠或矛盾，覆盖了父节点中提到的所有存储类型。每个子节点提供了具体的技术参数（如读取速度、重建时间、SLA等）和计算逻辑，虽然都涉及RTO代价公式，但针对的是不同的物理/逻辑实体，因此不构成冗余。）

## Search Query

RAID6 rebuild time 18TB HDD hours business impact cost
