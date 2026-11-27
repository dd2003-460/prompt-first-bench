# N138: Prefill阶段TP=4通信开销占比修正：不同于Decode阶段，Prefill的AllReduce通信量与序列长度线性相关，当prompt长度超过一定阈值（

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N67

## Claim

Prefill阶段TP=4通信开销占比修正：不同于Decode阶段，Prefill的AllReduce通信量与序列长度线性相关，当prompt长度超过一定阈值（如>4k tokens）时，NVLink 300GB/s带宽下的通信延迟将占据总Prefill时间的显著比例（预计>20%），需引入修正因子。

## Corrected Claim

Prefill阶段TP=4通信开销占比修正：不同于Decode阶段，Prefill的AllReduce通信量与序列长度线性相关，当prompt长度超过一定阈值（如>4k tokens）时，NVLink 300GB/s带宽下的通信延迟将占据总Prefill时间的显著比例（预计>20%），需引入修正因子。

## Evidence

先验知识/题面给定，逻辑校验通过：Prefill阶段计算密集，AllReduce通信量随序列长度线性增加，在长序列（>4k tokens）下，受限于NVLink带宽，通信延迟占比显著上升（>20%）符合分布式推理的基本物理直觉和工程经验。
