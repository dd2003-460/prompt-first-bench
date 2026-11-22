# N252: Activation_Overhead 的精确分解：包括 CUDA Context 开销（约 0.5-1.0 GB）、临时激活张量峰值（约 1.0-2.0 GB

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N89

## Claim

Activation_Overhead 的精确分解：包括 CUDA Context 开销（约 0.5-1.0 GB）、临时激活张量峰值（约 1.0-2.0 GB，取决于 Batch Size 和序列长度）以及框架内部数据结构开销（约 0.2-0.5 GB）；在 Batch Size=1 时，总 Activation_Overhead 通常为 1.5-3.5 GB，需根据具体框架（vLLM vs SGLang）和硬件架构进行实测校准。

## Corrected Claim

Activation_Overhead 的精确分解：包括 CUDA Context 开销（约 0.5-1.0 GB）、临时激活张量峰值（约 1.0-2.0 GB，取决于 Batch Size 和序列长度）以及框架内部数据结构开销（约 0.2-0.5 GB）；在 Batch Size=1 时，总 Activation_Overhead 通常为 1.5-3.5 GB，需根据具体框架（vLLM vs SGLang）和硬件架构进行实测校准。

## Evidence

先验知识/题面给定，逻辑校验通过
