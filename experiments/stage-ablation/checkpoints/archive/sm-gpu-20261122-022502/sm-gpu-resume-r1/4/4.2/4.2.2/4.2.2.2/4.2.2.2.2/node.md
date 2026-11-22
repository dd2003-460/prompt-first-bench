# N807: RTX 4090 之间通过 PCIe 4.0 x16 互联的有效带宽约为 32 GB/s (理论 64 GB/s 的一半，因全双工共享及协议开销)，因此传输 2

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N251, N252, N253

## Claim

RTX 4090 之间通过 PCIe 4.0 x16 互联的有效带宽约为 32 GB/s (理论 64 GB/s 的一半，因全双工共享及协议开销)，因此传输 27 GB 激活值的纯通信时间 T_transfer = 27 GB / 32 GB/s = 0.84375 s ≈ 844 ms。

## Corrected Claim

RTX 4090 之间通过 PCIe 4.0 x16 互联的有效带宽约为 32 GB/s (理论 64 GB/s 的一半，因全双工共享及协议开销)，因此传输 27 GB 激活值的纯通信时间 T_transfer = 27 GB / 32 GB/s = 0.84375 s ≈ 844 ms。

## Evidence

先验知识/题面给定，逻辑校验通过：PCIe 4.0 x16 理论双向带宽约 64 GB/s，考虑协议开销后有效带宽约 32 GB/s 符合工程常识；27 GB / 32 GB/s = 0.84375 s 计算正确。
