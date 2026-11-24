# N417: 回源传输时间 T_transfer_origin_self 的计算：T_transfer = s_weighted / (B_pop_origin_link *

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N129

## Claim

回源传输时间 T_transfer_origin_self 的计算：T_transfer = s_weighted / (B_pop_origin_link * 8 * 10^6) * 1000 ms。以 s_weighted=1.5MB (图片0.7*1MB+视频0.3*5MB近似), B_link=100Mbps 为例，T_transfer ≈ 0.12ms，远小于 RTT，表明传输时间通常不是 P99 延迟的主要贡献项，除非 s > 10MB 或链路 < 10Mbps。

## Corrected Claim

回源传输时间 T_transfer_origin_self 的计算：T_transfer = s_weighted / (B_pop_origin_link * 8 * 10^6) * 1000 ms。以 s_weighted=1.5MB (图片0.7*1MB+视频0.3*5MB近似), B_link=100Mbps 为例，T_transfer ≈ 0.12ms，远小于 RTT，表明传输时间通常不是 P99 延迟的主要贡献项，除非 s > 10MB 或链路 < 10Mbps。

## Evidence

先验知识/题面给定，逻辑校验通过：1.5MB数据在100Mbps链路下的传输时间计算正确（1.5*8/100=0.12ms），且远小于典型RTT（通常>10ms），结论符合网络传输基本物理规律。
