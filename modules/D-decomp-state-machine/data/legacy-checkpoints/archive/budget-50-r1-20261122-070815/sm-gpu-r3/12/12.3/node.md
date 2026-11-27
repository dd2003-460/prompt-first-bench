# N435: RTX 4090 运行 INT4 模型时的 Prefill 性能受限于 GEMM 反量化内核效率，其有效 FLOPS 利用率通常仅为理论峰值的 60-70%，而

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N150, N151, N152

## Claim

RTX 4090 运行 INT4 模型时的 Prefill 性能受限于 GEMM 反量化内核效率，其有效 FLOPS 利用率通常仅为理论峰值的 60-70%，而 L40S 原生 FP8 支持使有效利用率可达 80-85%，导致实际吞吐差距大于算力纸面差距。

## Corrected Claim

RTX 4090 运行 INT4 模型时的 Prefill 性能受限于 GEMM 反量化内核效率，其有效 FLOPS 利用率通常低于 L40S 原生 FP8 支持下的利用率，导致实际吞吐差距大于算力纸面差距。

## Evidence

[质询]具体数值区间（60-70% vs 80-85%）缺乏通用基准测试支持，实际利用率高度依赖模型结构、序列长度及具体推理框架（如 vLLM/TensorRT-LLM）的实现细节，不同场景下波动极大，断言固定区间存在过度概括风险。 | 先验知识/题面给定，逻辑校验通过：RTX 4090 无原生 FP8 支持需反量化 INT4 至 FP16 进行 GEMM，确实存在额外开销；L40S 支持 FP8 可减少数据搬运和计算精度转换开销，理论上利用率更高。但具体百分比为经验估计，非绝对物理定律，故降级。

## Search Query

INT4 dequantization overhead GPU prefill performance efficiency L40S FP8 native
