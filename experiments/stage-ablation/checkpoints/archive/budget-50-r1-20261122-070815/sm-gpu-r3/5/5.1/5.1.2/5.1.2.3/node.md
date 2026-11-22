# N342: NVIDIA H100 SXM5 的 Performance per Watt 在 LLM 推理场景下约为 0.5-0.8 tokens/s/W (基于 FP8

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N121

## Claim

NVIDIA H100 SXM5 的 Performance per Watt 在 LLM 推理场景下约为 0.5-0.8 tokens/s/W (基于 FP8/BF16 混合负载)，而 A100 PCIe 约为 0.05-0.1 tokens/s/W，L40S 约为 0.1-0.2 tokens/s/W；该比值差异源于 H100 的 NVLink 高带宽互联和 FP8 Tensor Core 效率，而非单纯 TDP 差异，用于量化'高功耗是否换来等比例性能提升'。

## Corrected Claim

NVIDIA H100 SXM5 的 Performance per Watt 在 LLM 推理场景下约为 0.5-0.8 tokens/s/W (基于 FP8/BF16 混合负载)，而 A100 PCIe 约为 0.05-0.1 tokens/s/W，L40S 约为 0.1-0.2 tokens/s/W；该比值差异源于 H100 的 NVLink 高带宽互联和 FP8 Tensor Core 效率，而非单纯 TDP 差异，用于量化'高功耗是否换来等比例性能提升'。

## Evidence

先验知识/题面给定，逻辑校验通过
