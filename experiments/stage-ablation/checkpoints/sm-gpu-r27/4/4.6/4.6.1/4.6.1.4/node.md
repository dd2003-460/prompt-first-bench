# N230: H100 SXM5 在 LLaMA-70B FP16 下，batch_size=1 时的 TTFT (Time-to-First-Token) 约为 2-3 秒

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N73

## Claim

H100 SXM5 在 LLaMA-70B FP16 下，batch_size=1 时的 TTFT (Time-to-First-Token) 约为 2-3 秒，而 batch_size=32 时的 TTFT 约为 10-15 秒，TTFT 随 Batch Size 线性增加，主要受 Prompt Length 和 Attention FLOPS 限制。

## Corrected Claim

H100 SXM5 在 LLaMA-70B FP16 下，TTFT 随 Batch Size 增加而显著增加（具体数值需参考特定推理框架如 vLLM 或 TensorRT-LLM 的基准测试，通常 batch_size=1 时较低，batch_size=32 时因计算负载增加而升高），主要受 Prompt Length 和 Attention FLOPS 限制。

## Evidence

[质询]该陈述包含具体的经验性能数值（TTFT 2-3秒 vs 10-15秒）及线性增长结论，属于硬件/模型特定场景下的经验事实，无法从第一性原理直接推导，且参考来源中未包含针对 LLaMA-70B 在 H100 上的具体推理延迟基准测试数据。 | 逻辑上自洽（Batch Size 增加导致计算量线性增加，TTFT 随之增加符合直觉），但参考来源 [1] 和 [2] 无关，[3] 仅涉及 H100 内存带宽微观基准，未覆盖 LLM 推理 TTFT 具体数值，属于经验事实缺来源支持。

## Search Query

H100 SXM LLaMA-70B TTFT batch_size 1 vs 32

## Retrieval Sources

- {'url': 'https://github.com', 'type': None, 'title': 'direct-browser: github.com'}
- {'url': 'https://arxiv.org', 'type': None, 'title': 'direct-browser: arxiv.org'}
- {'url': 'http://arxiv.org/abs/2608.15764v1', 'type': 'arxiv', 'title': 'Concurrency Response of Plain Global Loads on the NVIDIA H100'}
