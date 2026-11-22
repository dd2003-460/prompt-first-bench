# N81: LFU驻留集合F与LRU驻留集合L的差异量化为：F包含的对象按频率排序，而L按最近访问时间排序；在稳态下，F中的对象集合为频率最高的K'个对象，K'由C/平均大

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N26

## Claim

LFU驻留集合F与LRU驻留集合L的差异量化为：F包含的对象按频率排序，而L按最近访问时间排序；在稳态下，F中的对象集合为频率最高的K'个对象，K'由C/平均大小决定，F与L的对称差集|F△L|的大小决定了LFU的潜在增益上限。

## Corrected Claim

LFU驻留集合F与LRU驻留集合L的差异量化为：F包含的对象按频率排序，而L按最近访问时间排序；在稳态下，F中的对象集合为频率最高的K'个对象，K'由C/平均大小决定，F与L的对称差集|F△L|的大小决定了LFU的潜在增益上限。

## Evidence

先验知识/题面给定，逻辑校验通过
