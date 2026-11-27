# N128: AMD RX 7900 XTX 在 ROCm 6.x 最新驱动下对 INT4/W4A16 量化的硬件加速支持状态：是否启用了 RDNA3 的专用 INT4 指令

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N35, N36, N37

## Claim

AMD RX 7900 XTX 在 ROCm 6.x 最新驱动下对 INT4/W4A16 量化的硬件加速支持状态：是否启用了 RDNA3 的专用 INT4 指令集，还是仍依赖 FP32/FP16 软件模拟，这将决定其实际吞吐量是否真的比同带宽 NVIDIA 卡低 15-25% 或差距缩小至 <5%。

## Corrected Claim

AMD RX 7900 XTX 在 ROCm 6.x 下对 INT4/W4A16 量化的硬件加速支持状态及与同带宽 NVIDIA 卡的具体性能差距（15-25% 或 <5%）需依赖最新实测数据验证，当前缺乏直接证据确认其是否已完全启用 RDNA3 专用 INT4 指令集以消除软件模拟开销。

## Evidence

[质询]该陈述包含具体的性能差距数值（15-25% vs <5%）和特定的软件/硬件支持状态（ROCm 6.x 下是否启用专用 INT4 指令），属于高度依赖具体版本和实测数据的经验事实，且缺乏公开权威基准测试直接证实该特定量化格式在 RDNA3 上的确切加速机制及性能对比。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源，无法验证具体驱动版本下的指令集启用状态及精确性能差距）

## Search Query

ROCm 6.0 RX 7900 XTX INT4 quantization hardware acceleration RDNA3
