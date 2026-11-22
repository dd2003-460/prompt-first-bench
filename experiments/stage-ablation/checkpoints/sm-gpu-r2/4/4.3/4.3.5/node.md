# N113: 1x RTX 4090 + 128GB DDR5 的混合架构中，若 offload 比例为 50%，则实际解码吞吐量受限于 PCIe 带宽 64 GB/s 和 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N23

## Claim

1x RTX 4090 + 128GB DDR5 的混合架构中，若 offload 比例为 50%，则实际解码吞吐量受限于 PCIe 带宽 64 GB/s 和 DDR5 带宽 2.304 TB/s 的瓶颈，理论最大解码吞吐量约为 min(64 / (13.5 * 0.5), 2304 / (13.5 * 0.5)) ≈ 9.48 tokens/s。

## Corrected Claim

1x RTX 4090 + 128GB DDR5 的混合架构中，若 offload 比例为 50%，则实际解码吞吐量受限于 PCIe 带宽 64 GB/s 和 DDR5 带宽 2.304 TB/s 的瓶颈，理论最大解码吞吐量约为 min(64 / (13.5 * 0.5), 2304 / (13.5 * 0.5)) ≈ 9.48 tokens/s。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 min(64/(13.5*0.5), 2304/(13.5*0.5)) 正确得出 9.48，且符合混合架构中瓶颈由较小带宽决定的逻辑。
