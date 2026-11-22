# N169: Batch=2 时的总显存需求计算：权重 27GB + KV Cache 16GB (8GB*2) + 框架开销 4GB = 47GB，仍超出单卡 RTX 40

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N49, N50, N51

## Claim

Batch=2 时的总显存需求计算：权重 27GB + KV Cache 16GB (8GB*2) + 框架开销 4GB = 47GB，仍超出单卡 RTX 4090 (24GB) 容量，确认单卡无法支持 Batch=2 的 INT8 推理。

## Corrected Claim

Batch=2 时的总显存需求计算：权重 27GB + KV Cache 16GB (8GB*2) + 框架开销 4GB = 47GB，仍超出单卡 RTX 4090 (24GB) 容量，确认单卡无法支持 Batch=2 的 INT8 推理。

## Evidence

先验知识/题面给定，逻辑校验通过：27+16+4=47GB > 24GB，算术正确且符合显存占用基本逻辑
