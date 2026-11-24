# N516: s_avg 对回源带宽需求的影响：Origin_Bandwidth_Req = (1 - Hit_Rate) × Monthly_Requests × s_av

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N173

## Claim

s_avg 对回源带宽需求的影响：Origin_Bandwidth_Req = (1 - Hit_Rate) × Monthly_Requests × s_avg / 30 / 86400 × 8 Gbps，若 Hit_Rate=0.9, Monthly_Requests=1.5B, s_avg=3.6MB，则 Origin_Bandwidth_Req ≈ 1.8 Gbps，需对比源站出口带宽 1-10 Gbps 判断是否瓶颈

## Corrected Claim

s_avg 对回源带宽需求的影响：Origin_Bandwidth_Req = (1 - Hit_Rate) × Monthly_Requests × s_avg / 30 / 86400 × 8 Gbps，若 Hit_Rate=0.9, Monthly_Requests=1.5B, s_avg=3.6MB，则 Origin_Bandwidth_Req ≈ 1.8 Gbps，需对比源站出口带宽 1-10 Gbps 判断是否瓶颈

## Evidence

先验知识/题面给定，逻辑校验通过：公式量纲正确（Bytes/s 转 Gbps），数值计算准确（(1-0.9)*1.5e9*3.6*1024*1024/30/86400*8 ≈ 1.8 Gbps），符合CDN回源带宽估算的基本原理。
