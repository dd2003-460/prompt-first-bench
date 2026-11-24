# N198: 自建POP入向带宽需求计算：Inbound_Peak_Mbps = (Upload_Traffic_Mbps + Miss_Download_Traffic_M

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N64

## Claim

自建POP入向带宽需求计算：Inbound_Peak_Mbps = (Upload_Traffic_Mbps + Miss_Download_Traffic_Mbps) × Peak_Factor_Inbound，其中Upload_Traffic = 0.2TB/day ≈ 296 Mbps，Miss_Download = 2TB × (1-H) ≈ 100GB (若H=95%) ≈ 148 Mbps，总入向Avg ≈ 444 Mbps，峰值约1110-1776 Mbps

## Corrected Claim

自建POP入向带宽需求计算：Inbound_Peak_Mbps = (Upload_Traffic_Mbps + Miss_Download_Traffic_Mbps) × Peak_Factor_Inbound，其中Upload_Traffic = 0.2TB/day ≈ 296 Mbps，Miss_Download = 2TB × (1-H) ≈ 100GB (若H=95%) ≈ 148 Mbps，总入向Avg ≈ 444 Mbps，峰值约1110-1776 Mbps

## Evidence

先验知识/题面给定，逻辑校验通过：0.2TB/day换算为296Mbps正确，2TB*5%=100GB换算为148Mbps正确，总和444Mbps正确，峰值系数2.5-4倍符合常规工程估算。
