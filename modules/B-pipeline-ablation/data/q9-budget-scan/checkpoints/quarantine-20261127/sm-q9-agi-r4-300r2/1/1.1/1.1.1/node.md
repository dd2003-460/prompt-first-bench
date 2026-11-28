# N29: CUDA Context 显存开销实测值为 1.5-2.0 GB（针对 4x V100-SXM2 集群初始化状态），使得单卡物理 16GB 的实际可用显存降至 

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N6, N7, N8

## Claim

CUDA Context 显存开销实测值为 1.5-2.0 GB（针对 4x V100-SXM2 集群初始化状态），使得单卡物理 16GB 的实际可用显存降至 14.0-14.5 GB，而非理论最大值。

## Corrected Claim

CUDA Context 显存开销实测值为 1.5-2.0 GB（针对 4x V100-SXM2 集群初始化状态），使得单卡物理 16GB 的实际可用显存降至 14.0-14.5 GB，而非理论最大值。

## Evidence

父节点级核验失败（LLM 错误）：Expecting ',' delimiter: line 8 column 201 (char 885)

## Search Query

V100 SXM2 CUDA context memory overhead GB
