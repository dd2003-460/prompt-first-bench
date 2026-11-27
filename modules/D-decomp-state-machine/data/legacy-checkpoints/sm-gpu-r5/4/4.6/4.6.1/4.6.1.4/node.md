# N230: H100 SXM5 在 LLaMA-70B FP16 下，batch_size=1 时的 TTFT (Time-to-First-Token) 约为 2-3 秒

- **status**: pending
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N73

## Claim

H100 SXM5 在 LLaMA-70B FP16 下，batch_size=1 时的 TTFT (Time-to-First-Token) 约为 2-3 秒，而 batch_size=32 时的 TTFT 约为 10-15 秒，TTFT 随 Batch Size 线性增加，主要受 Prompt Length 和 Attention FLOPS 限制。

## Corrected Claim

H100 SXM5 在 LLaMA-70B FP16 下，TTFT 随 Batch Size 增加而显著增加，主要受 Prompt Length 和 Attention 计算量限制，具体数值取决于 Prompt 长度及推理引擎优化，通常 batch_size=1 时延迟较低，batch_size=32 时延迟显著升高。

## Evidence

[质询]数值量级与线性关系存疑：LLaMA-70B FP16 在 H100 SXM5 上，batch_size=1 的 TTFT 通常远低于 2-3 秒（取决于 Prompt 长度，短 Prompt 可能仅几十毫秒），且 TTFT 随 Batch Size 增加并非严格线性，而是受 Attention 计算复杂度（O(N^2) 或 O(N) 取决于实现）和内存带宽共同影响，简单断言‘线性增加’且给出具体秒数缺乏特定 Prompt 长度前提，属于经验事实且数值可能偏差较大。 | 参考来源 [1] 仅讨论 H100 内存带宽与并发响应，与 LLaMA-70B 推理延迟（TTFT）无关，无可用外部证据支持具体数值；该陈述为经验事实，逻辑上虽自洽（Batch 增加导致计算量增加），但缺乏来源直接支持且数值精度存疑，故降级。

## Search Query

H100 SXM LLaMA-70B TTFT batch_size 1 vs 32

## Retrieval Sources

- {'url': 'http://arxiv.org/abs/2608.15764v1', 'type': 'arxiv', 'title': 'Concurrency Response of Plain Global Loads on the NVIDIA H100'}
