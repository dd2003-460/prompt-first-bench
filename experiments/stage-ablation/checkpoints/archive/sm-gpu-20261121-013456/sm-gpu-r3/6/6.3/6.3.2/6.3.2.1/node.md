# N262: A100 80GB 在 Qwen3-27B BF16 下的实测吞吐量：基于 vLLM 0.6.x 版本，A100 80GB PCIe 运行 Qwen3-27B 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N102

## Claim

A100 80GB 在 Qwen3-27B BF16 下的实测吞吐量：基于 vLLM 0.6.x 版本，A100 80GB PCIe 运行 Qwen3-27B BF16 的吞吐量约为 45-50 tokens/s（来源：NVIDIA 基准测试，[时效待核]），该值高于 2×4090 的 28 tokens/s，是切换至 A100 的性能依据。

## Corrected Claim

A100 80GB 可运行 Qwen3-27B BF16，基于 vLLM 的实测吞吐量受并发和上下文长度影响显著，具体数值需根据实际负载配置确定，通常高于 2×4090 的 28 tokens/s。

## Evidence

[质询]来源[1]描述的是双A100（2x A100）在vLLM 0.19.1下的性能，且未提供具体的tokens/s数值，无法直接支持单卡A100在vLLM 0.6.x下45-50 tokens/s的具体数值；此外，Qwen3-27B BF16模型大小约54GB，单卡A100 80GB虽可容纳，但KV Cache空间受限，实际吞吐受并发和上下文长度影响极大，45-50 tokens/s这一具体数值缺乏该特定配置下的直接证据支持。 | 来源[1]主题相关（A100+Qwen3-27B+vLLM）但配置不同（双卡 vs 单卡，版本不同），且未提供具体吞吐数值，仅能间接佐证A100可运行该模型，无法直接支持具体吞吐量数值，属于经验事实缺直接来源支持。

## Search Query

NVIDIA A100 80GB Qwen3-27B BF16 vLLM throughput tokens per second

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2040488166298228423&rut=eb494b4607dab43cd4463424cebca1077176e83c53311721536b1d53d3f94e39', 'type': 'ddg', 'title': '在双 A100 上部署 Qwen3.6-27B，两轮 vLLM 调优后 128K 吞吐提升约 20%——实测结论与配置'}
