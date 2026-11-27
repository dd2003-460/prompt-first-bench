# N408: RTX 5090 的 TDP 为 575W，若采用 16K 上下文方案以适配 32GB 显存，其每瓦特吞吐量 (Tokens/s per Watt) 约为 10

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N154

## Claim

RTX 5090 的 TDP 为 575W，若采用 16K 上下文方案以适配 32GB 显存，其每瓦特吞吐量 (Tokens/s per Watt) 约为 100/575 ≈ 0.175，需对比 RTX 4090 (450W, ~40 Tokens/s, 0.089) 和 A100 (400W, ~60 Tokens/s, 0.15) 以评估能效比。

## Corrected Claim

RTX 5090 的 TDP 约为 575W（待官方确认），在特定 16K 上下文负载下，其能效比估算约为 0.175 Tokens/s/W（基于假设吞吐量 100 Tokens/s），需与 RTX 4090 和 A100 进行实际基准测试对比以评估能效。

## Evidence

[质询]RTX 5090 的 TDP 为 575W 属于经验事实（硬件规格），且该数值在发布前/后存在争议（部分早期泄露或官方规格可能不同，如 575W 是常见传闻值，但需确认是否为最终官方定值；此外，RTX 5090 的显存带宽和架构变化对 16K 上下文下的实际吞吐量影响巨大，直接假设 100 Tokens/s 缺乏严谨的基准测试支持，属于推测性数值）。 | 经验事实，逻辑自洽但缺来源支持。RTX 5090 的 TDP 和具体吞吐量均为经验数据，非第一性原理可推导。虽然 100/575 ≈ 0.175 的数学计算正确，但输入参数（TDP 575W, 吞吐 100 Tokens/s）缺乏可靠来源直接支持，且 16K 上下文下的实际性能受显存带宽限制，简单线性估算可能偏差较大。

## Search Query

RTX 5090 TDP 575W power efficiency LLM inference comparison RTX 4090 A100
