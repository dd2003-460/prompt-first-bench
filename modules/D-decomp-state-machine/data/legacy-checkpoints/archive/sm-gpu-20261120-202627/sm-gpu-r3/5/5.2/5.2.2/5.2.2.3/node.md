# N381: A100 80GB SXM 的能效比 (Tokens/Joule) = Throughput (N121 值) / P_avg (N150 值)，例如 40 t

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N120, N121, N122

## Claim

A100 80GB SXM 的能效比 (Tokens/Joule) = Throughput (N121 值) / P_avg (N150 值)，例如 40 tokens/s / 320W = 0.125 tokens/J，用于与消费级方案 (如 15 tokens/s / 450W = 0.033 tokens/J) 进行单位能耗产出对比，量化'能效比优于双卡消费级方案'的具体倍数。

## Corrected Claim

A100 80GB SXM 的能效比 (Tokens/Joule) = Throughput (N121 值) / P_avg (N150 值)，例如 40 tokens/s / 320W = 0.125 tokens/J，用于与消费级方案 (如 15 tokens/s / 450W = 0.033 tokens/J) 进行单位能耗产出对比，量化'能效比优于双卡消费级方案'的具体倍数。

## Evidence

先验知识/题面给定，逻辑校验通过：能效比定义为单位能耗产出（Tokens/Joule），计算公式 Throughput/Power 量纲正确（tokens/s / W = tokens/J），数值示例 40/320=0.125 和 15/450≈0.033 计算无误，对比逻辑自洽。
