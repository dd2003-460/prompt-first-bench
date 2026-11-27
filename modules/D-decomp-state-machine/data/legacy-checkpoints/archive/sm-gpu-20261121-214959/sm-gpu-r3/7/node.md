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

父节点级核验通过：正交+完备+无冗余（由于只有一个子节点，正交性和冗余性检查自动通过。该子节点精准地深入验证了父节点中‘可行’结论的关键前提（即剩余显存是否足以支撑运行时的激活值和系统开销），没有遗漏父节点中的其他关键分支（如INT4+BF16的溢出情况属于已排除的无效路径，无需单独拆解），因此完备性合格。）
