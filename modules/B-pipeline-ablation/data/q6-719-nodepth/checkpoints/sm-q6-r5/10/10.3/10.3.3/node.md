# N386: 修正分母公式：R_norm = (R_read_daily * 1.0 + R_write_daily * 0.5) / 1000 = (0.95 * R_da

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N129

## Claim

修正分母公式：R_norm = (R_read_daily * 1.0 + R_write_daily * 0.5) / 1000 = (0.95 * R_daily + 0.05 * R_daily * 0.5) / 1000 = 0.975 * R_daily / 1000，比原始分母R_daily/1000低2.5%，导致每千请求成本被高估2.5%。

## Corrected Claim

修正分母公式：R_norm = (R_read_daily * 1.0 + R_write_daily * 0.5) / 1000 = (0.95 * R_daily + 0.05 * R_daily * 0.5) / 1000 = 0.975 * R_daily / 1000，比原始分母R_daily/1000低2.5%，导致每千请求成本被高估2.5%。

## Evidence

先验知识/题面给定，逻辑校验通过：数学推导正确，0.975/1.0 = 0.975，分母降低2.5%导致比值（成本）升高约2.56%，近似为2.5%符合工程估算精度。
