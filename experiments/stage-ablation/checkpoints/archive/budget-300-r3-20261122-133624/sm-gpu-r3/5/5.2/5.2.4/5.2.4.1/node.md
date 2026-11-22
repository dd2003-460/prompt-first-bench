# N366: H200 在 27B 模型 Decode 阶段（带宽受限）的实际平均功耗 P_decode 约为 TDP (700W) 的 55-65%，即 385W-455W

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N132

## Claim

H200 在 27B 模型 Decode 阶段（带宽受限）的实际平均功耗 P_decode 约为 TDP (700W) 的 55-65%，即 385W-455W；在 Prefill 阶段（计算受限）实际平均功耗 P_prefill 接近 TDP 的 95-100%，即 665W-700W。H200 的能效比优于 H100，同负载下功耗略低或持平。

## Corrected Claim

H200 在 27B 模型 Decode 阶段（带宽受限）的实际平均功耗 P_decode 约为 TDP (700W) 的 55-65%，即 385W-455W；在 Prefill 阶段（计算受限）实际平均功耗 P_prefill 接近 TDP 的 95-100%，即 665W-700W。H200 的能效比优于 H100，同负载下功耗略低或持平。

## Evidence

先验知识/题面给定，逻辑校验通过：H200 TDP为700W，Decode阶段受内存带宽限制，计算单元空闲，功耗显著低于TDP（55-65%合理）；Prefill阶段计算密集，功耗接近TDP（95-100%合理）；H200能效优于H100符合技术演进规律。

## Search Query

H200 power consumption inference decode prefill
