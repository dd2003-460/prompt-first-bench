# N313: 工作点 1（高性低成/基准线）：输入 32768 tokens，输出 1024 tokens，Batch Size=1，Temperature=0，使用 vLL

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N87

## Claim

工作点 1（高性低成/基准线）：输入 32768 tokens，输出 1024 tokens，Batch Size=1，Temperature=0，使用 vLLM 框架，记录 TTFT 和平均 tokens/s，作为所有后续对比的基准吞吐量 T_base。

## Corrected Claim

工作点 1（高性低成/基准线）：输入 32768 tokens，输出 1024 tokens，Batch Size=1，Temperature=0，使用 vLLM 框架，记录 TTFT 和平均 tokens/s，作为所有后续对比的基准吞吐量 T_base。

## Evidence

先验知识/题面给定，逻辑校验通过
