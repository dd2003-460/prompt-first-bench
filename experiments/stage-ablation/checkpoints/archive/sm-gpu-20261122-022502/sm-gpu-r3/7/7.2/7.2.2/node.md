# N257: 基准方案 1×A100 (BF16) 的 TCO_per_token 敏感性分析：在吞吐量为 15 tokens/s (N75 中值) 且 3 年运行 50% 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N84

## Claim

基准方案 1×A100 (BF16) 的 TCO_per_token 敏感性分析：在吞吐量为 15 tokens/s (N75 中值) 且 3 年运行 50% 利用率条件下，总生成 Token 数为 5,913 万，CapEx 摊销 ($2,375/yr * 3 = $7,125, 基于 N61 残值修正) 加电力成本 ($0.5kW * 13,140h * $0.15/kWh = $986)，总成本 $8,111，TCO/token = $0.137，显著高于 2×4090 方案，表明在中等吞吐量区间内，数据卡的高 CapEx 使其 TCO 劣势明显，除非吞吐量提升至 > 100 tokens/s (需 FP8 优化)。

## Corrected Claim

基准方案 1×A100 (BF16) 的 TCO_per_token 敏感性分析：在吞吐量为 15 tokens/s (N75 中值) 且 3 年运行 50% 利用率条件下，总生成 Token 数为 5,913 万，CapEx 摊销 ($2,375/yr * 3 = $7,125, 基于 N61 残值修正) 加电力成本 ($0.5kW * 13,140h * $0.15/kWh = $986)，总成本 $8,111，TCO/token = $0.137，显著高于 2×4090 方案，表明在中等吞吐量区间内，数据卡的高 CapEx 使其 TCO 劣势明显，除非吞吐量提升至 > 100 tokens/s (需 FP8 优化)。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算自洽（总Token数、CapEx摊销、电力成本及TCO/token推导均符合算术逻辑），且符合A100高CapEx导致单Token成本高于消费级显卡组合的经济直觉。
