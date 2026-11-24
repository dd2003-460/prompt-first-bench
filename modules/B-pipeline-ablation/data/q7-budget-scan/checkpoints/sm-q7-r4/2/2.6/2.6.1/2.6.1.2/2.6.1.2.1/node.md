# N600: NVMe SSD 5年总写入量（TBW）验证：500TB容量，假设每日重写因子DWF=1.0（数据湖主要读取，少量更新），年写入量=500TB * 365 * 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N202

## Claim

NVMe SSD 5年总写入量（TBW）验证：500TB容量，假设每日重写因子DWF=1.0（数据湖主要读取，少量更新），年写入量=500TB * 365 * 1.0 = 182,500TB。5年总写入=912,500TB。单盘(2TB)需承受TBW ≥ 912,500/250(盘数) = 3,650TB。主流企业级NVMe(如Intel P5510 2TB)标称DWPD=3.0，对应TBW=2TB*3*5=30TB? 不，DWPD是Daily Write Per Drive。2TB * 3 DWPD * 365 * 5 = 10,950TB。远大于3,650TB，故5年内SSD物理寿命不构成瓶颈，折旧期5年安全。

## Corrected Claim

NVMe SSD 5年总写入量（TBW）验证：500TB容量，假设每日重写因子DWF=1.0（数据湖主要读取，少量更新），年写入量=500TB * 365 * 1.0 = 182,500TB。5年总写入=912,500TB。单盘(2TB)需承受TBW ≥ 912,500/250(盘数) = 3,650TB。主流企业级NVMe(如Intel P5510 2TB)标称DWPD=3.0，对应TBW=2TB*3*5=30TB? 不，DWPD是Daily Write Per Drive。2TB * 3 DWPD * 365 * 5 = 10,950TB。远大于3,650TB，故5年内SSD物理寿命不构成瓶颈，折旧期5年安全。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程自洽（500TB*365*5=912,500TB总写入，除以250盘得单盘3,650TB需求；Intel P5510 2TB DWPD 3.0对应寿命10,950TB，远大于需求），符合企业级SSD常规规格与寿命估算逻辑。

## Search Query

Enterprise NVMe SSD 2TB DWPD 3.0 TBW calculation 5 years
