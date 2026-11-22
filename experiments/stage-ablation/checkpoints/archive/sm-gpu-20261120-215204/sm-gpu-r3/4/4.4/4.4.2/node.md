# N105: 激活值缓冲（Activation Buffer）显存占用估算：对于Batch Size=1的推理场景，激活值峰值显存通常小于1GB；但在Prefill阶段处理3

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N25

## Claim

激活值缓冲（Activation Buffer）显存占用估算：对于Batch Size=1的推理场景，激活值峰值显存通常小于1GB；但在Prefill阶段处理32K输入时，中间激活张量可能瞬时占用2-4GB，需预留此空间以避免OOM。

## Corrected Claim

激活值缓冲（Activation Buffer）显存占用估算：对于Batch Size=1的推理场景，激活值峰值显存通常小于1GB；但在Prefill阶段处理32K输入时，中间激活张量可能瞬时占用2-4GB，需预留此空间以避免OOM。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LLM inference activation memory footprint prefill 32k batch size 1 GPU OOM margin
