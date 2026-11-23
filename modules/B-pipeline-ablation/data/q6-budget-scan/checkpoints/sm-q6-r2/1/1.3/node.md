# N8: 排队延迟T_queue的M/M/c模型参数：T_queue = 1/(μ - λ) * (1 - ρ)，其中λ为请求到达率（req/s），μ为单边缘节点服务速率

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N1

## Claim

排队延迟T_queue的M/M/c模型参数：T_queue = 1/(μ - λ) * (1 - ρ)，其中λ为请求到达率（req/s），μ为单边缘节点服务速率（req/s），ρ = λ/(cμ)为利用率，c为并发连接数；P99对应99分位排队时间

## Corrected Claim

M/M/c 模型的排队延迟 T_queue 通常通过 Erlang C 公式计算：T_queue = (C(c, λ/μ) / (cμ - λ))，其中 C(c, λ/μ) 是 Erlang C 概率，表示请求需要等待的概率。

## Evidence

父节点级核验未通过：不完备（子节点正交且无冗余，但存在关键遗漏。父节点明确定义了 M/M/c 模型，但子节点仅覆盖了 λ、μ、c 三个输入参数，完全缺失了核心输出指标 T_queue 的具体计算逻辑（如利用 Erlang C 公式计算等待概率 Wq，再乘以服务时间 1/μ 得到 T_queue）。此外，子节点3提到的‘自相似性修正’属于模型局限性说明，而非 M/M/c 模型本身的参数分解，导致对‘P99对应99分位排队时间’这一关键输出的推导过程缺失。）

## Search Query

M/M/c queue P99 latency formula utilization
