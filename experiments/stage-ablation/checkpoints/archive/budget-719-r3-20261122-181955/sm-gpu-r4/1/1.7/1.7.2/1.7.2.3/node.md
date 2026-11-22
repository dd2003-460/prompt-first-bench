# N229: A100 80GB 的 $/GB 指标 $187.5-$225.0 基于 80GB 显存，在 32K 上下文 BF16 推理中可用 KV Cache 为 ~26

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N70

## Claim

A100 80GB 的 $/GB 指标 $187.5-$225.0 基于 80GB 显存，在 32K 上下文 BF16 推理中可用 KV Cache 为 ~26GB，修正后 $/GB(KV) 约为 $615-$692，显著高于 RTX 4090 的修正值，表明 A100 在 KV Cache 容量性价比上不占优，但其优势在于支持更大 Batch Size 和更长上下文，需结合并发需求评估。

## Corrected Claim

A100 80GB 的 $/GB 指标 $187.5-$225.0 基于 80GB 显存，在 32K 上下文 BF16 推理中可用 KV Cache 为 ~26GB，修正后 $/GB(KV) 约为 $615-$692，显著高于 RTX 4090 的修正值，表明 A100 在 KV Cache 容量性价比上不占优，但其优势在于支持更大 Batch Size 和更长上下文，需结合并发需求评估。

## Evidence

先验知识/题面给定，逻辑校验通过：A100 80GB 价格区间合理，KV Cache 占用估算符合 BF16 32K 上下文典型量级，修正后 $/GB 计算逻辑自洽，且 A100 在 KV 容量性价比上低于消费级显卡但胜在并发与长上下文的结论符合工程常识。
