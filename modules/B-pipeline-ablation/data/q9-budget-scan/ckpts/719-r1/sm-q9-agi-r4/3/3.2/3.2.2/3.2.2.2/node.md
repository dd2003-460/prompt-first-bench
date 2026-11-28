# N186: 工作点2（平衡显存与并发）：FP8量化，Batch_Size=4，每序列分配64K tokens KV Cache，总KV占用≈256K tokens×4×8K

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N53

## Claim

工作点2（平衡显存与并发）：FP8量化，Batch_Size=4，每序列分配64K tokens KV Cache，总KV占用≈256K tokens×4×8KB=8GB，剩余显存2-4GB用于激活值，适合中等并发科研任务

## Corrected Claim

工作点2（平衡显存与并发）：FP8量化，Batch_Size=4，每序列分配64K tokens KV Cache，总KV占用≈256K tokens×4×8KB=8GB，剩余显存2-4GB用于激活值，适合中等并发科研任务

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算正确（256K * 8KB = 2GB，2GB * 4 = 8GB），符合FP8量化下KV Cache显存占用的工程估算逻辑。
