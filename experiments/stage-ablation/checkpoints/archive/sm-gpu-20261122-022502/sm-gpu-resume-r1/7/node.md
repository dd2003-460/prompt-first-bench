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

父节点级核验通过：正交+完备+无冗余（父节点的核心结论是确定可行的配置组合（INT4+FP8）并指出剩余显存需用于激活值/缓冲。子节点专门针对这一剩余显存（4.21GB）进行详细拆解和可行性验证（覆盖激活值、CUDA上下文、框架缓冲），逻辑上是对父节点结论的深入论证，没有重复父节点的计算过程（INT4+BF16溢出等），也没有矛盾。由于只有一个子节点，不存在子节点间的正交性或冗余问题。）
