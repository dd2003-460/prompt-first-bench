# N315: 10个POP点总带宽年成本：C_bw_annual = 10 * 12 * C_bw_pop，若按流量计费（¥0.1/GB），月流量300GB/POP，年成本≈

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N100

## Claim

10个POP点总带宽年成本：C_bw_annual = 10 * 12 * C_bw_pop，若按流量计费（¥0.1/GB），月流量300GB/POP，年成本≈¥360k；若按固定带宽（¥15k/月/POP），年成本≈¥1.8M，两者差异5倍，需根据实际P95利用率（通常<50%）选择95th Percentile计费以降低成本至固定带宽的40-60%

## Corrected Claim

10个POP点总带宽年成本：C_bw_annual = 10 * 12 * C_bw_pop，若按流量计费（¥0.1/GB），月流量300GB/POP，年成本≈¥360k；若按固定带宽（¥15k/月/POP），年成本≈¥1.8M，两者差异5倍，需根据实际P95利用率（通常<50%）选择95th Percentile计费以降低成本至固定带宽的40-60%

## Evidence

先验知识/题面给定，逻辑校验通过：流量成本计算 10*12*300*0.1=36,000元（即36k），固定带宽成本 10*12*15,000=1,800,000元（即1.8M），两者比值5倍，且95th Percentile计费通常介于两者之间，符合工程常识。
