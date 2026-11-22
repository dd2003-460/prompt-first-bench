# N150: A100 80GB在Qwen3-27B INT8量化下的实测吞吐率为48 tokens/s (TensorRT-LLM, 32K ctx, Batch=1)，该

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N44

## Claim

A100 80GB在Qwen3-27B INT8量化下的实测吞吐率为48 tokens/s (TensorRT-LLM, 32K ctx, Batch=1)，该数据来自NVIDIA技术白皮书，低于理论值54.1 tokens/s，差异源于HBM访问延迟和调度开销。

## Corrected Claim

A100 80GB在Qwen3-27B INT8量化下的实测吞吐率约为48 tokens/s (TensorRT-LLM, 32K ctx, Batch=1)，该数据据称来自NVIDIA技术白皮书，低于理论值54.1 tokens/s，差异主要源于HBM访问延迟和调度开销。

## Evidence

[质询]该陈述包含具体的硬件性能实测数据（48 tokens/s）及特定来源（NVIDIA技术白皮书），属于经验事实。由于检索无可用来源，无法验证该具体数值及来源的真实性，且不同量化方案（如SmoothQuant vs 原生INT8）及具体实现细节可能导致吞吐率显著差异，存在数值不准确或来源虚构的风险。 | 经验事实，逻辑自洽（实测低于理论值符合物理直觉）但缺来源支持，无法排除具体数值或来源错误的可能性。

## Search Query

Qwen3-27B A100 TensorRT-LLM benchmark tokens per second 32k
