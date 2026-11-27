# N219: A100 上运行 FP8 量化模型时，由于缺乏原生 FP8 Tensor Core，需执行 Dequantize->FP16 MatMul->Quantize 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N61

## Claim

A100 上运行 FP8 量化模型时，由于缺乏原生 FP8 Tensor Core，需执行 Dequantize->FP16 MatMul->Quantize 流程，其计算密度效率系数 k_fp8_sim 约为 0.4-0.6 (相对于原生 FP8 硬件加速)，导致有效吞吐量从理论 FP8 峰值下降至 INT8 水平以下，具体需对比 TensorRT 对 FP8 on Ampere 的优化版本 (如 TRT-LLM 0.9+) 的实测数据。

## Corrected Claim

A100 上运行 FP8 量化模型时，由于缺乏原生 FP8 Tensor Core，需执行 Dequantize->FP16 MatMul->Quantize 流程，导致有效吞吐量低于理论 FP8 峰值，具体效率取决于优化实现（如 TensorRT 版本），通常低于原生 FP8 硬件加速性能。

## Evidence

[质询]具体数值系数 0.4-0.6 缺乏公开基准测试支持，且不同优化策略（如 TensorRT 的融合算子）下该系数波动较大，属于经验事实而非固定物理常数。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

TensorRT-LLM FP8 emulation performance penalty Ampere A100
