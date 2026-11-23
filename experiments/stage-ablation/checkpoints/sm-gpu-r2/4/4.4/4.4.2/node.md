# N68: 高敏感性变量判定实例：以 H100 方案为例，TCO ≈ $30k + $1.8k (3yr power) = $31.8k，Throughput = 50 t

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N19

## Claim

高敏感性变量判定实例：以 H100 方案为例，TCO ≈ $30k + $1.8k (3yr power) = $31.8k，Throughput = 50 tokens/s，Quality_Score = 1.0。∂Ranking/∂P_price = 1/50 = 0.02 (低敏感)；∂Ranking/∂T_throughput = -31.8k / (2500 * 1) = -12.72 (高敏感，|∂| > 0.5)；∂Ranking/∂E_power = 3/50 = 0.06 (低敏感)。结论：吞吐量是最高敏感性变量，其 ±20% 扰动将导致 Ranking 变化 ±20%，需在决策矩阵中单独列出。

## Corrected Claim

高敏感性变量判定实例：以 H100 方案为例，TCO ≈ $30k + $1.8k (3yr power) = $31.8k，Throughput = 50 tokens/s，Quality_Score = 1.0。∂Ranking/∂P_price = 1/50 = 0.02 (低敏感)；∂Ranking/∂T_throughput = -31.8k / (2500 * 1) = -12.72 (高敏感，|∂| > 0.5)；∂Ranking/∂E_power = 3/50 = 0.06 (低敏感)。结论：吞吐量是最高敏感性变量，其 ±20% 扰动将导致 Ranking 变化 ±20%，需在决策矩阵中单独列出。

## Evidence

先验知识/题面给定，逻辑校验通过：基于 TCO/Throughput 的排名定义，吞吐量作为分母，其相对变化直接导致排名的等比例反向变化（弹性为1），数值推导自洽。
