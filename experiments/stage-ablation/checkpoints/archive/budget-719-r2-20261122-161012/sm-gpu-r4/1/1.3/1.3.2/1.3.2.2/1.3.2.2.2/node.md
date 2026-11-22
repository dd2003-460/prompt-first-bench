# N372: WRX90 平台相对消费级平台在 2x 4090 推理场景下的性能增益量化：由于 N154 已证明 PCIe 带宽非瓶颈，WRX90 的额外成本仅带来 CPU 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N155

## Claim

WRX90 平台相对消费级平台在 2x 4090 推理场景下的性能增益量化：由于 N154 已证明 PCIe 带宽非瓶颈，WRX90 的额外成本仅带来 CPU 侧 Offload 能力（8 通道内存带宽 ~300GB/s vs 消费级 ~100GB/s）；若不使用 CPU Offload（即模型完全装入 GPU 显存），WRX90 平台的边际性能增益为 0%，此时 $2,750-$3,550 的额外成本为纯沉没成本，导致 TCO 性价比直接下降。

## Corrected Claim

WRX90 平台相对消费级平台在 2x 4090 推理场景下的性能增益量化：由于 N154 已证明 PCIe 带宽非瓶颈，WRX90 的额外成本仅带来 CPU 侧 Offload 能力（8 通道内存带宽 ~300GB/s vs 消费级 ~100GB/s）；若不使用 CPU Offload（即模型完全装入 GPU 显存），WRX90 平台的边际性能增益为 0%，此时 $2,750-$3,550 的额外成本为纯沉没成本，导致 TCO 性价比直接下降。

## Evidence

先验知识/题面给定，逻辑校验通过：若模型完全装入GPU显存且PCIe非瓶颈，CPU侧带宽差异不影响推理性能，边际增益为0的推导符合逻辑。
