# N243: 单POP CPU瓶颈的并发请求数上限修正：考虑TLS握手开销（约0.5ms/req）和GC停顿，实际单核处理能力 Q_core = 1000ms / (0.3m

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N78

## Claim

单POP CPU瓶颈的并发请求数上限修正：考虑TLS握手开销（约0.5ms/req）和GC停顿，实际单核处理能力 Q_core = 1000ms / (0.3ms + 0.5ms + 0.2ms) ≈ 500 req/s；16核服务器总并发 Q_max_corrected = 16 × 500 = 8,000 req/s，对应带宽上限 8,000 × 1.5MB ≈ 9.6 Gbps，高于纯计算模型估算的5 Gbps。

## Corrected Claim

单POP CPU瓶颈的并发请求数上限修正：考虑TLS握手开销（约0.5ms/req）和GC停顿，实际单核处理能力 Q_core = 1000ms / (0.3ms + 0.5ms + 0.2ms) ≈ 500 req/s；16核服务器总并发 Q_max_corrected = 16 × 500 = 8,000 req/s，对应带宽上限 8,000 × 1.5MB ≈ 9.6 Gbps，高于纯计算模型估算的5 Gbps。
