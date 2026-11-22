# N381: RTX 4090 在 FP8 推理模式下的功耗效率比（Joules/Token）或相对于 BF16 模式的功耗变化率：FP8 计算单元（Tensor Cores

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N134

## Claim

RTX 4090 在 FP8 推理模式下的功耗效率比（Joules/Token）或相对于 BF16 模式的功耗变化率：FP8 计算单元（Tensor Cores）的能效是否显著高于 FP16/INT8，导致在相同吞吐量下平均功耗降低的具体百分比（如降低 10-20%）。

## Corrected Claim

RTX 4090 在 FP8 推理模式下，由于 Tensor Cores 对低精度格式的支持优化，其能效比通常优于 BF16/FP16 模式，在相同吞吐量下平均功耗会有所降低，但具体降低百分比（如10-20%）因工作负载和驱动版本而异，需具体基准测试确认。

## Evidence

[质询]具体数值（如降低10-20%）缺乏公开权威基准测试支持，且实际功耗变化受驱动优化、散热策略及具体模型架构影响极大，不同场景下差异显著，直接断言固定百分比存在过度概括风险。 | 经验事实，逻辑自洽（FP8精度降低通常带来能效提升）但缺来源支持，且具体百分比无法从第一性原理严格推出。

## Search Query

RTX 4090 FP8 inference power efficiency vs FP16 joules per token
