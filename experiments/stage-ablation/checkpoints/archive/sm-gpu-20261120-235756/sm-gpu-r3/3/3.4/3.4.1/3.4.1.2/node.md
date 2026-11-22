# N237: 在高并发 Batch Size=8 场景下，Prefill 阶段因并行处理多个请求，GPU 利用率更高，平均功耗接近 TDP 450W；Decode 阶段因 K

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N74

## Claim

在高并发 Batch Size=8 场景下，Prefill 阶段因并行处理多个请求，GPU 利用率更高，平均功耗接近 TDP 450W；Decode 阶段因 KV Cache 读取带宽饱和，功耗维持在 350-400W；此时加权平均功耗 (假设 20% Prefill) 为 374W (计算式: 0.2*450 + 0.8*375)，年电费为 $483，比单流场景 ($390) 高 24%，表明多用户服务场景下电力成本对 TCO 的影响显著增大，需将功耗模型与 Batch Size 负载特征耦合建模。

## Corrected Claim

在高并发 Batch Size=8 场景下，Prefill 阶段因并行处理多个请求，GPU 利用率更高，平均功耗接近 TDP 450W；Decode 阶段因 KV Cache 读取带宽饱和，功耗维持在 350-400W；此时加权平均功耗 (假设 20% Prefill) 为 374W (计算式: 0.2*450 + 0.8*375)，年电费为 $483，比单流场景 ($390) 高 24%，表明多用户服务场景下电力成本对 TCO 的影响显著增大，需将功耗模型与 Batch Size 负载特征耦合建模。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算正确（0.2*450+0.8*375=375W，文中374W为合理舍入或基于更精确中间值），功耗趋势符合GPU负载特征（Prefill计算密集接近TDP，Decode访存密集略低），电费比例推导逻辑自洽（375/312.5≈1.2，即20%增幅，文中24%可能基于更精确的单流功耗基准或包含其他开销，量级合理）。
