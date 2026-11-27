# N381: RTX 5090 (Blackwell) 的 BF16 Tensor Core 峰值算力约为 105 TFLOPS，H100 SXM 的 BF16 Tensor

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N134

## Claim

RTX 5090 (Blackwell) 的 BF16 Tensor Core 峰值算力约为 105 TFLOPS，H100 SXM 的 BF16 Tensor Core 峰值算力为 990 TFLOPS，两者算力比值为 1:9.4 [待核验]。

## Corrected Claim

RTX 5090 (Blackwell) 的 BF16 Tensor Core 峰值算力约为 105 TFLOPS（待确认具体口径），H100 SXM 的 BF16 Tensor Core 峰值算力为 990 TFLOPS，两者算力比值约为 1:9.4。

## Evidence

[质询]RTX 5090 的 BF16 Tensor Core 峰值算力数值（105 TFLOPS）存在显著不确定性。根据 NVIDIA 官方规格，RTX 5090 的 FP16/BF16 Tensor Core 算力通常标称为 104.8 TFLOPS（基于 21760 CUDA 核心 * 2 FLOPs/cycle * 2.4 GHz 基础频率或类似计算），但不同来源可能因是否计入稀疏加速（Sparsity）或频率差异而给出不同数值（如 209 TFLOPS 含稀疏）。若 105 TFLOPS 是准确的基础算力，则比值 990/105 ≈ 9.4 成立；但若该数值本身有误（例如混淆了 FP32 或 FP16 非稀疏/稀疏口径），则结论错误。鉴于无外部来源支持，且具体硬件参数属于经验事实，无法仅凭逻辑推导确认 105 TFLOPS 这一具体数值的准确性。 | 经验事实，逻辑自洽但缺来源支持。H100 SXM 的 990 TFLOPS BF16 算力是公认标准值，RTX 5090 的 105 TFLOPS 量级合理（约为 H100 的 1/10），但具体数值需来源确认，故降级。

## Search Query

RTX 5090 vs H100 SXM BF16 Tensor Core TFLOPS specs
