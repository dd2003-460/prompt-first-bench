# N188: Mac Studio M2 Ultra 运行 INT4 量化模型时的软件栈限制：llama.cpp 和 MLX 框架对 INT4 权重的反量化（Dequanti

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N62

## Claim

Mac Studio M2 Ultra 运行 INT4 量化模型时的软件栈限制：llama.cpp 和 MLX 框架对 INT4 权重的反量化（Dequantization）发生在 CPU 或 GPU 核心，而非专用硬件单元，导致 INT4 的实际 Decode 吞吐受限于 ALU 指令吞吐而非内存带宽。实测显示，INT4 在 Mac Studio 上的吞吐提升幅度（相对于 BF16）通常仅为 1.2-1.5 倍，而非理论带宽比 4 倍，即理论 59.26 tokens/s 可能实际仅达 20-30 tokens/s [待核验]。

## Corrected Claim

Mac Studio M2 Ultra 运行 INT4 量化模型时，由于 llama.cpp 和 MLX 框架中 INT4 权重的反量化发生在 CPU 或 GPU 核心而非专用硬件单元，实际 Decode 吞吐受限于 ALU 指令吞吐而非内存带宽。因此，INT4 相对于 BF16 的实际吞吐提升幅度通常低于理论带宽比（4倍），具体提升倍数取决于模型规模与硬件负载，通常显著低于理论值。

## Evidence

[质询]该陈述包含具体的实测性能数据（1.2-1.5倍提升、20-30 tokens/s），属于经验事实。由于检索失败无外部来源支持，且不同模型大小、序列长度及具体硬件配置下，INT4相对于BF16的加速比波动较大，无法仅凭逻辑推导确认该特定数值区间为普遍真理。 | 经验事实，逻辑自洽（INT4反量化确实消耗ALU资源，导致加速比低于理论带宽比），但缺来源支持具体数值。

## Search Query

Mac Studio M2 Ultra INT4 dequantization performance bottleneck llama.cpp MLX
