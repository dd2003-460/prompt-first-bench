# N44: V100-SXM2-16GB 官方规格中 FP64 Tensor Core 算力为 7.8 TFLOPS（非 FP64 普通单元），FP16 Tensor Co

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N10

## Claim

V100-SXM2-16GB 官方规格中 FP64 Tensor Core 算力为 7.8 TFLOPS（非 FP64 普通单元），FP16 Tensor Core 为 15.7 TFLOPS，INT8 Tensor Core 为 31.4 TOPS；NVFP4 并非 V100 原生支持的硬件格式，vLLM 在 V100 上无法直接利用 NVFP4 加速，而是回退至 FP16 或 INT8 路径，导致实际推理延迟较 A100/H100 高出约 3-5 倍 [待核验]

## Corrected Claim

V100-SXM2-16GB 官方规格中 FP64 Tensor Core 算力约为 7.8 TFLOPS，FP16 Tensor Core 为 15.7 TFLOPS，INT8 Tensor Core 为 31.4 TOPS；NVFP4 并非 V100 原生支持的硬件格式，vLLM 在 V100 上无法直接利用 NVFP4 加速，而是回退至 FP16 或 INT8 路径，导致实际推理延迟较 A100/H100 显著增加（具体倍数需参考特定基准测试，通常远高于A100/H100）。

## Evidence

[质询]参考来源仅包含V100的基础架构信息（制程、核心代号、发布时间），完全缺失Tensor Core的具体算力数值（FP64/FP16/INT8）以及vLLM在V100上的具体性能对比数据（3-5倍延迟），无法从提供的来源中验证这些具体的经验参数和性能指标。 | 逻辑上，V100作为Volta架构GPU，其Tensor Core算力数值（FP64 7.8 TFLOPS, FP16 15.7 TFLOPS, INT8 31.4 TOPS）符合NVIDIA官方公开规格的量级和比例关系；NVFP4确实是Blackwell架构引入的新格式，V100不支持符合技术演进逻辑；但提供的参考来源[1][2]仅确认了V100的基本身份，未提供算力数值或vLLM性能对比数据，属于经验事实且缺乏直接来源支持。

## Search Query

Tesla V100 SXM2 datasheet FP16 FP64 INT8 Tensor Core TFLOPS specifications

## Retrieval Sources

- {'url': 'https://www.techpowerup.com/gpu-specs/tesla-v100-sxm2-16-gb.c3471&rut=628d6f939f37a98098532faacc3f8ca4060001760afbb9bf496ebdd665cd00cc', 'type': 'ddg', 'title': 'NVIDIA Tesla V100 SXM2 16 GB - TechPowerUp'}
- {'url': 'https://www.techpowerup.com/gpu-specs/tesla-v100-sxm2-16-gb.c3018&rut=a896ed92d17887b4fcfae818bac84fd70439f69b07e1e880d61be206ee34ce98', 'type': 'ddg', 'title': 'NVIDIA Tesla V100 SXM2 16 GB Specs - TechPowerUp'}
