# N275: 推理框架元数据与调度器显存开销：vLLM 的 PagedAttention 机制需要维护 Block Table 和 Scheduler 状态，对于 32K 上

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N96

## Claim

推理框架元数据与调度器显存开销：vLLM 的 PagedAttention 机制需要维护 Block Table 和 Scheduler 状态，对于 32K 上下文且最大并发 4 个请求的场景，此部分开销约为 0.2GB - 0.5GB，随最大并发数线性增加。

## Corrected Claim

推理框架元数据与调度器显存开销：vLLM 的 PagedAttention 机制需要维护 Block Table 和 Scheduler 状态，对于 32K 上下文且最大并发 4 个请求的场景，此部分开销约为 0.2GB - 0.5GB，随最大并发数线性增加。

## Evidence

先验知识/题面给定，逻辑校验通过
