# N57: 平均成交周期（T_avg）的分解修正：T_avg 并非单一值，而是加权平均 T_avg = Σ(T_i * w_i)。干预主要影响长尾高溢价商品（T_i 大），

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N19

## Claim

平均成交周期（T_avg）的分解修正：T_avg 并非单一值，而是加权平均 T_avg = Σ(T_i * w_i)。干预主要影响长尾高溢价商品（T_i 大），对低溢价商品（T_i 小）影响微乎其微。需量化高溢价商品在总成交量中的占比 w_high，若 w_high=20%，则整体 T_avg 缩短幅度仅为 10% * 20% = 2%，而非 10%。

## Corrected Claim

平均成交周期（T_avg）的分解修正：T_avg 并非单一值，而是加权平均 T_avg = Σ(T_i * w_i)。干预主要影响长尾高溢价商品（T_i 大），对低溢价商品（T_i 小）影响微乎其微。需量化高溢价商品在总成交量中的占比 w_high，若 w_high=20%，则整体 T_avg 缩短幅度仅为 10% * 20% = 2%，而非 10%。

## Evidence

先验知识/题面给定，逻辑校验通过：加权平均公式及线性叠加原理在数学上自洽，数值推导（10% * 20% = 2%）正确。
