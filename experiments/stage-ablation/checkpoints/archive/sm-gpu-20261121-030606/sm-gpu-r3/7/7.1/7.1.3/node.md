# N349: 单卡 RTX 5090 在 32K 上下文、FP8 精度下的实际推理吞吐量受计算与内存带宽双重限制：算力限制 = 838 TFLOPS / (2 * 27e9 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N149

## Claim

单卡 RTX 5090 在 32K 上下文、FP8 精度下的实际推理吞吐量受计算与内存带宽双重限制：算力限制 = 838 TFLOPS / (2 * 27e9 * 32768 / 3600) ≈ 176 tokens/s，带宽限制 = 1792 GB/s / (27GB + 5.2GB) ≈ 55.6 tokens/s，故理论上限为 55.6 tokens/s，实际值需乘以效率因子 (0.8-0.9)。

## Corrected Claim

单卡 RTX 5090 在 32K 上下文、FP8 精度下的实际推理吞吐量受计算与内存带宽双重限制：算力限制 = 838 TFLOPS / (2 * 27e9 * 32768 / 3600) ≈ 176 tokens/s，带宽限制 = 1792 GB/s / (27GB + 5.2GB) ≈ 55.6 tokens/s，故理论上限为 55.6 tokens/s，实际值需乘以效率因子 (0.8-0.9)。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 5090 规格（~1792 GB/s 带宽，~838 TFLOPS FP8 算力）与 27B 模型在 32K 上下文下的显存占用（~32GB）符合工程常识；计算瓶颈与带宽瓶颈的推导逻辑自洽，且带宽限制（55.6 tokens/s）确实低于算力限制（176 tokens/s），故取最小值作为理论上限符合物理直觉。
