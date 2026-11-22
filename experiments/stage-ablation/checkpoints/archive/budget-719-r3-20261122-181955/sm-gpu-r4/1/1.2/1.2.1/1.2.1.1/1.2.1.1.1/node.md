# N440: A100 80GB PCIe 的 BF16 稠密算力为 312 TFLOPS（非 N149 中误用的 156 TFLOPS），基于 NVIDIA 官方 data

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N149

## Claim

A100 80GB PCIe 的 BF16 稠密算力为 312 TFLOPS（非 N149 中误用的 156 TFLOPS），基于 NVIDIA 官方 datasheet 及 HuggingFace 硬件规格表。

## Corrected Claim

A100 80GB PCIe 的 BF16 稠密算力需依据具体 NVIDIA 官方 datasheet 版本确认，通常标称值在 19.5 TFLOPS (FP32/BF16 基础) 至 312 TFLOPS (Tensor Core 峰值，可能含稀疏或 SXM 混淆) 之间，建议核实具体测试条件与精度模式。

## Evidence

[质询]数值量级与官方规格存在显著偏差：NVIDIA A100 80GB PCIe 的官方 BF16 稠密算力通常为 19.5 TFLOPS（或 Tensor Core 加速下的 312 TFLOPS，但需明确是否含稀疏加速或特定精度模式），若陈述指代的是标准稠密 BF16 算力，312 TFLOPS 这一数值更接近 A100 SXM 版本的 Tensor Core 峰值或混淆了稀疏/稠密口径；此外，'非 N149 中误用的 156 TFLOPS' 这一对比缺乏上下文，156 TFLOPS 并非 A100 的标准标称值，可能是对 FP16 或其他配置的误读。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且数值与常见公开规格存在口径歧义，无法确证 312 TFLOPS 为 PCIe 版 BF16 稠密算力的准确值）

## Search Query

NVIDIA A100 80GB PCIe datasheet BF16 dense TFLOPS
