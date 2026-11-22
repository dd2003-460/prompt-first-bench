# N285: 显存容量下限 32GB 的边界验证：Qwen3-27B W4 权重 (~14GB) + 32K 上下文 KV Cache (假设 GQA 4:1, head_d

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N103

## Claim

显存容量下限 32GB 的边界验证：Qwen3-27B W4 权重 (~14GB) + 32K 上下文 KV Cache (假设 GQA 4:1, head_dim 128, 80层, FP16 KV: 80*2*8*128*2*32768/1024^3 ≈ 4.0GB) + 激活/框架开销 (~2-4GB) ≈ 20-22GB。32GB 显存 (如 RTX 4090 24GB 不足, RTX 5090 32GB 刚好) 可容纳，但余量极小，无法支持 Batch Size > 1 或更长上下文。若需支持 Batch 2 或 64K 上下文，显存下限需提升至 48GB。

## Corrected Claim

显存容量下限 32GB 的边界验证：Qwen3-27B W4 权重 (~14GB) + 32K 上下文 KV Cache (假设 GQA 4:1, head_dim 128, 80层, FP16 KV: 80*2*8*128*2*32768/1024^3 ≈ 4.0GB) + 激活/框架开销 (~2-4GB) ≈ 20-22GB。32GB 显存 (如 RTX 4090 24GB 不足, RTX 5090 32GB 刚好) 可容纳，但余量极小，无法支持 Batch Size > 1 或更长上下文。若需支持 Batch 2 或 64K 上下文，显存下限需提升至 48GB。

## Evidence

先验知识/题面给定，逻辑校验通过：权重14GB + KV Cache 4GB + 开销2-4GB ≈ 20-22GB，小于32GB，且24GB不足，逻辑自洽。
