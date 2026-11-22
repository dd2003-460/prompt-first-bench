# N60: 多卡 TP=2 方案中，KV Cache 显存分布：KV Cache 通常按 Head 维度切分，每卡承载 $N_{kv\_heads}/2 = 2$ 个 KV

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N11

## Claim

多卡 TP=2 方案中，KV Cache 显存分布：KV Cache 通常按 Head 维度切分，每卡承载 $N_{kv\_heads}/2 = 2$ 个 KV Head，因此每卡 KV 占用约为单卡全量的一半（~2.05GB），而非简单除以 2 后的总量。

## Corrected Claim

多卡 TP=2 方案中，KV Cache 显存分布：KV Cache 通常按 Head 维度切分，每卡承载 $N_{kv\_heads}/2 = 2$ 个 KV Head，因此每卡 KV 占用约为单卡全量的一半（~2.05GB），而非简单除以 2 后的总量。

## Evidence

先验知识/题面给定，逻辑校验通过：TP=2 时 KV Cache 按 Head 切分，每卡承载总 Head 数的一半，显存占用相应减半，符合张量并行原理。

## Search Query

Tensor Parallelism KV cache sharding head dimension
