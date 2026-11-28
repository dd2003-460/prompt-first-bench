# N9: TP=4 通信开销占比：在 V100 SXM2 (NVLink 300GB/s) 架构下，AllReduce 通信时间占单步推理总时间的比例在隐藏层维度 >40

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N1, N2, N3

## Claim

TP=4 通信开销占比：在 V100 SXM2 (NVLink 300GB/s) 架构下，AllReduce 通信时间占单步推理总时间的比例在隐藏层维度 >4096 时达到 [待核验]%，导致 TP=4 相比 TP=2 的加速比低于线性预期（理想 4x vs 实际 ~[待核验]x）。

## Corrected Claim

在 V100 SXM2 (NVLink 300GB/s) 架构下，当隐藏层维度 >4096 时，AllReduce 通信时间占单步推理总时间的比例显著上升，导致 TP=4 相比 TP=2 的加速比低于线性预期（理想 4x vs 实际 <4x）。

## Evidence

[质询]具体数值缺失且缺乏来源支持：陈述中关键量化指标（通信占比百分比、实际加速比倍数）均为[待核验]状态，且本轮检索无可用来源，无法验证这些经验性数值是否符合V100 SXM2在特定隐藏层维度下的实际性能表现。 | 逻辑自洽：TP=4相比TP=2通信量增加（AllReduce通信量随TP线性增长），且V100 NVLink带宽有限，高维隐藏层下通信开销占比上升导致加速比低于线性预期符合分布式推理基本原理；但具体数值属经验事实，无来源支持，故降级。

## Search Query

Tensor Parallelism overhead V100 NVLink AllReduce latency ratio transformer
