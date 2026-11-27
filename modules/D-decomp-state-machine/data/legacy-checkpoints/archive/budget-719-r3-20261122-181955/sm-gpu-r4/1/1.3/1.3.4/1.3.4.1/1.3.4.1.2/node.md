# N523: 修正 N182 中 KV Cache 估算错误：基于已确认事实 N370/N372，Qwen3-27B 在 BF16 下 KV Cache per token 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N182

## Claim

修正 N182 中 KV Cache 估算错误：基于已确认事实 N370/N372，Qwen3-27B 在 BF16 下 KV Cache per token 为 256 KB (而非 N182 隐含的 n_kv_heads=32 导致的更大值)，32K 上下文单请求 KV Cache 占用为 8 GB (而非 8.59 GB)；因此单请求总显存需求 = 54 GB (权重) + 8 GB (KV) + 2 GB (框架/激活) = 64 GB，仍远小于 192 GB 显存，但并发能力计算需基于 8 GB/req 而非 8.59 GB/req。

## Corrected Claim

修正 N182 中 KV Cache 估算错误：基于已确认事实 N370/N372，Qwen3-27B 在 BF16 下 KV Cache per token 为 256 KB (而非 N182 隐含的 n_kv_heads=32 导致的更大值)，32K 上下文单请求 KV Cache 占用为 8 GB (而非 8.59 GB)；因此单请求总显存需求 = 54 GB (权重) + 8 GB (KV) + 2 GB (框架/激活) = 64 GB，仍远小于 192 GB 显存，但并发能力计算需基于 8 GB/req 而非 8.59 GB/req。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B 架构参数（GQA, n_kv_heads=8, head_dim=128, layers=64）推导 KV Cache 为 256KB/token，32K 上下文为 8GB，总显存 64GB 符合物理直觉且与 192GB 显存对比合理。
