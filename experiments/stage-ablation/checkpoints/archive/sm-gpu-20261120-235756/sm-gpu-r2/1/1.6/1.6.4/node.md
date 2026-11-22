# N54: W4A16的TPOT优势：权重体积仅为BF16的1/4，理论TPOT降低约75%，在显存带宽受限场景（如RTX 4090 1008GB/s）下，W4A16的吞吐

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N12

## Claim

W4A16的TPOT优势：权重体积仅为BF16的1/4，理论TPOT降低约75%，在显存带宽受限场景（如RTX 4090 1008GB/s）下，W4A16的吞吐可达BF16的3-4倍，是低显存高吞吐场景的首选。

## Corrected Claim

W4A16的TPOT优势：权重体积仅为BF16的1/4，理论TPOT降低约75%，在显存带宽受限场景（如RTX 4090 1008GB/s）下，W4A16的吞吐可达BF16的3-4倍，是低显存高吞吐场景的首选。

## Evidence

先验知识/题面给定，逻辑校验通过：W4A16权重体积为BF16的1/4，在显存带宽受限场景下，理论吞吐提升与带宽节省比例一致，符合基本物理/经济直觉。

## Search Query

W4A16 inference throughput vs BF16 memory bandwidth bound
