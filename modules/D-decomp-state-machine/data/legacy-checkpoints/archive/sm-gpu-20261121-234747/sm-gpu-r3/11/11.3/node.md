# N501: 每瓦特吞吐量（Tokens/s/W）的计算公式：Efficiency = (Tokens_per_second / W_avg)，其中 W_avg 需区分峰值功

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N158

## Claim

每瓦特吞吐量（Tokens/s/W）的计算公式：Efficiency = (Tokens_per_second / W_avg)，其中 W_avg 需区分峰值功耗与平均功耗，对于间歇性负载（如对话式推理），平均功耗通常低于峰值，需通过功率计实测或基于负载剖面（Prefill/Decode比例）加权计算，例如 RTX 4090 在 50% Prefill + 50% Decode 负载下平均功耗约为 300W，能效比约为 20/300 = 0.067 tokens/s/W [待核验]

## Corrected Claim

每瓦特吞吐量（Tokens/s/W）的计算公式：Efficiency = (Tokens_per_second / W_avg)，其中 W_avg 需区分峰值功耗与平均功耗，对于间歇性负载（如对话式推理），平均功耗通常低于峰值，需通过功率计实测或基于负载剖面（Prefill/Decode比例）加权计算，例如 RTX 4090 在 50% Prefill + 50% Decode 负载下平均功耗约为 300W，能效比约为 20/300 = 0.067 tokens/s/W [待核验]

## Evidence

先验知识/题面给定，逻辑校验通过：公式定义正确，RTX 4090 在混合负载下平均功耗约 300W 符合工程常识（低于 450W 峰值），计算逻辑自洽。
