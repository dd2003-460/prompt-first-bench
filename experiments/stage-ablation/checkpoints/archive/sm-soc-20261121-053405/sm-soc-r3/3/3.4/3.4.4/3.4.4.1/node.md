# N167: WACC 中权益成本 r_e 的估算公式：r_e = r_f + β_mkt * (r_m - r_f) + β_illiquidity。其中 r_f（无风险利

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N62

## Claim

WACC 中权益成本 r_e 的估算公式：r_e = r_f + β_mkt * (r_m - r_f) + β_illiquidity。其中 r_f（无风险利率）取 10 年期国债收益率（当前约 4%-5%），β_mkt 为平台行业贝塔（通常 1.0-1.2），r_m 为市场风险溢价（通常 5%-7%），β_illiquidity 为流动性风险溢价（二手平台因用户粘性高，估计 0.5%-1%）。代入后 r_e ≈ 10%-13%。

## Corrected Claim

WACC 中权益成本 r_e 的估算公式：r_e = r_f + β_mkt * (r_m - r_f) + β_illiquidity。其中 r_f（无风险利率）取 10 年期国债收益率（当前约 4%-5%），β_mkt 为平台行业贝塔（通常 1.0-1.2），r_m 为市场风险溢价（通常 5%-7%），β_illiquidity 为流动性风险溢价（二手平台因用户粘性高，估计 0.5%-1%）。代入后 r_e ≈ 10%-13%。

## Evidence

先验知识/题面给定，逻辑校验通过：CAPM公式结构正确，各参数取值范围（无风险利率4-5%、Beta 1.0-1.2、市场风险溢价5-7%、流动性溢价0.5-1%）符合金融常识，代入计算得出的权益成本区间10%-13%在数学上自洽且量级合理。
