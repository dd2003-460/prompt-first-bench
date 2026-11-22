# N40: 买家期望效用阈值下移的量化：买家接受溢价 $\pi$ 的条件为 $E[U_{buyer}] = V_{true} - P_{list} - C_{search}

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N7

## Claim

买家期望效用阈值下移的量化：买家接受溢价 $\pi$ 的条件为 $E[U_{buyer}] = V_{true} - P_{list} - C_{search} \cdot (1-k) > 0$，其中 $V_{true}$ 为商品真实价值，$C_{search}$ 为基准搜索成本。当 $k$ 从0.6增加时，阈值 $V_{true} > P_{list} + C_{search} \cdot (1-k)$ 左侧项减小，允许买家在更高溢价 $\pi$ 下仍保持正效用。

## Corrected Claim

买家期望效用阈值下移的量化：买家接受溢价 $\pi$ 的条件为 $E[U_{buyer}] = V_{true} - P_{list} - C_{search} \cdot (1-k) > 0$，其中 $V_{true}$ 为商品真实价值，$C_{search}$ 为基准搜索成本。当 $k$ 从0.6增加时，阈值 $V_{true} > P_{list} + C_{search} \cdot (1-k)$ 左侧项减小，允许买家在更高溢价 $\pi$ 下仍保持正效用。

## Evidence

先验知识/题面给定，逻辑校验通过：效用函数定义及不等式推导在数学上自洽，k增加导致搜索成本项减小，从而允许更高的溢价，符合经济学直觉。

## Search Query

quantification of buyer expected utility threshold shift due to search cost reduction
