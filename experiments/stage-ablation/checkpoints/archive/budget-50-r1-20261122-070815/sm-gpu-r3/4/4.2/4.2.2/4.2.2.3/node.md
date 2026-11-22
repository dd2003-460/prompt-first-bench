# N307: A100 运行 Qwen3-27B BF16 时的吞吐量受 2039 GB/s 带宽限制，理论上限约为 2039 / (54+2) ≈ 36 tok/s，实际受

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N106

## Claim

A100 运行 Qwen3-27B BF16 时的吞吐量受 2039 GB/s 带宽限制，理论上限约为 2039 / (54+2) ≈ 36 tok/s，实际受计算瓶颈影响可能更低，需搜索实测数据以校准能效比计算

## Corrected Claim

A100 SXM 运行 Qwen3-27B BF16 时，若仅考虑权重加载带宽限制（2039 GB/s / ~54 GB），理论上限约为 37 tok/s；实际吞吐量受计算瓶颈、KV Cache 及系统开销影响，通常低于此值，需实测数据校准。

## Evidence

[质询]该陈述包含具体的硬件规格（A100带宽2039 GB/s）和模型参数（Qwen3-27B），属于经验事实。虽然A100 SXM的带宽确为2039 GB/s，但Qwen3-27B的具体参数量及BF16下的精确字节数需核实（通常27B模型BF16权重约54GB，计算逻辑成立，但缺乏来源直接支持该特定组合的实测或理论上限结论）。此外，'实际受计算瓶颈影响可能更低'是定性描述，但'理论上限约为36 tok/s'是基于纯带宽限制的简化估算，未考虑KV Cache等额外内存开销，且缺乏外部来源验证该具体数值。 | 经验事实，逻辑自洽但缺来源支持。A100 SXM带宽2039 GB/s为已知硬件规格，27B模型BF16权重约54GB，2039/54≈37.7，与36 tok/s量级一致，但无检索来源直接支持该特定场景的吞吐量结论。

## Search Query

A100 Qwen 27B BF16 inference throughput tokens per second vLLM
