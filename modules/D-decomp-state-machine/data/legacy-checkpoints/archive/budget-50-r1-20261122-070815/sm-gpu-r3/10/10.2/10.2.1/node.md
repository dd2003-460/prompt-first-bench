# N420: Qwen3-27B 在 RTX 4090 上 BF16 精度下的实测吞吐量（tokens/s），作为基准值，需从社区实测报告（如 Reddit r/LocalL

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N146

## Claim

Qwen3-27B 在 RTX 4090 上 BF16 精度下的实测吞吐量（tokens/s），作为基准值，需从社区实测报告（如 Reddit r/LocalLLaMA 或 GitHub issues）获取，注意区分 prefill 和 decode 阶段。

## Corrected Claim

Qwen3-27B 在 RTX 4090 上 BF16 精度下的实测吞吐量（tokens/s）需根据具体上下文长度和并发设置从社区实测报告获取，通常 prefill 阶段吞吐量远高于 decode 阶段，具体数值需查阅最新社区数据。

## Evidence

[质询]该陈述声称存在一个具体的“实测吞吐量”数值作为基准，但实际吞吐量高度依赖于上下文长度、并发数、量化方式及驱动版本，不存在单一的固定数值；且当前检索无可用来源，无法验证具体数值。 | 经验事实，逻辑自洽但缺来源支持（检索失败，无外部证据）

## Search Query

Qwen3-27B RTX 4090 vLLM BF16 throughput tokens per second
