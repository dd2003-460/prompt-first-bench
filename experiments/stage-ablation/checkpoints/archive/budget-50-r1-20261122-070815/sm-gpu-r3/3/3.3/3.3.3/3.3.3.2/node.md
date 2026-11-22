# N279: 在 vLLM 或 PyTorch 中，2x RTX 4090 进行 Tensor Parallel 推理时，每层 Transformer 块需执行 2 次 Al

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N85

## Claim

在 vLLM 或 PyTorch 中，2x RTX 4090 进行 Tensor Parallel 推理时，每层 Transformer 块需执行 2 次 All-Reduce（Attention 后和 FFN 后）；对于 64 层模型，单次 Token 生成涉及的总通信数据量约为 2 * 64 * (Hidden_Size * Batch_Size * Dtype_Size)，其中 Hidden_Size=4096, Dtype_Size=2 (BF16)，需量化此通信量与 PCIe 带宽的比值以估算通信延迟占比

## Corrected Claim

在 vLLM 或 PyTorch 中，2x RTX 4090 进行 Tensor Parallel 推理时，每层 Transformer 块需执行 2 次 All-Reduce（Attention 后和 FFN 后）；对于 64 层模型，单次 Token 生成涉及的总通信数据量约为 2 * 64 * (Hidden_Size * Batch_Size * Dtype_Size)，其中 Hidden_Size=4096, Dtype_Size=2 (BF16)，需量化此通信量与 PCIe 带宽的比值以估算通信延迟占比

## Evidence

先验知识/题面给定，逻辑校验通过：Transformer 标准架构中 Attention 和 FFN 后各需一次 All-Reduce，64 层模型共 128 次通信，每次通信数据量为 Hidden_Size * Batch_Size * Dtype_Size，公式推导符合分布式推理基本原理。

## Search Query

tensor parallel all-reduce communication volume per layer transformer hidden size
