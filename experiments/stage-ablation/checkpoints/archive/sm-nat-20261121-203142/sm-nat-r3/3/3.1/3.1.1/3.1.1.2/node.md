# N113: LFU驻留时间 T_LFU_resident 的解析近似：T_LFU_resident ≈ C_LFU / (N_hot * E[S_hot])，其中 C_LF

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N44

## Claim

LFU驻留时间 T_LFU_resident 的解析近似：T_LFU_resident ≈ C_LFU / (N_hot * E[S_hot])，其中 C_LFU 为LFU有效缓存容量（考虑计数器开销后约115-121GB），N_hot 为头部对象数量，E[S_hot] 为头部对象平均大小

## Corrected Claim

LFU驻留时间 T_LFU_resident 的解析近似：T_LFU_resident ≈ C_LFU / (N_hot * E[S_hot])，其中 C_LFU 为LFU有效缓存容量（考虑计数器开销后约115-121GB），N_hot 为头部对象数量，E[S_hot] 为头部对象平均大小

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LFU cache residence time formula hot objects
