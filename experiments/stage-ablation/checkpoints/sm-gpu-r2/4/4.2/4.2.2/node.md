# N61: vLLM 社区基准测试 (vLLM Benchmark Suite) 针对 Qwen3-27B 在 H100 80GB 上的典型复现值：batch_size=1

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N17

## Claim

vLLM 社区基准测试 (vLLM Benchmark Suite) 针对 Qwen3-27B 在 H100 80GB 上的典型复现值：batch_size=1, context_length=32K 时，Prefill 阶段吞吐约为 1500-2000 tokens/s，Decode 阶段吞吐约为 40-60 tokens/s (FP8)；该数据来自 GitHub vLLM 仓库 issue 或 HuggingFace 社区 benchmark 帖子。

## Corrected Claim

vLLM 社区基准测试显示，Qwen3-27B 在 H100 80GB 上（batch_size=1, context_length=32K, FP8）的 Prefill 吞吐通常在千级 tokens/s，Decode 吞吐在几十 tokens/s 量级，具体数值需参考最新社区实测数据。

## Evidence

[质询]具体数值（1500-2000 tokens/s prefill, 40-60 tokens/s decode）属于高度依赖硬件配置、软件版本及量化精度的经验事实，且缺乏来源支持，无法排除因配置差异导致数值偏差的可能性。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

vLLM benchmark Qwen3-27B H100 32k context decode tokens per second
