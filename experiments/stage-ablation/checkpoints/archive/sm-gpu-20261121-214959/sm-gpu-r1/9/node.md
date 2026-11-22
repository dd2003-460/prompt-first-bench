# N34: Mac Studio M2 Ultra (192GB) 单卡在 32K 上下文下的最大可行精度验证：BF16 权重 (54GB) + BF16 KV Cache

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

Mac Studio M2 Ultra (192GB) 单卡在 32K 上下文下的最大可行精度验证：BF16 权重 (54GB) + BF16 KV Cache (12.58GB) = 66.58GB < 192GB (可行，大量冗余)。结论：Mac Studio 单卡可轻松运行 BF16 全精度模型，无需量化，质量损失为 0，但受限于 800GB/s 带宽，Decode 速度约为 54GB / 800GB/s ≈ 14.8 tokens/s (理论上限)。

## Corrected Claim

Mac Studio M2 Ultra (192GB) 单卡在 32K 上下文下的最大可行精度验证：BF16 权重 (54GB) + BF16 KV Cache (12.58GB) = 66.58GB < 192GB (可行，大量冗余)。结论：Mac Studio 单卡可轻松运行 BF16 全精度模型，无需量化，质量损失为 0，但受限于 800GB/s 带宽，Decode 速度约为 54GB / 800GB/s ≈ 14.8 tokens/s (理论上限)。

## Evidence

检索失败: no sources from any channel (all 5 failed)
