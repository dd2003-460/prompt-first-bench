# N186: 在 M/M/1 排队模型中，若服务速率 μ = 100 req/min (1.67 req/s) 且利用率 ρ = 0.8，则平均等待时间 W_q = ρ/(μ

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N72

## Claim

在 M/M/1 排队模型中，若服务速率 μ = 100 req/min (1.67 req/s) 且利用率 ρ = 0.8，则平均等待时间 W_q = ρ/(μ(1-ρ)) ≈ 2.4s；但 vLLM 或 API 网关通常采用 FIFO 或多队列，实际 P99 延迟受突发流量影响，需引入 M/G/1 修正项或实测 P99/W_q 比值（通常为 2-5 倍）来校准调度超时阈值。

## Corrected Claim

在 M/M/1 排队模型中，若服务速率 μ = 100 req/min (1.67 req/s) 且利用率 ρ = 0.8，则平均等待时间 W_q = ρ/(μ(1-ρ)) ≈ 2.4s；但 vLLM 或 API 网关通常采用 FIFO 或多队列，实际 P99 延迟受突发流量影响，需引入 M/G/1 修正项或实测 P99/W_q 比值（通常为 2-5 倍）来校准调度超时阈值。

## Evidence

先验知识/题面给定，逻辑校验通过：M/M/1 公式 W_q = ρ/(μ(1-ρ)) 代入 μ=1.67 req/s, ρ=0.8 计算得 2.4s，数值准确；P99 与均值比值 2-5 倍符合排队论及工程经验常识。

## Search Query

M/M/1 queueing theory P99 latency ratio bursty traffic
