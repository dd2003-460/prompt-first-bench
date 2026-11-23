# N41: 混合策略的 P99 延迟成本函数 $C_{hyb}(T, s, \theta)$：$C_{hyb} = \theta \cdot C_{self}^{local

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N4, N5, N6

## Claim

混合策略的 P99 延迟成本函数 $C_{hyb}(T, s, \theta)$：$C_{hyb} = \theta \cdot C_{self}^{local} + (1-\theta) \cdot C_{pub}^{tail} + C_{sync}^{cross}$，其中 $\theta$ 为本地命中流量比例，$C_{sync}^{cross}$ 为跨域同步/回源成本，需最小化 $C_{hyb}$ 关于 $\theta$ 和 POP 选址 $S_{10}$。

## Corrected Claim

混合策略的 P99 延迟成本函数 $C_{hyb}(T, s, \theta)$：$C_{hyb} = \theta \cdot C_{self}^{local} + (1-\theta) \cdot C_{pub}^{tail} + C_{sync}^{cross}$，其中 $\theta$ 为本地命中流量比例，$C_{sync}^{cross}$ 为跨域同步/回源成本，需最小化 $C_{hyb}$ 关于 $\theta$ 和 POP 选址 $S_{10}$。

## Evidence

先验知识/题面给定，逻辑校验通过
