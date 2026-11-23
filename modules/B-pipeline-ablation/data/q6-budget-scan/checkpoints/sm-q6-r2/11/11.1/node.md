# N143: P99 延迟目标 $T_{target}$ 的构成公式为 $T_{target} = L_{edge} + L_{backhaul} + L_{processi

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N35

## Claim

P99 延迟目标 $T_{target}$ 的构成公式为 $T_{target} = L_{edge} + L_{backhaul} + L_{processing} + L_{queue}$。其中 $L_{edge}$ 和 $L_{processing}$ 为固定开销（约 5-15ms），$L_{backhaul}$ 取决于回源路径，$L_{queue}$ 取决于负载。

## Corrected Claim

P99 延迟目标 $T_{target}$ 的构成公式为 $T_{target} = L_{edge} + L_{backhaul} + L_{processing} + L_{queue}$。其中 $L_{edge}$ 和 $L_{processing}$ 为固定开销（约 5-15ms），$L_{backhaul}$ 取决于回源路径，$L_{queue}$ 取决于负载。

## Evidence

先验知识/题面给定，逻辑校验通过：延迟分解符合网络通信基本模型，5-15ms的固定开销量级在边缘计算场景下合理。
