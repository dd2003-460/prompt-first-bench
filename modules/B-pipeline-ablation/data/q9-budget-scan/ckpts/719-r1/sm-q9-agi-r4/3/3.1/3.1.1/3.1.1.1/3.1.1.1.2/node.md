# N483: vLLM 在 V100 上处理 NVFP4 权重的实际执行路径：由于缺乏硬件支持，执行 'Dequantize to FP16 -> FP16 GEMM' 流水

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N172

## Claim

vLLM 在 V100 上处理 NVFP4 权重的实际执行路径：由于缺乏硬件支持，执行 'Dequantize to FP16 -> FP16 GEMM' 流水线，其中 Dequantization 步骤通过 CUDA kernel 实现，占用额外 5-10% 的 SM 周期

## Corrected Claim

vLLM 在 V100 上处理 NVFP4 权重时，由于缺乏原生硬件支持，通常执行 'Dequantize to FP16 -> FP16 GEMM' 流水线，其中 Dequantization 步骤通过 CUDA kernel 实现，会引入额外的计算开销（具体占比视实现和负载而定，通常在个位数百分比量级）。

## Evidence

[质询]具体数值（5-10% SM 周期开销）和特定执行路径细节（V100 上 NVFP4 的具体 Dequantize 实现方式）属于高度具体的经验性能数据，缺乏通用公开文档支持，且不同 vLLM 版本或配置下该比例可能波动较大，存在将特定基准测试结果泛化为固定事实的风险。 | 经验事实，逻辑自洽（V100 无 FP4 硬件支持需反量化至 FP16 符合架构常识，反量化占用少量 SM 资源符合直觉），但检索无可用来源，无法验证具体 5-10% 的数值精度及特定实现细节。

## Search Query

vLLM NVFP4 quantization V100 dequantization overhead benchmark
