# N8: 主流推理框架（vLLM/TGI）在处理 32K 上下文时的基础运行时显存开销（CUDA Context, 算子缓冲, 调度器）约为 1.5-2.5GB

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

主流推理框架（vLLM/TGI）在处理 32K 上下文时的基础运行时显存开销（CUDA Context, 算子缓冲, 调度器）约为 1.5-2.5GB

## Corrected Claim

主流推理框架（vLLM/TGI）在处理 32K 上下文时的基础运行时显存开销（CUDA Context, 算子缓冲, 调度器）约为 1.5-2.5GB

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

vLLM base memory overhead 32k context
