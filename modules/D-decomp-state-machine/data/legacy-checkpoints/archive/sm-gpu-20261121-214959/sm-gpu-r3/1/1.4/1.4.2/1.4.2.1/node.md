# N155: RTX 5090 (Blackwell) 原生支持 FP8 和 NVFP4，其理论 FP8 计算峰值约为 512 TFLOPS (FP8) 或 1024 TFL

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N48

## Claim

RTX 5090 (Blackwell) 原生支持 FP8 和 NVFP4，其理论 FP8 计算峰值约为 512 TFLOPS (FP8) 或 1024 TFLOPS (NVFP4)。对比 H100 SXM 的 989 TFLOPS (FP8)，RTX 5090 的 FP8 计算峰值仅为 H100 的 ~52% (512/989)，而非 N48 声称的 60-80%。N48 的 60-80% 估计可能混淆了带宽比 (1792/2039=87.9%) 与计算能力比。

## Corrected Claim

RTX 5090 (Blackwell) 原生支持 FP8 和 NVFP4，其理论 FP8 计算峰值约为 512 TFLOPS (FP8) 或 1024 TFLOPS (NVFP4)。对比 H100 SXM 的 989 TFLOPS (FP8)，RTX 5090 的 FP8 计算峰值仅为 H100 的 ~52% (512/989)，而非 N48 声称的 60-80%。N48 的 60-80% 估计可能混淆了带宽比 (1792/2039=87.9%) 与计算能力比。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 5090 FP8峰值约512 TFLOPS，H100 SXM FP8峰值约989 TFLOPS，比值约51.8%，与陈述一致；带宽比混淆的攻击点已被陈述自身澄清。

## Search Query

RTX 5090 Blackwell FP8 TFLOPS vs H100 SXM FP8 TFLOPS
