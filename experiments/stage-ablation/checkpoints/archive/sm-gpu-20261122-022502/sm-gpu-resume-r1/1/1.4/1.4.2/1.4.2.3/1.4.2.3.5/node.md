# N516: FP8 KV Cache 相对于 BF16 KV Cache 的精度损失在 32K 上下文下通常可忽略（<1% 困惑度增加），因为 FP8 E4M3/E5M2 

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N157

## Claim

FP8 KV Cache 相对于 BF16 KV Cache 的精度损失在 32K 上下文下通常可忽略（<1% 困惑度增加），因为 FP8 E4M3/E5M2 格式保留了足够的动态范围，是 RTX 5090 32GB 显存下兼顾容量与质量的首选 KV 精度。

## Corrected Claim

FP8 KV Cache 相对于 BF16 KV Cache 在 32K 上下文下通常具有可接受的精度损失，FP8 E4M3/E5M2 格式保留了足够的动态范围，是 RTX 5090 32GB 显存下兼顾容量与质量的常用 KV 精度选择。

## Evidence

[质询]将‘精度损失可忽略’与‘首选KV精度’混为一谈，且‘<1%困惑度增加’在32K长上下文下缺乏普遍性实证支持，不同模型和任务下FP8 KV Cache的精度损失可能显著高于1%，且‘首选’属于主观工程权衡而非绝对事实。 | 先验知识/题面给定，逻辑校验通过，但‘<1%’和‘首选’为经验性断言，缺乏来源直接支持，降级为定性表述。

## Search Query

FP8 KV cache perplexity impact vs BF16
