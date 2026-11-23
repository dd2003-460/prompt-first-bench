# N406: 全自建策略的每千请求成本函数 $C_{self}(R) = \frac{C_{fixed}^{self} + C_{var}^{self}(R)}{R/1000

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N150

## Claim

全自建策略的每千请求成本函数 $C_{self}(R) = \frac{C_{fixed}^{self} + C_{var}^{self}(R)}{R/1000}$，其中 $C_{fixed}^{self}$ 为 10 个 POP 点的硬件折旧、机柜租金及基础运维人力成本之和，$C_{var}^{self}(R)$ 为随流量线性增长的带宽及跨网结算费用。

## Corrected Claim

全自建策略的每千请求成本函数 $C_{self}(R) = \frac{C_{fixed}^{self} + C_{var}^{self}(R)}{R/1000}$，其中 $C_{fixed}^{self}$ 为 10 个 POP 点的硬件折旧、机柜租金及基础运维人力成本之和，$C_{var}^{self}(R)$ 为随流量线性增长的带宽及跨网结算费用。

## Evidence

先验知识/题面给定，逻辑校验通过：成本函数结构符合经济学中固定成本与可变成本分摊的基本原理，量纲（元/千请求）与变量定义（R为请求量）自洽，无内部矛盾。
