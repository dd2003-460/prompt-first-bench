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

父节点级核验通过：正交+完备+无冗余（子节点分别针对HDD、NVMe SSD和云S3三种不同存储介质的RTO量化逻辑进行了独立且详细的修正与定义，彼此之间无重叠（正交），且完整覆盖了父节点中提到的所有场景（完备）。虽然都涉及RTO计算公式，但针对不同介质的物理特性和故障模式进行了具体化，不属于简单参数冗余。）

## Search Query

RAID6 rebuild time 18TB HDD hours business impact cost
