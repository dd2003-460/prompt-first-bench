# N93: Batch Size=1 时，单卡推理吞吐量计算公式：Tokens_per_sec = Memory_Bandwidth_GB_s / (Weight_Byte

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N17

## Claim

Batch Size=1 时，单卡推理吞吐量计算公式：Tokens_per_sec = Memory_Bandwidth_GB_s / (Weight_Bytes_per_Token + KV_Read_Bytes_per_Token)，其中 Memory_Bandwidth_GB_s 取自 N18 的实测/标称值。

## Corrected Claim

Batch Size=1 时，单卡推理吞吐量计算公式：Tokens_per_sec = Memory_Bandwidth_GB_s / (Weight_Bytes_per_Token + KV_Read_Bytes_per_Token)，其中 Memory_Bandwidth_GB_s 取自 N18 的实测/标称值。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

single card inference throughput formula batch size 1 memory bandwidth
