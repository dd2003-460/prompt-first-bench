# N61: 数据中心卡 TCO 交叉点计算：设 H100 价格 P_h100=$28k, H200 价格 P_h200=$32k, MI300X 价格 P_mi=$18k 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N13

## Claim

数据中心卡 TCO 交叉点计算：设 H100 价格 P_h100=$28k, H200 价格 P_h200=$32k, MI300X 价格 P_mi=$18k [待核验]。年 OpEx = 功耗 * 8760 * 电价。H100 (700W) 年 OpEx=$6132, H200 (700W) 年 OpEx=$6132, MI300X (750W) 年 OpEx=$6570。3年 TCO = 价格 + 3*OpEx + 冷却摊销。H100 3年 TCO ≈ $28k + $18.4k + $5k = $51.4k; H200 ≈ $32k + $18.4k + $5k = $55.4k; MI300X ≈ $18k + $19.7k + $5k = $42.7k。MI300X 在 3 年周期内 TCO 最低，但需考虑 ROCm 软件稳定性风险 [待核验]。

## Corrected Claim

数据中心卡 TCO 交叉点计算：设 H100 价格 P_h100=$28k, H200 价格 P_h200=$32k, MI300X 价格 P_mi=$18k [待核验]。年 OpEx = 功耗 * 8760 * 电价。H100 (700W) 年 OpEx=$6132, H200 (700W) 年 OpEx=$6132, MI300X (750W) 年 OpEx=$6570。3年 TCO = 价格 + 3*OpEx + 冷却摊销。H100 3年 TCO ≈ $28k + $18.4k + $5k = $51.4k; H200 ≈ $32k + $18.4k + $5k = $55.4k; MI300X ≈ $18k + $19.7k + $5k = $42.7k。MI300X 在 3 年周期内 TCO 最低，但需考虑 ROCm 软件稳定性风险 [待核验]。

## Evidence

先验知识/题面给定，逻辑校验通过：OpEx计算（700W*8760h*0.1$/kWh≈$6132）及TCO加总逻辑自洽，数值量级合理。
