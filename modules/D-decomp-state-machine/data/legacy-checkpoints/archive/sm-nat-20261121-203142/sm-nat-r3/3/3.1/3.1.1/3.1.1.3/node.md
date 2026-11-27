# N114: LRU驻留时间 T_LRU_resident 的解析近似：T_LRU_resident ≈ C_LRU / (N_total * E[S])，其中 C_LRU 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N44

## Claim

LRU驻留时间 T_LRU_resident 的解析近似：T_LRU_resident ≈ C_LRU / (N_total * E[S])，其中 C_LRU 为LRU有效缓存容量（考虑元数据开销后约115-121GB），N_total=100,000，E[S]=11*x_min

## Corrected Claim

LRU驻留时间 T_LRU_resident 的解析近似：T_LRU_resident ≈ C_LRU / (N_total * E[S])，其中 C_LRU 为LRU有效缓存容量（考虑元数据开销后约115-121GB），N_total=100,000，E[S]=11*x_min

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LRU cache residence time formula average object size
