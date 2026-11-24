# N370: 对象传输时间 T_transfer_origin 的计算公式为 T_transfer = (s * 8) / B_origin_link，其中 s 为对象大小 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N114

## Claim

对象传输时间 T_transfer_origin 的计算公式为 T_transfer = (s * 8) / B_origin_link，其中 s 为对象大小 (MB)，B_origin_link 为源站出口带宽 (Mbps)。例如，s=1MB，B_origin_link=100Mbps，则 T_transfer ≈ 80ms；s=10MB，B_origin_link=100Mbps，则 T_transfer ≈ 800ms，这成为大文件回源的主要瓶颈。

## Corrected Claim

对象传输时间 T_transfer_origin 的计算公式为 T_transfer = (s * 8) / B_origin_link，其中 s 为对象大小 (MB)，B_origin_link 为源站出口带宽 (Mbps)。例如，s=1MB，B_origin_link=100Mbps，则 T_transfer ≈ 80ms；s=10MB，B_origin_link=100Mbps，则 T_transfer ≈ 800ms，这成为大文件回源的主要瓶颈。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 T=(s*8)/B 符合单位换算逻辑（MB转Mb除以Mbps得秒），数值计算 1*8/100=0.08s=80ms 及 10*8/100=0.8s=800ms 准确无误。

## Search Query

file transfer time calculation origin bandwidth 100Mbps 10MB
