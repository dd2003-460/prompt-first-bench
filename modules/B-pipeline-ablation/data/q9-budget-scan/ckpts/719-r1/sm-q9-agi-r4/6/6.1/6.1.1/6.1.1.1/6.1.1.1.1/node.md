# N685: NVFP4 在 V100 (Compute Cap 7.0) 上的实际执行路径：V100 不支持 FP4 指令集，CUDA 内核会将 FP4 权重在线反量化为 

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N249

## Claim

NVFP4 在 V100 (Compute Cap 7.0) 上的实际执行路径：V100 不支持 FP4 指令集，CUDA 内核会将 FP4 权重在线反量化为 FP16 进行矩阵乘法，反量化操作本身引入额外计算开销（约 10-20% 的额外 FLOPs），且反量化后的 FP16 权重需驻留显存，因此显存占用并非简单的 2x，而是取决于反量化是逐块（block-wise）还是全量（full-batch）执行；若逐块执行，峰值显存可能略高于 FP4 存储大小但远低于 2x，需实测 vLLM 在 V100 上加载 NVFP4 模型时的显存占用曲线

## Corrected Claim

NVFP4 在 V100 (Compute Cap 7.0) 上不支持原生 FP4 指令，CUDA 内核需将 FP4 权重在线反量化为 FP16 进行矩阵乘法。反量化操作会引入额外计算开销，且显存占用取决于反量化粒度（逐块或全量）；具体开销比例及峰值显存需实测确定，通常逐块执行可显著降低峰值显存。

## Evidence

[质询]该陈述包含具体的性能开销数值（10-20% FLOPs）和特定的软件行为假设（vLLM在V100上的具体实现细节），属于经验事实。由于缺乏外部来源支持，且不同反量化策略（如使用LUT vs 算术运算）及硬件微架构差异可能导致开销显著偏离此范围，无法确证该具体数值区间。 | 经验事实，逻辑自洽但缺来源支持。V100 (CC 7.0) 确实不支持原生FP4指令，必须反量化至FP16/BF16计算，这一核心机制符合硬件架构常识；但具体的10-20%开销及vLLM的具体显存行为属于未经证实的经验数据。

## Search Query

vLLM NVFP4 quantization V100 compute capability 7.0 dequantization memory footprint block-wise
