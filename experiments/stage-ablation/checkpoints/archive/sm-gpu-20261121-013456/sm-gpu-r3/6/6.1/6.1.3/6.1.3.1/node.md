# N240: 1×RTX 4090 方案中，硬件折旧成本占比随使用年限 N 的变化公式为：Depreciation_Ratio(N) = (1599/N) / (1599/N

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N95

## Claim

1×RTX 4090 方案中，硬件折旧成本占比随使用年限 N 的变化公式为：Depreciation_Ratio(N) = (1599/N) / (1599/N + 0.45*8760*N*0.12 + 100)，其中电力成本随 N 线性增长，导致折旧占比非线性下降。

## Corrected Claim

1×RTX 4090 方案中，硬件折旧成本占比随使用年限 N 的变化公式为：Depreciation_Ratio(N) = (1599/N) / (1599/N + 0.45*8760*N*0.12 + 100)，其中电力成本随 N 线性增长，导致折旧占比非线性下降。

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构符合成本分摊逻辑，电力成本随时间线性累积导致分母中折旧项占比非线性下降，数学推导自洽。
