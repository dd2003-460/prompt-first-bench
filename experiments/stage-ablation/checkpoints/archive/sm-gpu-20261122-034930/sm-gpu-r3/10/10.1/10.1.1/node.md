# N414: RTX 4090 INT8推理Qwen3-27B (32K ctx)的实测吞吐率22 tokens/s仅适用于Seq_len ≤ 8K的场景；当Seq_len=

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N149

## Claim

RTX 4090 INT8推理Qwen3-27B (32K ctx)的实测吞吐率22 tokens/s仅适用于Seq_len ≤ 8K的场景；当Seq_len=32K时，由于KV Cache读取量从~1.3GB增至~10.7GB，Memory-bound占比显著上升，实测吞吐率将降至约14-16 tokens/s（基于带宽模型修正：1008GB/s / (27GB权重 + 10.7GB KV + 4GB开销) ≈ 26.7理论值，但长序列下Kernel效率下降系数约为0.55-0.60）。

## Corrected Claim

RTX 4090 INT8推理Qwen3-27B (32K ctx)的实测吞吐率22 tokens/s仅适用于Seq_len ≤ 8K的场景；当Seq_len=32K时，由于KV Cache读取量显著增加，Memory-bound占比上升，实测吞吐率预计将显著降低（具体数值需实测验证，理论估算约为14-16 tokens/s）。

## Evidence

[质询]该陈述包含具体的硬件性能实测数据（22 tokens/s, 14-16 tokens/s）和特定的模型/硬件组合（RTX 4090, Qwen3-27B），属于经验事实。虽然带宽模型的逻辑推导（Memory-bound 导致吞吐下降）在物理上自洽，但具体的数值（如 22 tokens/s 和 14-16 tokens/s）无法从第一性原理严格推出，且缺乏外部来源支持。此外，'Qwen3-27B' 的具体存在性及在 RTX 4090 上的具体表现属于特定经验数据，若无来源证实，不能视为 verified。 | 经验事实，逻辑自洽但缺来源支持。带宽模型修正逻辑合理（KV Cache 增大导致 Memory-bound 加剧，吞吐下降），但具体数值缺乏外部证据验证。

## Search Query

RTX 4090 Qwen3-27B INT8 vLLM throughput 32k context length benchmark
