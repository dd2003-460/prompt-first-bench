# N233: 95th 带宽计费模式下的等效流量单价 $P_{equiv}$ 公式修正：原公式分母应为月总秒数 $86400 \times 30$，而非 $720 \time

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N79, N80, N81

## Claim

95th 带宽计费模式下的等效流量单价 $P_{equiv}$ 公式修正：原公式分母应为月总秒数 $86400 \times 30$，而非 $720 \times 1000$，修正后 $P_{equiv} = R_{bandwidth} / (B_{95th} \times 2592000)$。

## Corrected Claim

95th 带宽计费模式下的等效流量单价 $P_{equiv}$ 公式修正：原公式分母应为月总秒数 $86400 \times 30$，而非 $720 \times 1000$，修正后 $P_{equiv} = R_{bandwidth} / (B_{95th} \times 2592000)$。

## Evidence

先验知识/题面给定，逻辑校验通过：95th带宽计费通常按月结算，月总秒数约为30天×86400秒/天=2592000秒，公式推导符合基本物理/经济直觉。
