# N309: 平台成本支出项 ΔW_platform 的量化：ΔW_platform = C_dev + C_ops * T_int，其中 C_dev 为干预系统开发的一次性

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N89

## Claim

平台成本支出项 ΔW_platform 的量化：ΔW_platform = C_dev + C_ops * T_int，其中 C_dev 为干预系统开发的一次性成本（假设 50万元），C_ops 为日常运营成本（假设 0.5元/单），T_int 为干预实施后的总成交单量。若 T_int = 10000单，则 ΔW_platform = 500000 + 0.5*10000 = 505000元。

## Corrected Claim

平台成本支出项 ΔW_platform 的量化：ΔW_platform = C_dev + C_ops * T_int，其中 C_dev 为干预系统开发的一次性成本（假设 50万元），C_ops 为日常运营成本（假设 0.5元/单），T_int 为干预实施后的总成交单量。若 T_int = 10000单，则 ΔW_platform = 500000 + 0.5*10000 = 505000元。

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构符合成本构成逻辑（一次性+变动成本），数值计算 500000 + 0.5*10000 = 505000 准确无误，量纲一致。
