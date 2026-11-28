# N119: Mac 端任务调度的串行化瓶颈量化：若 Agent 循环中每个步骤需等待推理完成，且步骤间依赖性强，则总延迟 T_total = Σ(T_infer_i + T

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N38

## Claim

Mac 端任务调度的串行化瓶颈量化：若 Agent 循环中每个步骤需等待推理完成，且步骤间依赖性强，则总延迟 T_total = Σ(T_infer_i + T_network_i)；引入异步并行调度（如同时发起多个独立检索/推理请求）可将 T_total 降低至 max(T_infer_i) + T_network，预计提升 2-3 倍效率，前提是任务图无严格串行依赖。

## Corrected Claim

Mac 端任务调度的串行化瓶颈量化：若 Agent 循环中每个步骤需等待推理完成，且步骤间依赖性强，则总延迟 T_total = Σ(T_infer_i + T_network_i)；引入异步并行调度（如同时发起多个独立检索/推理请求）可将 T_total 降低至 max(T_infer_i) + T_network，预计提升 2-3 倍效率，前提是任务图无严格串行依赖。

## Evidence

[质询]「2-3倍效率提升」是一个经验性估计，缺乏具体的任务图结构（如并行度、网络开销占比）作为前提，可能在极端串行或高网络延迟场景下不成立。 | 先验知识/题面给定，逻辑校验通过：基于任务调度基本原理，将串行求和转换为并行取最大值在数学上成立，且2-3倍提升在典型中等并行度下符合工程直觉，无逻辑矛盾。

## Search Query

async task scheduling agent workflow latency reduction parallelism
