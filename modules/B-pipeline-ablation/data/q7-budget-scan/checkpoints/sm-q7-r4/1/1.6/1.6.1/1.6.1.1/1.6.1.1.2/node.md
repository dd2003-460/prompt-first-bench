# N394: 工作点B（中持久性/中成本）：阿里云 OSS 标准存储（ZRS 同城冗余）持久性承诺 12 nines (10^-12)，单价 ¥0.12/GB/月，隐含冗余系

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N173

## Claim

工作点B（中持久性/中成本）：阿里云 OSS 标准存储（ZRS 同城冗余）持久性承诺 12 nines (10^-12)，单价 ¥0.12/GB/月，隐含冗余系数 k_redundancy ≈ 1.5（跨 3 AZ EC），单位有效容量成本 C_eff_B = 0.12 * 1.5 = ¥0.18/GB/月

## Corrected Claim

工作点B（中持久性/中成本）：阿里云 OSS 标准存储（ZRS 同城冗余）持久性承诺 12 nines (10^-12)，单价 ¥0.12/GB/月，隐含冗余系数 k_redundancy ≈ 1.5（跨 3 AZ EC），单位有效容量成本 C_eff_B = 0.12 * 1.5 = ¥0.18/GB/月

## Evidence

先验知识/题面给定，逻辑校验通过：阿里云OSS标准存储（ZRS）官方承诺数据持久性为99.9999999999%（12个9），价格约0.12元/GB/月，ZRS通常涉及多副本或纠删码导致物理存储开销大于逻辑容量，隐含冗余系数1.5符合工程常识，计算逻辑自洽。
