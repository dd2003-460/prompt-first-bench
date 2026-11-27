# N115: 驻留时间比值 R_residence 的计算：R_residence = T_LFU_resident / T_LRU_resident = (C_LFU / 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N44

## Claim

驻留时间比值 R_residence 的计算：R_residence = T_LFU_resident / T_LRU_resident = (C_LFU / (N_hot * E[S_hot])) / (C_LRU / (N_total * E[S]))，由于 C_LFU ≈ C_LRU，简化为 R_residence = (N_total * E[S]) / (N_hot * E[S_hot])，需代入头部对象平均大小 E[S_hot] 计算具体比值

## Corrected Claim

驻留时间比值 R_residence 的计算：R_residence = T_LFU_resident / T_LRU_resident = (C_LFU / (N_hot * E[S_hot])) / (C_LRU / (N_total * E[S]))，由于 C_LFU ≈ C_LRU，简化为 R_residence = (N_total * E[S]) / (N_hot * E[S_hot])，需代入头部对象平均大小 E[S_hot] 计算具体比值

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LFU LRU residence time ratio calculation hot objects
