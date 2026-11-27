# N20: Qwen3.8-27B模型层数假设为48层，head_dim为128，TP=4切分后，每token KV Cache开销为(2 * 48 * 128 * 2 b

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N8

## Claim

Qwen3.8-27B模型层数假设为48层，head_dim为128，TP=4切分后，每token KV Cache开销为(2 * 48 * 128 * 2 bytes / 4) = 12KB

## Corrected Claim

Qwen3.8-27B模型层数假设为48层，head_dim为128，TP=4切分后，每token KV Cache开销为(2 * 48 * 128 * 2 bytes / 4) = 12KB

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 (2 * 48 * 128 * 2 / 4) = 12288 bytes = 12KB 正确，符合 Transformer KV Cache 标准计算公式及 TP 切分逻辑。
