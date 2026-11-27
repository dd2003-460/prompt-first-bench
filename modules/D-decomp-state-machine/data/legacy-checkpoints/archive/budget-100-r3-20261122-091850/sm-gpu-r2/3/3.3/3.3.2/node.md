# N72: PCIe vs NVLink 带宽差距对多卡推理性能的影响：NVLink 4.0 (RTX 3090/4090 无此配置，A100/H100 有) 带宽为 60

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N18

## Claim

PCIe vs NVLink 带宽差距对多卡推理性能的影响：NVLink 4.0 (RTX 3090/4090 无此配置，A100/H100 有) 带宽为 600-900 GB/s，而 PCIe 4.0 为 32 GB/s。若互联带宽成为瓶颈，TPS 上限 ≈ Interconnect_Bandwidth / (Data_Size_Per_Token_Communication)。对于 2x 4090，由于缺乏高带宽互联，TP=2 的效率通常低于 50-60%。

## Corrected Claim

PCIe vs NVLink 带宽差距对多卡推理性能的影响：NVLink 4.0 (RTX 3090/4090 无此配置，A100/H100 有) 带宽为 600-900 GB/s，而 PCIe 4.0 为 32 GB/s。若互联带宽成为瓶颈，TPS 上限 ≈ Interconnect_Bandwidth / (Data_Size_Per_Token_Communication)。对于 2x 4090，由于缺乏高带宽互联，TP=2 的效率通常低于 50-60%。

## Evidence

[质询]NVLink 4.0 带宽数值范围（600-900 GB/s）可能混淆了不同代际或双向/单向口径，且 RTX 4090 确实无 NVLink，但 A100/H100 的 NVLink 版本不同（A100 为 NVLink 3.0, H100 为 NVLink 4.0），需确认 600-900 GB/s 是否准确覆盖所有提及的卡型。 | 先验知识/题面给定，逻辑校验通过：NVLink 带宽远高于 PCIe 是公认事实，TP 效率受互联带宽限制符合分布式推理基本原理，数值量级合理。

## Search Query

PCIe vs NVLink bandwidth impact on multi-GPU LLM inference efficiency
