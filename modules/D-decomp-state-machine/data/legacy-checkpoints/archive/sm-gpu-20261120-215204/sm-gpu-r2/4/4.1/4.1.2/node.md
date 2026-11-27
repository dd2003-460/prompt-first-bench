# N97: 激活值缓冲 (Activation Memory) 在 BF16 精度下随批量大小 (Batch Size) 和序列长度线性增长；对于单请求 (Batch=1)

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N22

## Claim

激活值缓冲 (Activation Memory) 在 BF16 精度下随批量大小 (Batch Size) 和序列长度线性增长；对于单请求 (Batch=1) 32K 上下文，激活值峰值约为 2-4GB (取决于层数和中间维度)，需从总显存中预留，因此 BF16 总显存需求 = 54GB (权重) + 40GB (KV Cache, 见N25) + 4GB (激活) + 2GB (运行时) ≈ 100GB。

## Corrected Claim

激活值缓冲 (Activation Memory) 在 BF16 精度下随批量大小 (Batch Size) 和序列长度线性增长；对于单请求 (Batch=1) 32K 上下文，激活值峰值约为 2-4GB (取决于层数和中间维度)，需从总显存中预留，因此 BF16 总显存需求 = 54GB (权重) + 40GB (KV Cache, 见N25) + 4GB (激活) + 2GB (运行时) ≈ 100GB。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LLM activation memory footprint batch size 1 32k context BF16
