# N227: 吞吐量衰减系数：INT8 相比 BF16 的理论吞吐量提升倍数与实际实测值差异，受限于计算单元而非显存带宽时的瓶颈分析。

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N73

## Claim

吞吐量衰减系数：INT8 相比 BF16 的理论吞吐量提升倍数与实际实测值差异，受限于计算单元而非显存带宽时的瓶颈分析。

## Corrected Claim

INT8 相比 BF16 通常具有更高的理论吞吐量（通常约为 2 倍或更高，取决于硬件对 INT8 的支持程度），但在实际应用中，若系统受限于显存带宽而非计算单元，吞吐量提升幅度可能低于理论值，具体倍数需依据特定硬件架构和实测数据确定。

## Evidence

[质询]该陈述描述的是具体的硬件性能经验事实（INT8 vs BF16 吞吐量倍数及瓶颈分析），属于硬件规格与实测数据范畴，无法从第一性原理严格推导，且缺乏具体数值支撑，存在因硬件架构不同（如 Tensor Core 支持程度、内存带宽限制）导致结论差异的风险。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且属于硬件性能经验数据，不适用第一性原理推导条款）

## Search Query

RTX 4090 INT8 vs BF16 LLM inference throughput benchmark
