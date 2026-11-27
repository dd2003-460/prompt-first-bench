# N100: TP=2 的主要性能增益来自显存释放带来的 Batch Size 提升潜力：TP=4 受限于 KV Cache 只能支持 ~3 个 262k 并发，而 TP=2

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N52

## Claim

TP=2 的主要性能增益来自显存释放带来的 Batch Size 提升潜力：TP=4 受限于 KV Cache 只能支持 ~3 个 262k 并发，而 TP=2 支持 1 个 262k 或 ~50 个 5k 短序列并发；在科研场景多为短序列迭代 (5k-15k tokens) 的情况下，TP=2 可将有效 Batch Size 从 3 提升至 5-10，从而通过提高 GPU 利用率将 Decode 吞吐提升 20-50%。

## Corrected Claim

TP=2 的主要性能增益来自显存释放带来的 Batch Size 提升潜力：相比 TP=4，TP=2 能显著增加可用于 KV Cache 的显存，从而支持更大的并发 Batch Size（例如从个位数提升至十位数级别）；在科研场景多为短序列迭代的情况下，这种 Batch Size 的提升可通过提高 GPU 利用率带来显著的 Decode 吞吐增益。

## Evidence

[质询]数值量级与具体场景强耦合：'Batch Size 从 3 提升至 5-10' 及 '吞吐提升 20-50%' 是高度依赖具体硬件配置（如 H100/A100 显存大小）、模型架构（如 MoE vs Dense）及推理引擎优化程度的经验性估算，缺乏通用性，且 TP=2 下 KV Cache 的显存占用并未减半（权重减半但 KV Cache 通常仍分布在所有卡上或需特定配置），因此 Batch Size 的提升幅度可能被高估。 | 先验知识/题面给定，逻辑校验通过：TP 降低确实能释放显存用于 KV Cache，从而支持更大 Batch Size，进而提升 Decode 阶段 GPU 利用率；但具体数值（5-10倍提升、20-50% 吞吐增益）属于经验事实，在无外部来源支持且存在场景依赖性的情况下，降级为定性表述。
