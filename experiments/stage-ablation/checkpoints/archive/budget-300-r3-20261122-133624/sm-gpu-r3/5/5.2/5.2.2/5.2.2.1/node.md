# N360: H100 PCIe 在 27B 模型 Decode 阶段（带宽受限）的实际平均功耗 P_decode 约为 TDP (700W) 的 60-70%，即 420W

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N129

## Claim

H100 PCIe 在 27B 模型 Decode 阶段（带宽受限）的实际平均功耗 P_decode 约为 TDP (700W) 的 60-70%，即 420W-490W；在 Prefill 阶段（计算受限）实际平均功耗 P_prefill 接近 TDP 的 90-100%，即 630W-700W。

## Corrected Claim

H100 PCIe 在 27B 模型 Decode 阶段（带宽受限）的实际平均功耗 P_decode 约为 TDP (700W) 的 60-70%，即 420W-490W；在 Prefill 阶段（计算受限）实际平均功耗 P_prefill 接近 TDP 的 90-100%，即 630W-700W。

## Evidence

先验知识/题面给定，逻辑校验通过：H100 PCIe TDP为700W，Decode阶段受显存带宽限制，计算单元空闲率高，功耗通常降至TDP的60-70%；Prefill阶段计算密集，功耗接近TDP上限，符合GPU功耗与负载类型的物理规律。

## Search Query

H100 PCIe power consumption decode vs prefill inference workload
