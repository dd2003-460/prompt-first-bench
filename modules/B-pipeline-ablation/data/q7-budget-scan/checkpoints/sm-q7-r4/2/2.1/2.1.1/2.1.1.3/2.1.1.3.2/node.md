# N481: TBW(总字节写入)寿命精确计算：单盘寿命天数 D_life = TBW_rating / (Daily_Write_Volume * DWAF)。若单盘16T

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N162

## Claim

TBW(总字节写入)寿命精确计算：单盘寿命天数 D_life = TBW_rating / (Daily_Write_Volume * DWAF)。若单盘16TB DWPD=1，则TBW=16PB。假设实际日写入1TB(0.0625 DWPD)，D_life = 16,000TB / (1TB * 1.2) ≈ 13,333天 ≈ 36.5年。远大于5年周期，无需预留更换预算。

## Corrected Claim

TBW(总字节写入)寿命精确计算：单盘寿命天数 D_life = TBW_rating / (Daily_Write_Volume * DWAF)。若单盘16TB DWPD=1，则TBW=16PB。假设实际日写入1TB(0.0625 DWPD)，D_life = 16,000TB / (1TB * 1.2) ≈ 13,333天 ≈ 36.5年。远大于5年周期，无需预留更换预算。

## Evidence

先验知识/题面给定，逻辑校验通过：TBW定义及寿命计算公式符合存储行业标准，数值量级（16PB TBW对应16TB DWPD=1）及计算结果（约36.5年）逻辑自洽且合理。
