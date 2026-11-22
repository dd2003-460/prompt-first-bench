# N378: RTX 4090 在 32K 上下文、Batch=1 下的实测 Decode 吞吐量通常为 30-40 tokens/s，而 H100 SXM 为 80-100

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N133

## Claim

RTX 4090 在 32K 上下文、Batch=1 下的实测 Decode 吞吐量通常为 30-40 tokens/s，而 H100 SXM 为 80-100 tokens/s，实测比值为 1:2.5 至 1:3.3，低于理论带宽比 (1:3.32)，差异源于 H100 更高的计算密度和更优的内存控制器效率，该实测比值应作为最终性价比计算的基准系数。

## Corrected Claim

RTX 4090 与 H100 SXM 在 32K 上下文、Batch=1 下的实测 Decode 吞吐量比值通常在 1:2.5 至 1:3.3 之间，低于理论带宽比 (1:3.32)，该比值可作为性能对比的参考基准，但具体数值需根据实际模型和配置调整。

## Evidence

[质询]具体吞吐量数值（30-40 tokens/s 和 80-100 tokens/s）属于高度依赖模型架构、量化方式及软件栈的经验事实，且不同测试场景下波动较大，缺乏通用性；此外，将特定实测比值直接定义为‘最终性价比计算的基准系数’在方法论上过于绝对，忽略了其他成本因素。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）

## Search Query

RTX 4090 vs H100 Qwen2 72B decode throughput benchmark tokens/s
