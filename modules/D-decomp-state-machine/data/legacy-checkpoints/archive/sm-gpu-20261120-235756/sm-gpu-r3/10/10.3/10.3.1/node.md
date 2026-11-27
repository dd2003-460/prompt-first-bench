# N349: AMD MI300X 的官方 TDP 为 750W，但实际推理负载下的功耗通常在 400W-600W 之间（取决于 Batch Size 和上下文长度），导致实

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N132, N133, N134

## Claim

AMD MI300X 的官方 TDP 为 750W，但实际推理负载下的功耗通常在 400W-600W 之间（取决于 Batch Size 和上下文长度），导致实际年电费成本在 $590-$885 之间，而非基于 TDP 峰值计算的 $986。

## Corrected Claim

AMD MI300X 的官方 TDP 为 750W，实际推理负载下的功耗通常低于 TDP 峰值（具体数值取决于负载类型），导致实际年电费成本低于基于 TDP 峰值计算的估算值。

## Evidence

[质询]具体数值（400W-600W 功耗区间及 $590-$885 电费）缺乏公开权威数据支持，且电费计算隐含了特定的电价假设（约 $0.10/kWh），不同地区电价差异巨大，导致具体金额不具备普适性。 | 经验事实，逻辑自洽但缺来源支持。MI300X TDP 750W 为已知事实，推理负载低于峰值符合物理直觉，但具体功耗区间和电费数值无外部来源佐证，且电费高度依赖电价假设。

## Search Query

AMD MI300X actual power consumption inference benchmark watts
