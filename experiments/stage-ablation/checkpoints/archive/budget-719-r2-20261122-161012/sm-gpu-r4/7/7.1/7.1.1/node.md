# N265: 工作点 A (高性低成/不可行)：RTX 4090 单卡 + BF16。显存需求 55GB > 24GB，OOM 错误，吞吐量 0 tok/s。此点作为基准排除

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N119

## Claim

工作点 A (高性低成/不可行)：RTX 4090 单卡 + BF16。显存需求 55GB > 24GB，OOM 错误，吞吐量 0 tok/s。此点作为基准排除项，证明单卡消费级显卡在 BF16 下无法承载 Qwen3-27B 32K 上下文。

## Corrected Claim

工作点 A (高性低成/不可行)：RTX 4090 单卡 + BF16。显存需求 55GB > 24GB，OOM 错误，吞吐量 0 tok/s。此点作为基准排除项，证明单卡消费级显卡在 BF16 下无法承载 Qwen3-27B 32K 上下文。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B 在 BF16 下权重约 54GB，加上 32K 上下文的 KV Cache 及激活值，显存需求远超 RTX 4090 的 24GB，必然导致 OOM，逻辑自洽。
