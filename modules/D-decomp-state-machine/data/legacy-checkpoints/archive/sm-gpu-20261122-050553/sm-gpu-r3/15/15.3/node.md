# N352: A100 40GB 方案的条件性边界：仅在用户要求单卡部署且接受 FP8 KV Cache（3GB 缺口填充）时成立；若用户要求 BF16 KV Cache，A

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N121

## Claim

A100 40GB 方案的条件性边界：仅在用户要求单卡部署且接受 FP8 KV Cache（3GB 缺口填充）时成立；若用户要求 BF16 KV Cache，A100 40GB 亦不可行，需升级至 A100 80GB 或 H100 80GB，成本增加 $10000-$20000。

## Corrected Claim

A100 40GB 方案的条件性边界：仅在用户要求单卡部署且接受 FP8 KV Cache（3GB 缺口填充）时成立；若用户要求 BF16 KV Cache，A100 40GB 亦不可行，需升级至 A100 80GB 或 H100 80GB，成本增加 $10000-$20000。

## Evidence

先验知识/题面给定，逻辑校验通过：A100 40GB显存限制下，FP8 KV Cache相比BF16减半，可填补3GB缺口实现单卡部署；若坚持BF16则显存不足，需升级至80GB卡，成本增加符合市场规律。
