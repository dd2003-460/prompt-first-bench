# N354: 64K 上下文、BF16 精度下的总显存需求具体数值为 66.74 GB (54 GB 权重 + 10.74 GB KV + 2.0 GB 激活)，此值排除 R

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N123

## Claim

64K 上下文、BF16 精度下的总显存需求具体数值为 66.74 GB (54 GB 权重 + 10.74 GB KV + 2.0 GB 激活)，此值排除 RTX 4090 (24GB) 和 RTX 5090 (32GB)，仅数据中心卡 (A100/H100) 可行。

## Corrected Claim

64K 上下文、BF16 精度下的总显存需求具体数值为 66.74 GB (54 GB 权重 + 10.74 GB KV + 2.0 GB 激活)，此值排除 RTX 4090 (24GB) 和 RTX 5090 (32GB)，仅数据中心卡 (A100/H100) 可行。

## Evidence

先验知识/题面给定，逻辑校验通过：64K上下文下KV Cache占用约10.74GB，加上54GB权重和2GB激活，总显存需求66.74GB，确实超出RTX 4090/5090容量，需A100/H100等数据中心卡。
