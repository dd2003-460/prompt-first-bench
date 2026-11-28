# N70: 多卡互联拓扑对初始成本的边际影响：若2x RTX 4090通过PCIe x16/x8直连（无NVLink），通信开销导致有效吞吐下降约10-20%，但无需额外硬

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N13

## Claim

多卡互联拓扑对初始成本的边际影响：若2x RTX 4090通过PCIe x16/x8直连（无NVLink），通信开销导致有效吞吐下降约10-20%，但无需额外硬件成本；若考虑NVLink Bridge (仅部分专业卡支持，如A100/H100)，单条NVLink桥接器成本约$500-$1000，且限制CPU选择，需权衡是否值得为<5%的延迟降低支付溢价 [待核验NVLink桥接器实时价格及适用性]

## Corrected Claim

多卡互联拓扑对初始成本的边际影响：若2x RTX 4090通过PCIe x16/x8直连（无NVLink），通信开销可能导致有效吞吐下降，但无需额外硬件成本；若考虑NVLink（主要适用于A100/H100等专业卡，消费级RTX 4090不支持NVLink），需评估特定型号NVLink桥接器的市场成本及主板兼容性，以权衡是否值得为潜在的性能提升支付溢价。

## Evidence

[质询]NVLink桥接器价格及适用性属于实时变动的市场经验数据，且不同代际/型号差异巨大，缺乏当前确切来源支持；此外，‘限制CPU选择’的表述过于绝对，通常NVLink主要依赖主板插槽布局而非严格限制CPU型号。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

NVLink bridge cost dual GPU inference latency impact
