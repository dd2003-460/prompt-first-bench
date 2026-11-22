# N222: H100 SXM 上 FP8 vs BF16 的 T_prefill 理论加速比计算：H100 FP8 Tensor Core 峰值算力 989 TFLOPS 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N82

## Claim

H100 SXM 上 FP8 vs BF16 的 T_prefill 理论加速比计算：H100 FP8 Tensor Core 峰值算力 989 TFLOPS (vs BF16 989/2 ≈ 494.5 TFLOPS，注意 H100 标称 BF16 为 989 TFLOPS 含稀疏，密集为 494.5)。修正：H100 SXM BF16 密集算力 989 TFLOPS 是错误记忆，实际 BF16 密集为 989 TFLOPS (含 sparsity) 或 494.5 (dense)。查证：H100 SXM BF16 Tensor Core 989 TFLOPS (with sparsity), 494.5 (dense). FP8 为 1979 TFLOPS (sparsity), 989.5 (dense). 因此 FP8 密集算力是 BF16 密集算力的 2 倍。理论 T_prefill 加速比 = 2.0x (假设 MFU 恒定)。

## Corrected Claim

H100 SXM 上 FP8 密集算力为 1,979 TFLOPS，BF16 密集算力为 989 TFLOPS。因此 FP8 密集算力是 BF16 密集算力的 2 倍。理论 T_prefill 加速比 = 2.0x (假设 MFU 恒定)。

## Evidence

[质询]数值量级错误：H100 SXM 的 FP8 和 BF16 峰值算力数值与官方规格及参考来源严重不符。来源显示 H100 SXM FP8 稀疏算力为 3,958 TFLOPS，BF16 稀疏算力为 1,979 TFLOPS，而陈述中使用的 989/1979 TFLOPS 仅为 PCIe 版本或错误记忆，导致基础数据错误。 | 参考来源 [1] 和 [2] 明确指出 H100 SXM 的 FP8 Tensor Core 算力为 3,958 TFLOPS (sparse) 和 1,979 TFLOPS (dense)，BF16 为 1,979 TFLOPS (sparse) 和 989 TFLOPS (dense)。陈述中声称 BF16 密集为 494.5 TFLOPS 或 989 TFLOPS 含稀疏，FP8 为 989.5 (dense)，这与 SXM 版本的实际规格（FP8 dense 1979, BF16 dense 989）矛盾，且混淆了 SXM 与 PCIe 版本的性能指标（PCIe 版本 FP8 sparse 为 1979, dense 989.5）。

## Search Query

NVIDIA H100 SXM dense FP8 vs BF16 TFLOPS specification

## Retrieval Sources

- {'url': 'https://gpusmith.com/hardware/gpus/nvidia-h100-sxm&rut=55f709c954c2dc2a5ec2014bee413884cdfa4a5d73d5f2d73b22f9fc76087cfd', 'type': 'ddg', 'title': 'NVIDIA H100 SXM Specs & Procurement | GPU Smith'}
- {'url': 'https://www.spheron.network/blog/nvidia-h100-specs/&rut=e5afe5d28135b0864354f6a919c9b5413af325349242231957e28963cf88f536', 'type': 'ddg', 'title': 'NVIDIA H100 Specs: FP32 TFLOPS, 80GB HBM3, Memory Bandwidth | Spheron'}
- {'url': 'https://inferencex.semianalysis.com/chips/h100&rut=6288999ef3b04c4335f2b673fee144f9b1eb96492fdfd67f32bbcbb9abd5b818', 'type': 'ddg', 'title': 'NVIDIA H100 SXM Specs: ~$1.17/hr, 80 GB HBM3 | InferenceX'}
