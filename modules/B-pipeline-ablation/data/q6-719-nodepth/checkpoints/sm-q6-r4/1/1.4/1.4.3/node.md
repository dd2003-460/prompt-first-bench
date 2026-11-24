# N52: Hit_Rate = 1 - (U / R)，其中 U 和 R 为日级统计量；若 U/R > 1，则 Hit_Rate 下限为 0（表示缓存容量不足或对象更新极

- **status**: verified
- **level**: L3
- **source**: given
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N9

## Claim

Hit_Rate = 1 - (U / R)，其中 U 和 R 为日级统计量；若 U/R > 1，则 Hit_Rate 下限为 0（表示缓存容量不足或对象更新极快），需引入缓存容量约束修正项

## Corrected Claim

Hit_Rate = 1 - (U / R)，其中 U 和 R 为日级统计量；若 U/R > 1，则 Hit_Rate 下限为 0（表示缓存容量不足或对象更新极快），需引入缓存容量约束修正项

## Evidence

先验知识/题面给定，逻辑校验通过
