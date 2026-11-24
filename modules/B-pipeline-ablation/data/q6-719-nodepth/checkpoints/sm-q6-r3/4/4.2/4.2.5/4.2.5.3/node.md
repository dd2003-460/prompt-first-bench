# N350: 回源传输延迟 T_transfer_origin 对 P99 的贡献：T_transfer_origin = s_object / B_link，其中 B_li

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N108

## Claim

回源传输延迟 T_transfer_origin 对 P99 的贡献：T_transfer_origin = s_object / B_link，其中 B_link 为 POP 到源站的专线带宽（典型 10-100Gbps），对于 s_object=1MB，T_transfer ≈ 0.1-1ms；对于 s_object=10MB，T_transfer ≈ 1-10ms

## Corrected Claim

回源传输延迟 T_transfer_origin 对 P99 的贡献：T_transfer_origin = s_object / B_link，其中 B_link 为 POP 到源站的专线带宽（典型 10-100Gbps），对于 s_object=1MB，T_transfer ≈ 0.1-1ms；对于 s_object=10MB，T_transfer ≈ 1-10ms

## Evidence

先验知识/题面给定，逻辑校验通过：1MB/10Gbps=0.8ms, 1MB/100Gbps=0.08ms, 10MB/10Gbps=8ms, 10MB/100Gbps=0.8ms，数值量级与带宽范围匹配，符合物理直觉。
