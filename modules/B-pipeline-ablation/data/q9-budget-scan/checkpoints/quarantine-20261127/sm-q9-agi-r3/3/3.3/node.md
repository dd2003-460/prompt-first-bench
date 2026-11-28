# N18: max_num_seqs=8 在 TP=4 配置下，当序列长度 > 16k tokens 时，KV cache 显存占用超过单卡 12.6 GB 可用空间，vL

- **status**: degraded
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N3

## Claim

max_num_seqs=8 在 TP=4 配置下，当序列长度 > 16k tokens 时，KV cache 显存占用超过单卡 12.6 GB 可用空间，vLLM 将自动降低 batch size 至 2-4，导致吞吐量下降 50-75%。

## Corrected Claim

max_num_seqs=8 在 TP=4 配置下，当序列长度 > 16k tokens 时，KV cache 显存占用可能超过单卡 12.6 GB 可用空间，vLLM 将自动降低 batch size，导致吞吐量显著下降。

## Evidence

[质询]吞吐量下降50-75%的具体数值缺乏通用基准支持，高度依赖具体模型架构（如注意力头数、层数）和硬件特性，属于特定场景下的经验观测值而非普适规律。 | 先验知识/题面给定，逻辑校验通过：KV cache随序列长度线性增长，长序列下显存受限导致batch size降低进而影响吞吐符合vLLM调度机制的基本逻辑，但具体百分比为经验估计。
