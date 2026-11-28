# N178: N51的T_memory主导项计算：T_mem = Bytes_KV_Cache_Read / Bandwidth_HBM，其中Bytes_KV_Cache_R

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N51

## Claim

N51的T_memory主导项计算：T_mem = Bytes_KV_Cache_Read / Bandwidth_HBM，其中Bytes_KV_Cache_Read = Batch_Size × Seq_Len × KV_Per_Token_Bytes，Bandwidth_HBM = 900 GB/s (V100 SXM2理论值)，此公式揭示了吞吐量与序列长度成正比的瓶颈机制

## Corrected Claim

N51的T_memory主导项计算：T_mem = Bytes_KV_Cache_Read / Bandwidth_HBM，其中Bytes_KV_Cache_Read = Batch_Size × Seq_Len × KV_Per_Token_Bytes，Bandwidth_HBM = 900 GB/s (V100 SXM2理论值)，此公式揭示了吞吐量与序列长度成正比的瓶颈机制

## Evidence

先验知识/题面给定，逻辑校验通过：V100 SXM2 HBM带宽约900GB/s符合硬件规格，KV Cache读取量与Batch Size及Seq Len成正比符合LLM推理内存访问模型，公式推导逻辑自洽。
