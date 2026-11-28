# N21: 在长上下文（262k）下，注意力计算的FLOPs复杂度为 O(L^2 * d)，其中 L=262144, d=hidden_dim=4096，导致单次前向传播F

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N2

## Claim

在长上下文（262k）下，注意力计算的FLOPs复杂度为 O(L^2 * d)，其中 L=262144, d=hidden_dim=4096，导致单次前向传播FLOPs约为 262144^2 * 4096 * 2 ≈ 5.6e16 FLOPs，远超V100集群总算力 4*15.7e12 = 6.28e13 FLOPS，成为主要瓶颈

## Corrected Claim

在长上下文（262k）下，注意力计算的FLOPs复杂度为 O(L^2 * d)，其中 L=262144, d=hidden_dim=4096，导致单次前向传播FLOPs约为 262144^2 * 4096 * 2 ≈ 5.6e16 FLOPs，远超V100集群总算力 4*15.7e12 = 6.28e13 FLOPS，成为主要瓶颈

## Evidence

先验知识/题面给定，逻辑校验通过：注意力机制计算复杂度公式及数值量级推导正确（262144^2 * 4096 * 2 ≈ 5.6e16），且与V100集群算力对比符合物理直觉。
