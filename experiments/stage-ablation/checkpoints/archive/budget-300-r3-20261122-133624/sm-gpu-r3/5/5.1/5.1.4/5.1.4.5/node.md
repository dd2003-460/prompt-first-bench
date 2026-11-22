# N348: RTX 5090 在 INT8 下 Decode 阶段的实际有效带宽效率为 75-80% (受限于 GDDR7 的突发读取模式、PCIe 瓶颈及驱动优化)，因此

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N115, N116, N117

## Claim

RTX 5090 在 INT8 下 Decode 阶段的实际有效带宽效率为 75-80% (受限于 GDDR7 的突发读取模式、PCIe 瓶颈及驱动优化)，因此实际 Decode 吞吐量约为 49.8-53.1 tokens/s，而非基于 85% 效率估算的 56.4 tokens/s

## Corrected Claim

RTX 5090 在 INT8 下 Decode 阶段的实际有效带宽效率通常低于理论峰值（受限于 GDDR7 突发读取模式、PCIe 瓶颈及驱动优化），实际 Decode 吞吐量会低于基于高效率（如 85%）估算的理论值。

## Evidence

[质询]具体数值（75-80%效率、49.8-53.1 tokens/s）属于高度依赖具体模型架构、序列长度及驱动版本的经验性测量数据，无法从第一性原理严格推导，且缺乏外部来源佐证其精确性。 | 先验知识/题面给定，逻辑校验通过（数值量级与RTX 5090 GDDR7带宽及INT8推理常识相符），但具体效率百分比和吞吐量数值为经验事实，缺乏直接来源支持，故降级。

## Search Query

RTX 5090 INT8 decode throughput benchmark
