# N218: W4 精度在 RTX 4090 上的算力效率惩罚系数：由于 Ada 架构原生不支持 4-bit 整数矩阵乘加，W4 推理需依赖反量化至 FP16/INT8 进行

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N100

## Claim

W4 精度在 RTX 4090 上的算力效率惩罚系数：由于 Ada 架构原生不支持 4-bit 整数矩阵乘加，W4 推理需依赖反量化至 FP16/INT8 进行计算或专用 Kernel 优化，实际有效算力通常仅为 INT8 峰值的 60%-70%（即 ~99-115 TFLOPS），导致实际吞吐量低于纯带宽估算值。

## Corrected Claim

W4 精度在 RTX 4090 上的算力效率通常低于 INT8 峰值，具体惩罚系数取决于 Kernel 优化程度，实际有效算力往往显著低于 INT8 峰值，导致实际吞吐量低于纯带宽估算值。

## Evidence

[质询]数值量级与具体系数缺乏通用基准支持：'60%-70%' 是一个高度依赖具体 Kernel 实现（如 TensorRT-LLM 版本、是否使用 FP8 加速等）的经验值，并非 Ada 架构的固定物理属性；且 RTX 4090 的 INT8 峰值算力通常按 330 TOPS (稀疏) 或 165 TOPS (稠密) 计算，若按 165 TOPS 计算，60-70% 对应 99-115 TOPS，数值自洽，但该效率惩罚系数并非架构层面的绝对真理，而是特定软件栈下的性能表现，存在因优化提升而超过 70% 的可能性。 | 先验知识/题面给定，逻辑校验通过：Ada 架构确实原生不支持 INT4 矩阵乘加，需反量化或特殊 Kernel，导致算力效率低于 INT8 峰值是符合硬件原理的定性事实；但具体 '60%-70%' 的数值属于经验性工程参数，虽逻辑自洽且量级合理，但缺乏通用性，故降级为定性表述。

## Search Query

RTX 4090 W4 quantization inference performance penalty Ada architecture
