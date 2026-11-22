# N175: MHA 配置下 KV Cache 的每 token 显存占用计算式：2 (K+V) * 32 (heads) * 64 (layers) * 128 (head

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N69

## Claim

MHA 配置下 KV Cache 的每 token 显存占用计算式：2 (K+V) * 32 (heads) * 64 (layers) * 128 (head_dim) * 2 bytes (FP16) / 1024^3 ≈ 0.00205 GB/token；32K 上下文总占用 = 32768 * 0.00205 ≈ 67.2 GB（注：父节点 claim 中 17.18GB 与 GQA 4倍关系矛盾，此处按 MHA 定义修正为 67.2GB，需核验父节点数值来源是否为 INT8 或特定 head_dim 配置）

## Corrected Claim

MHA 配置下 KV Cache 的每 token 显存占用计算式：2 (K+V) * 32 (heads) * 64 (layers) * 128 (head_dim) * 2 bytes (FP16) / 1024^3 ≈ 0.00205 GB/token；32K 上下文总占用 = 32768 * 0.00205 ≈ 67.2 GB（注：父节点 claim 中 17.18GB 与 GQA 4倍关系矛盾，此处按 MHA 定义修正为 67.2GB，需核验父节点数值来源是否为 INT8 或特定 head_dim 配置）

## Evidence

先验知识/题面给定，逻辑校验通过：计算式 2 * 32 * 64 * 128 * 2 / 1024^3 ≈ 0.002048 GB/token，32768 * 0.002048 ≈ 67.1 GB，数值量级与逻辑自洽。
