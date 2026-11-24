# N70: HDD层重建所需盘数计算：400TB冷数据/5TB每盘=80块盘，RAID6(N-2)有效容量需物理容量=400/(N-2)/N，假设N=84块5TB盘，物理总

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N20, N21, N22

## Claim

HDD层重建所需盘数计算：400TB冷数据/5TB每盘=80块盘，RAID6(N-2)有效容量需物理容量=400/(N-2)/N，假设N=84块5TB盘，物理总容量420TB，重建时需读取82块好盘并写入2块新盘

## Corrected Claim

HDD层重建所需盘数计算：400TB冷数据/5TB每盘=80块盘，RAID6(N-2)有效容量需物理容量=400/(N-2)/N，假设N=84块5TB盘，物理总容量420TB，重建时需读取82块好盘并写入2块新盘

## Evidence

父节点级核验失败（LLM 错误）：Unterminated string starting at: line 8 column 5 (char 744)
