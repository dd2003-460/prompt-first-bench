# N157: 工作点 C (大小-热度强负相关)：当 ρ=-0.3 较强时，LFU 保留的小而热对象在字节命中率上优势更大，ΔH_byte > ΔH_req，具体差值取决于 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N54

## Claim

工作点 C (大小-热度强负相关)：当 ρ=-0.3 较强时，LFU 保留的小而热对象在字节命中率上优势更大，ΔH_byte > ΔH_req，具体差值取决于 E[S|LFU_hit] / E[S|LRU_hit] 的比值，需通过 Copula 模拟计算。

## Corrected Claim

工作点 C (大小-热度强负相关)：当 ρ=-0.3 较强时，LFU 保留的小而热对象在字节命中率上优势更大，ΔH_byte > ΔH_req，具体差值取决于 E[S|LFU_hit] / E[S|LRU_hit] 的比值，需通过 Copula 模拟计算。

## Evidence

先验知识/题面给定，逻辑校验通过
