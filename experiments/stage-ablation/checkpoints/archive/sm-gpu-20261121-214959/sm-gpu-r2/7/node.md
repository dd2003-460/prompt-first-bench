# N32: RTX 4090 (24GB) 单卡在 32K 上下文下的最大可行精度验证：INT4 权重 (13.5GB) + BF16 KV Cache (12.58GB)

- **status**: verified
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

RTX 4090 (24GB) 单卡在 32K 上下文下的最大可行精度验证：INT4 权重 (13.5GB) + BF16 KV Cache (12.58GB) = 26.08GB > 24GB (溢出)；INT4 权重 (13.5GB) + FP8 KV Cache (6.29GB) = 19.79GB < 24GB (可行，剩余 ~4.2GB 用于激活值/临时缓冲)。结论：单卡 4090 必须同时使用 INT4 权重和 FP8 KV Cache 才能满足 32K 容量下限。

## Corrected Claim

RTX 4090 (24GB) 单卡在 32K 上下文下的最大可行精度验证：INT4 权重 (13.5GB) + BF16 KV Cache (12.58GB) = 26.08GB > 24GB (溢出)；INT4 权重 (13.5GB) + FP8 KV Cache (6.29GB) = 19.79GB < 24GB (可行，剩余 ~4.2GB 用于激活值/临时缓冲)。结论：单卡 4090 必须同时使用 INT4 权重和 FP8 KV Cache 才能满足 32K 容量下限。

## Evidence

父节点级核验通过：正交+完备+无冗余（父节点的核心结论是确定‘INT4权重 + FP8 KV Cache’为唯一可行配置。子节点对该配置下的‘剩余显存余量是否足够支撑运行’进行了具体验证，这是父节点结论成立的必要前提（可行性验证）。子节点未重复父节点的计算过程，而是深入分析了余量的具体去向（激活值、CUDA开销等），逻辑上构成了‘配置选择’到‘配置验证’的完整闭环，无正交性问题，无冗余。）
