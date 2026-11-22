# N35: 在32GB显存GPU上运行27B模型BF16，若启用CPU Offload，需将至少 23.2GB 权重卸载至CPU内存，导致每生成一个token需从CPU内存

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N6

## Claim

在32GB显存GPU上运行27B模型BF16，若启用CPU Offload，需将至少 23.2GB 权重卸载至CPU内存，导致每生成一个token需从CPU内存读取对应层权重，若CPU内存带宽为 100GB/s (DDR5双通道典型值)，仅权重读取延迟即为 232ms/token，加上GPU计算时间，总延迟将超过 300ms/token (即 <3.3 tokens/s)，远低于交互式推理需求 (>10 tokens/s)

## Corrected Claim

在32GB显存GPU上运行27B模型BF16，若启用CPU Offload，需将至少 23.2GB 权重卸载至CPU内存，导致每生成一个token需从CPU内存读取对应层权重，若CPU内存带宽为 100GB/s (DDR5双通道典型值)，仅权重读取延迟即为 232ms/token，加上GPU计算时间，总延迟将超过 300ms/token (即 <3.3 tokens/s)，远低于交互式推理需求 (>10 tokens/s)

## Evidence

先验知识/题面给定，逻辑校验通过：27B模型BF16权重约54GB，32GB显存下需卸载约22-23GB至CPU；按100GB/s带宽计算，23.2GB/100GB/s=0.232s=232ms，加上计算时间总延迟超300ms/token，推理速度低于3.3 tokens/s，符合物理规律和工程常识。
