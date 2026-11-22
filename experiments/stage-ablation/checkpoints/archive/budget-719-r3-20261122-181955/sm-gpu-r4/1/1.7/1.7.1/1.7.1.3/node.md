# N228: RTX 4090 的 $/GB 指标 $66.7-$79.2 基于 24GB 显存，但 24GB 在 32K 上下文 BF16 推理中不足以容纳 KV Cach

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N69

## Claim

RTX 4090 的 $/GB 指标 $66.7-$79.2 基于 24GB 显存，但 24GB 在 32K 上下文 BF16 推理中不足以容纳 KV Cache（需 ~33GB），因此该指标对本题场景无效；有效指标应为 $ / (可用 KV Cache GB)，在 INT4 量化下可用 KV Cache 为 ~10.5GB，修正后 $/GB(KV) 约为 $152-$181。

## Corrected Claim

RTX 4090 的 $/GB 指标 $66.7-$79.2 基于 24GB 显存，但 24GB 在 32K 上下文 BF16 推理中不足以容纳 KV Cache（需 ~33GB），因此该指标对本题场景无效；有效指标应为 $ / (可用 KV Cache GB)，在 INT4 量化下可用 KV Cache 为 ~10.5GB，修正后 $/GB(KV) 约为 $152-$181。

## Evidence

先验知识/题面给定，逻辑校验通过：24GB显存扣除模型权重及激活值后，剩余空间确实不足以容纳32K上下文BF16所需的~33GB KV Cache；INT4量化下KV Cache占用减半，可用空间估算及$/GB修正计算在量级和逻辑上均自洽。
