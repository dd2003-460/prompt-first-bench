# N190: 填补 14.4GB 显存缺口的技术路径及其量化代价：1) KV Cache 量化 (FP8/INT8) 可节省 ~50% KV 显存 (约 3.2GB)，剩余缺

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N37

## Claim

填补 14.4GB 显存缺口的技术路径及其量化代价：1) KV Cache 量化 (FP8/INT8) 可节省 ~50% KV 显存 (约 3.2GB)，剩余缺口 11.2GB 需依赖 Offload；2) CPU Offload 11.2GB 权重导致的 Decode 吞吐量衰减系数 ≈ (GPU_BW / (GPU_BW * (48/62.4) + CPU_Mem_BW * (14.4/62.4)))，其中 RTX 4090 GPU_BW ≈ 1008 GB/s, DDR5 CPU_Mem_BW ≈ 80-100 GB/s，预计吞吐量降至单卡 4090 的 30-40%。

## Corrected Claim

填补 14.4GB 显存缺口的技术路径：1) KV Cache 量化 (FP8/INT8) 可节省约 50% KV 显存 (约 3.2GB)；2) 剩余 11.2GB 需依赖 CPU Offload。由于 PCIe 带宽瓶颈及数据搬运开销，Decode 吞吐量预计将显著下降，通常降至单卡 4090 的 30-50% 区间（具体取决于 Offload 策略与流水线优化）。

## Evidence

[质询]吞吐量衰减系数的计算公式存在逻辑缺陷：该公式将GPU带宽与CPU带宽按权重加权求和作为分母，隐含假设数据加载是并行且无重叠的，但实际Offload场景中，权重加载（CPU->GPU）与计算（GPU）通常存在流水线重叠或串行瓶颈，且未考虑PCIe带宽瓶颈（通常远低于DDR5内存带宽，约32-64GB/s），导致估算的30-40%吞吐量可能过于乐观或公式本身物理意义不明确。 | 先验知识/题面给定，逻辑校验通过。KV Cache量化节省50%显存符合FP8/INT8相对FP16/BF16的理论预期；RTX 4090带宽1008GB/s和DDR5带宽80-100GB/s量级正确。但吞吐量估算公式未考虑PCIe瓶颈及流水线重叠，属于简化模型，故降级为定性表述。
