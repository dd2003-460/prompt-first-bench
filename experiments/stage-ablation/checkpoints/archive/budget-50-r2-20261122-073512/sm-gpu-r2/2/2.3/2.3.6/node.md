# N106: Mac Pro M2 Ultra 512GB 单卡运行 Qwen3-27B 的显存可行性：BF16 权重 54GB + KV Cache (128MB/seq)

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N15

## Claim

Mac Pro M2 Ultra 512GB 单卡运行 Qwen3-27B 的显存可行性：BF16 权重 54GB + KV Cache (128MB/seq) + Overhead (2GB) ≈ 56.1GB < 512GB，显存可行，支持多并发。

## Corrected Claim

Mac Pro M2 Ultra 512GB 单卡运行 Qwen3-27B 的显存可行性：BF16 权重 54GB + KV Cache (128MB/seq) + Overhead (2GB) ≈ 56.1GB < 512GB，显存可行，支持多并发。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B 在 BF16 下权重约 54GB，加上少量 KV Cache 和 Overhead 总显存占用远低于 512GB，数值量级合理且逻辑自洽。
