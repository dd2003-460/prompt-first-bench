# N364: ROCm 6.x 中针对 RDNA3 的 INT4 量化内核（如 GPTQ/AWQ 后端）的实际吞吐量实测数据：需对比 FP16 基准，计算 INT4 加速比（

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N128

## Claim

ROCm 6.x 中针对 RDNA3 的 INT4 量化内核（如 GPTQ/AWQ 后端）的实际吞吐量实测数据：需对比 FP16 基准，计算 INT4 加速比（Speedup Ratio = Throughput_INT4 / Throughput_FP16）。若加速比 < 1.5x，则视为软件栈未充分利用硬件 INT4 单元。

## Corrected Claim

ROCm 6.x 中针对 RDNA3 的 INT4 量化内核（如 GPTQ/AWQ 后端）的实际吞吐量需通过实测对比 FP16 基准计算加速比；通常认为若加速比显著低于理论峰值（如 < 1.5x），可能表明软件栈未充分利用硬件 INT4 单元，但具体阈值需依据实际基准测试确定。

## Evidence

[质询]该陈述包含具体的经验性阈值（1.5x）和未提供的实测数据，属于硬件/软件性能经验事实，无法从第一性原理推导，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

ROCm 6.0 RX 7900 XTX INT4 quantization LLM inference benchmark speedup
