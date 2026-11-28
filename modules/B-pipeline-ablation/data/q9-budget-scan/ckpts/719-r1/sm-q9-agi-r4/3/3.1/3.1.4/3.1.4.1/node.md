# N178: N51的T_memory主导项计算：T_mem = Bytes_KV_Cache_Read / Bandwidth_HBM，其中Bytes_KV_Cache_R

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N51

## Claim

N51的T_memory主导项计算：T_mem = Bytes_KV_Cache_Read / Bandwidth_HBM，其中Bytes_KV_Cache_Read = Batch_Size × Seq_Len × KV_Per_Token_Bytes，Bandwidth_HBM = 900 GB/s (V100 SXM2理论值)，此公式揭示了吞吐量与序列长度成正比的瓶颈机制

## Corrected Claim

N51的T_memory主导项计算：T_mem = Bytes_KV_Cache_Read / Bandwidth_HBM，其中Bytes_KV_Cache_Read = Batch_Size × Seq_Len × KV_Per_Token_Bytes，Bandwidth_HBM = 900 GB/s (V100 SXM2理论值)，此公式揭示了吞吐量与序列长度成正比的瓶颈机制

## Evidence

父节点级核验未通过：不完备（子节点通过不同的工作点（长序列、中序列、短序列）从不同维度验证了父节点公式的适用性和瓶颈转移机制，彼此之间逻辑独立且互不矛盾，满足正交性；无冗余。但父节点核心是‘公式揭示吞吐量与序列长度的瓶颈机制’，子节点仅展示了三个离散点的数值计算和定性结论，缺乏对‘为什么随序列长度变化导致主导项切换’的理论推导或中间状态覆盖（例如中等长度下的过渡区域），未能完全解释‘机制’本身的动态过程，因此完备性不足。）
