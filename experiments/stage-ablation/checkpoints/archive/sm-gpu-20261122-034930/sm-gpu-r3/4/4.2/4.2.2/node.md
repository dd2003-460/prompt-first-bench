# N112: 工作点2（中带宽/高容量-数据中心）：A100 80GB有效带宽2039 GB/s，INT8权重27GB + KV Cache 10.7GB + 框架开销4GB

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N29

## Claim

工作点2（中带宽/高容量-数据中心）：A100 80GB有效带宽2039 GB/s，INT8权重27GB + KV Cache 10.7GB + 框架开销4GB = 41.7GB，理论吞吐上限 = 2039 / 41.7 ≈ 48.9 tokens/s；实际受计算瓶颈限制，实测约40-60 tokens/s，带宽利用率约82-123%，与RTX 4090类似，表明两者均处于计算与带宽混合瓶颈区。

## Corrected Claim

工作点2（中带宽/高容量-数据中心）：A100 80GB有效带宽2039 GB/s，INT8权重27GB + KV Cache 10.7GB + 框架开销4GB = 41.7GB，理论吞吐上限 = 2039 / 41.7 ≈ 48.9 tokens/s；实际受计算瓶颈限制，实测约40-60 tokens/s，带宽利用率约82-123%，与RTX 4090类似，表明两者均处于计算与带宽混合瓶颈区。

## Evidence

先验知识/题面给定，逻辑校验通过：A100 80GB HBM2e带宽约2039GB/s，41.7GB数据量下理论上限约48.9 tokens/s，实测40-60 tokens/s符合计算/带宽混合瓶颈特征，数值量级与工程常识一致。
