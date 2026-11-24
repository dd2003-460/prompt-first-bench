# N12: 硬件折旧成本：本地NVMe SSD阵列年折旧 = 硬件采购成本 / 折旧年限（典型3-5年），NVMe SSD单价约为¥3000-5000/TB，500TB需1

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N2

## Claim

硬件折旧成本：本地NVMe SSD阵列年折旧 = 硬件采购成本 / 折旧年限（典型3-5年），NVMe SSD单价约为¥3000-5000/TB，500TB需1000TB物理容量（RAID-10），年折旧 ≈ ¥600,000-1,000,000

## Corrected Claim

硬件折旧成本：本地NVMe SSD阵列年折旧 = 硬件采购成本 / 折旧年限（典型3-5年），NVMe SSD单价约为¥3000-5000/TB，500TB需1000TB物理容量（RAID-10），年折旧 ≈ ¥600,000-1,000,000

## Evidence

父节点级核验未通过：非正交, 不完备（1. 正交性违背：子节点3（电力成本）不属于父节点（硬件折旧成本）的范畴，折旧仅指资产价值随时间的摊销，不包含运营期间的电力消耗，二者属于不同的成本科目（CAPEX vs OPEX）。2. 完备性/范围错误：父节点明确限定为“折旧”，子节点3引入了无关的电力成本，导致分解偏离主题。）

## Search Query

NVMe SSD price per TB 2024
