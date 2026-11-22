# N131: 单卡 vs 多卡对比方案3（4x RTX 4060 Ti vs 1x MI300X）：4x RTX 4060 Ti 16GB总显存64GB，总价约为$1,600

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N25, N26, N27

## Claim

单卡 vs 多卡对比方案3（4x RTX 4060 Ti vs 1x MI300X）：4x RTX 4060 Ti 16GB总显存64GB，总价约为$1,600-$2,000 (4*$400-$500)。MI300X 192GB价格约为$15,000-$20,000。4x4060 Ti显存带宽总合约为 4*288 = 1152 GB/s，但PCIe互联极慢，多卡推理效率极低（<50%线性扩展），实际吞吐量可能低于单张高带宽卡。MI300X单卡5.3 TB/s带宽，性能远超4x4060 Ti。

## Corrected Claim

单卡 vs 多卡对比方案3（4x RTX 4060 Ti vs 1x MI300X）：4x RTX 4060 Ti 16GB总显存64GB，总价约为$1,600-$2,000 (4*$400-$500)。MI300X 192GB价格约为$15,000-$20,000。4x4060 Ti显存带宽总合约为 4*288 = 1152 GB/s，但PCIe互联极慢，多卡推理效率极低（<50%线性扩展），实际吞吐量可能低于单张高带宽卡。MI300X单卡5.3 TB/s带宽，性能远超4x4060 Ti。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4060 Ti 16GB 显存带宽确为 288 GB/s，4卡总带宽 1152 GB/s 计算正确；MI300X 显存带宽 5.3 TB/s 符合其 HBM3 规格；价格区间（4060 Ti 约 $450，MI300X 约 $15k-$20k）符合市场常识；多卡 PCIe 互联瓶颈导致推理效率低下的逻辑符合硬件架构原理。

## Search Query

4x RTX 4060 Ti LLM inference performance vs MI300X single card memory bandwidth
