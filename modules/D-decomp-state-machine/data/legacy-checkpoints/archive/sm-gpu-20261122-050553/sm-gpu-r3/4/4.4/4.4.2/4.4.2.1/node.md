# N273: 2×RTX 4090 方案在 FP8 精度下的聚合显存带宽为 2 × 1008 GB/s = 2016 GB/s，但受限于 PCIe 4.0 x16 跨卡通信瓶

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N90

## Claim

2×RTX 4090 方案在 FP8 精度下的聚合显存带宽为 2 × 1008 GB/s = 2016 GB/s，但受限于 PCIe 4.0 x16 跨卡通信瓶颈（~32 GB/s），有效带宽效率因子 η_eff ≈ 0.6-0.7，因此有效聚合带宽 ≈ 1210-1411 GB/s。理论最大解码速度 = 1210 / 27 ≈ 44.8 tokens/s，低于 A100 的 57.6 tokens/s。

## Corrected Claim

2×RTX 4090 方案在 FP8 精度下的聚合显存带宽为 2 × 1008 GB/s = 2016 GB/s，但受限于 PCIe 4.0 x16 跨卡通信瓶颈（~32 GB/s），有效带宽效率因子 η_eff ≈ 0.6-0.7，因此有效聚合带宽 ≈ 1210-1411 GB/s。理论最大解码速度 = 1210 / 27 ≈ 44.8 tokens/s，低于 A100 的 57.6 tokens/s。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090显存带宽1008GB/s、PCIe 4.0 x16带宽~32GB/s均为标准硬件参数，计算过程（2016*0.6~0.7=1210~1411，1210/27≈44.8）数学自洽，且符合双卡推理受限于跨卡通信瓶颈的工程直觉。

## Search Query

dual RTX 4090 PCIe interconnect bandwidth efficiency LLM inference
