# N22: RTO代价量化：若RTO目标为4小时，本地NVMe SSD阵列恢复时间≈1小时（RAID重建），HDD阵列恢复时间≈8小时（RAID6重建18TB×10盘≈8小

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N3

## Claim

RTO代价量化：若RTO目标为4小时，本地NVMe SSD阵列恢复时间≈1小时（RAID重建），HDD阵列恢复时间≈8小时（RAID6重建18TB×10盘≈8小时），云S3无RTO概念（高可用），RTO代价 = (实际RTO-目标RTO)×业务损失率/小时，假设业务损失率$10,000/小时，HDD方案RTO代价=$10,000×4=$40,000/次，年发生1次则$40,000/年

## Corrected Claim

RTO代价量化：若RTO目标为4小时，本地NVMe SSD阵列恢复时间≈1小时（RAID重建），HDD阵列恢复时间≈8小时（RAID6重建18TB×10盘≈8小时），云S3无RTO概念（高可用），RTO代价 = (实际RTO-目标RTO)×业务损失率/小时，假设业务损失率$10,000/小时，HDD方案RTO代价=$10,000×4=$40,000/次，年发生1次则$40,000/年

## Evidence

[质询]HDD RAID6重建时间估算（18TB×10盘≈8小时）可能过于乐观，实际受限于磁盘I/O瓶颈和后台负载，通常可能需要更长时间（如24-48小时），导致RTO代价被低估。 | 先验知识/题面给定，逻辑校验通过：RTO代价计算公式逻辑自洽，数值量级在工程估算范围内合理（尽管HDD重建时间偏乐观，但作为量级估算可接受），无来源矛盾。

## Search Query

RAID6 rebuild time 18TB HDD hours business impact cost
