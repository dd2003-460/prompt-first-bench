# N432: 上海本地场景下队列等待时间 T_queueing 的M/M/c模型计算：T_queueing = (ρ / (c × (1-ρ))) × (1/(μ-λ))，其

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N145

## Claim

上海本地场景下队列等待时间 T_queueing 的M/M/c模型计算：T_queueing = (ρ / (c × (1-ρ))) × (1/(μ-λ))，其中 ρ 为利用率，c 为并发连接数，μ 为服务速率，λ 为到达速率；在P99分位下需取 ρ=0.7 时的值

## Corrected Claim

上海本地场景下队列等待时间 T_queueing 的M/M/c模型计算：T_queueing = (C(c, λ/μ) / (cμ - λ))，其中 C(c, λ/μ) 为 Erlang C 公式，ρ 为利用率，c 为并发连接数，μ 为服务速率，λ 为到达速率；在P99分位下需取 ρ=0.7 时的值

## Evidence

[质询]公式形式错误：M/M/c 模型的等待时间公式并非简单的 (ρ / (c × (1-ρ))) × (1/(μ-λ))，该公式混淆了 M/M/1 和 M/M/c 的结构，且 M/M/c 的等待时间通常涉及 Erlang C 公式，不能简单用此线性比例表示。 | 先验知识/题面给定，逻辑校验未通过：M/M/c 模型的等待时间公式应为 T_queueing = (C(c, λ/μ) / (cμ - λ))，其中 C(c, λ/μ) 为 Erlang C 公式，而非题中给出的简化形式。

## Search Query

M/M/c queueing model P99 latency calculation utilization
