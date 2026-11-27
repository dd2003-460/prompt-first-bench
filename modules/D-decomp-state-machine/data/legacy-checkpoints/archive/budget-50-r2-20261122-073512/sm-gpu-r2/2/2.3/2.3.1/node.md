# N101: Mac Studio M2 Ultra 192GB 单卡运行 Qwen3-27B 的显存可行性：BF16 权重 54GB + KV Cache (128MB/s

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N15

## Claim

Mac Studio M2 Ultra 192GB 单卡运行 Qwen3-27B 的显存可行性：BF16 权重 54GB + KV Cache (128MB/seq) + Overhead (2GB) ≈ 56.1GB < 192GB，显存可行，支持多并发。

## Corrected Claim

Mac Studio M2 Ultra 192GB 单卡运行 Qwen3-27B 的显存可行性：BF16 权重 54GB + KV Cache (128MB/seq) + Overhead (2GB) ≈ 56.1GB < 192GB，显存可行，支持多并发。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B 参数量约 27B，BF16 精度下权重占用约 54GB，加上 KV Cache 和 Overhead 后总显存需求约 56.1GB，远小于 Mac Studio M2 Ultra 192GB 统一内存，显存可行性成立。
