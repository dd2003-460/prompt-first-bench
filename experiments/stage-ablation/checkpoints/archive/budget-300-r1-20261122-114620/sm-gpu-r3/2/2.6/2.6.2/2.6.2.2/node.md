# N260: Qwen3-27B 在 BF16 精度下的权重总字节数 N_weights_bytes 为 54 GB (27e9 params * 2 bytes/param

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N80

## Claim

Qwen3-27B 在 BF16 精度下的权重总字节数 N_weights_bytes 为 54 GB (27e9 params * 2 bytes/param)，此为 Decode 阶段每个 token 生成必须从显存读取的最小数据量。

## Corrected Claim

Qwen3-27B 在 BF16 精度下的权重总字节数 N_weights_bytes 为 54 GB (27e9 params * 2 bytes/param)，此为 Decode 阶段每个 token 生成必须从显存读取的最小数据量。

## Evidence

先验知识/题面给定，逻辑校验通过：27e9参数 * 2字节/参数 = 54e9字节 ≈ 54GB，计算正确且符合BF16精度定义。

## Search Query

Qwen3-27B BF16 weight size 54 GB
