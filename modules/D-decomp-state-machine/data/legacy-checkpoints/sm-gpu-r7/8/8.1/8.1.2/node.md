# N262: H100 SXM5 在 Batch Size=1、序列长度=128 的 Decode 阶段（内存带宽密集）实际功耗为 450W-550W，此时 GPU 计算单元

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N81

## Claim

H100 SXM5 在 Batch Size=1、序列长度=128 的 Decode 阶段（内存带宽密集）实际功耗为 450W-550W，此时 GPU 计算单元空闲率高，功耗显著低于 TDP，主要受 HBM 访问功耗驱动。

## Corrected Claim

H100 SXM5 在 Batch Size=1、序列长度=128 的 Decode 阶段（内存带宽密集）实际功耗为 450W-550W，此时 GPU 计算单元空闲率高，功耗显著低于 TDP，主要受 HBM 访问功耗驱动。

## Evidence

先验知识/题面给定，逻辑校验通过：H100 SXM5 TDP为700W，Decode阶段（BS=1, Seq=128）为内存带宽受限场景，计算单元利用率低，功耗主要由HBM访问驱动，450W-550W符合该工况下的典型功耗区间（显著低于TDP但高于纯待机功耗）。
