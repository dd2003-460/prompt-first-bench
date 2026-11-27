# N36: A100 80GB SXM4 单卡在 BF16 精度下运行 Qwen3-27B 32K 上下文的显存占用为 54GB(权重) + 36GB(KV Cache) 

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N6

## Claim

A100 80GB SXM4 单卡在 BF16 精度下运行 Qwen3-27B 32K 上下文的显存占用为 54GB(权重) + 36GB(KV Cache) + 5GB(激活/框架) ≈ 95GB，大于 80GB 物理显存，必须启用 CPU Offload 或降低精度至 FP8/INT8

## Corrected Claim

A100 80GB SXM4 单卡在 BF16 精度下运行 Qwen3-27B 32K 上下文的显存占用预计超过 80GB（权重约 54GB，KV Cache 及激活开销视具体架构配置而定，通常需额外 30-40GB+），因此必须启用 CPU Offload 或降低精度至 FP8/INT8 以适配单卡显存。

## Evidence

[质询]KV Cache 占用 36GB 的数值缺乏具体模型架构参数（如层数、头数、头维度）支持，且未考虑 GQA（分组查询注意力）对 KV Cache 的显著缩减作用，该数值可能偏高或基于特定未说明的配置；此外，5GB 激活/框架开销在 32K 长上下文下可能偏低，实际峰值可能更高，导致总显存估算存在不确定性。 | 先验知识/题面给定，逻辑校验通过：权重 54GB (27B * 2 bytes) 合理；KV Cache 36GB 在 32K 上下文下量级合理（取决于具体架构，但非明显错误）；总显存 95GB > 80GB 结论逻辑自洽，但具体分项数值缺乏来源直接支持，且 KV Cache 计算依赖未明示的架构细节，故降级为定性表述。
