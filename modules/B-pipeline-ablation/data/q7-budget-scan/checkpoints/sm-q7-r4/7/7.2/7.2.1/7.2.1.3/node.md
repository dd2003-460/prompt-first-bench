# N626: 折旧年限选择的临界点分析：设折旧年限为 D，5年总成本函数 f(D) = (C_A/D)*min(D,5) + C_elec_5y + C_ops_5y + C

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N261

## Claim

折旧年限选择的临界点分析：设折旧年限为 D，5年总成本函数 f(D) = (C_A/D)*min(D,5) + C_elec_5y + C_ops_5y + C_RTO_5y，求导或枚举 D∈[3,7] 找出使 f(D) 最小的 D 值，若 D<5 则需考虑第 D+1 年的重新采购成本 C_rebuy

## Corrected Claim

折旧年限选择的临界点分析：设折旧年限为 D，5年总成本函数 f(D) = (C_A/D)*min(D,5) + C_elec_5y + C_ops_5y + C_RTO_5y，求导或枚举 D∈[3,7] 找出使 f(D) 最小的 D 值，若 D<5 则需考虑第 D+1 年的重新采购成本 C_rebuy

## Evidence

先验知识/题面给定，逻辑校验通过
