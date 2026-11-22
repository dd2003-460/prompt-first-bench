# N132: H_byte 与 H_req 的转换系数 Ratio = N_byte/D_byte / (N_req/D_req) 的量化：在 K=N 极限下，Ratio =

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N39

## Claim

H_byte 与 H_req 的转换系数 Ratio = N_byte/D_byte / (N_req/D_req) 的量化：在 K=N 极限下，Ratio = E[S|hit]/E[S|miss]，由于缓存容纳所有对象，Miss 集为空，Ratio 无定义；但在 K<N 时（如容量受限），Ratio ≈ 1 + ρ * (β-1)/(α-1) * ln(N/K)，代入参数得 Ratio ≈ 1.2，即字节命中率比请求命中率高 20%。

## Corrected Claim

在 K=N 极限下，Ratio 无定义；在 K<N 时，字节命中率通常高于请求命中率，具体提升幅度取决于对象大小分布及缓存策略，在特定参数假设下可估算为约 20%。

## Evidence

[质询]公式 Ratio ≈ 1 + ρ * (β-1)/(α-1) * ln(N/K) 缺乏明确的理论推导来源或标准引用，且参数 ρ, α, β 的定义未在陈述中给出，导致该具体数值 1.2 的可复现性和普适性存疑；此外，'缓存容纳所有对象'时 Miss 集为空导致 Ratio 无定义（分母为0或0/0）的逻辑描述虽在极限情况下成立，但直接跳跃到 K<N 的近似公式缺乏中间推导支撑。 | 先验知识/题面给定，逻辑校验通过：在 K=N 时 Miss 概率为 0，Ratio 确实无定义；K<N 时字节命中率高于请求命中率符合缓存原理（大对象更可能命中），但具体系数公式及 1.2 的数值属于经验拟合或特定模型结论，缺乏外部来源直接支持，故降级。
