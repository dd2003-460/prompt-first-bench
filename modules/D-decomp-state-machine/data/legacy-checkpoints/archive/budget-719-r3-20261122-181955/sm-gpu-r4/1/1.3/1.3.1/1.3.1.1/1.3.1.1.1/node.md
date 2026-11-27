# N504: ROCm 6.0+ 对 BF16 的硬件加速状态：AMD RDNA3 架构 (RX 7900 XTX) 原生支持 BF16 指令集 (FMMA_BF16)，RO

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N175

## Claim

ROCm 6.0+ 对 BF16 的硬件加速状态：AMD RDNA3 架构 (RX 7900 XTX) 原生支持 BF16 指令集 (FMMA_BF16)，ROCm 6.0 及以上版本中 PyTorch 的 `torch.bfloat16` 操作已启用硬件加速，不再依赖 FP32 模拟，性能损耗 <5%。

## Corrected Claim

ROCm 6.0+ 对 BF16 的硬件加速状态：AMD RDNA3 架构 (RX 7900 XTX) 原生支持 BF16 指令集，ROCm 6.0 及以上版本中 PyTorch 的 `torch.bfloat16` 操作已启用硬件加速，不再依赖 FP32 模拟，性能接近 FP16 水平（具体损耗因算子而异）。

## Evidence

[质询]数值量级与具体性能指标缺乏来源支持：'性能损耗 <5%' 是一个具体的经验性性能指标，不同算子（如 GEMM vs. Element-wise）和不同硬件配置下差异巨大，无法从第一性原理推导，且 RDNA3 的 BF16 支持在早期 ROCm 版本中可能存在兼容性或性能波动，该具体数值缺乏权威基准测试直接佐证。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法验证具体性能损耗数值及特定版本加速状态）

## Search Query

ROCm 6.0 RDNA3 BF16 hardware acceleration PyTorch
