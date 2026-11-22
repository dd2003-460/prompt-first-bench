# N738: Qwen3-27B 共有 60 层 Transformer 结构，每层包含一次 Attention AllReduce 和一次 FFN AllReduce（若 

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N227

## Claim

Qwen3-27B 共有 60 层 Transformer 结构，每层包含一次 Attention AllReduce 和一次 FFN AllReduce（若 FFN 也切分），或仅 Attention 切分时每层 1 次 AllReduce。需确认 Qwen3 架构中 TP 切分策略：通常 Attention 和 FFN 均切分，故每层通信次数为 2 次 AllReduce（或 1 次 AllGather + 1 次 ReduceScatter）。

## Corrected Claim

Qwen3-27B 采用标准 Transformer 架构，在张量并行（TP）切分策略下，若 Attention 和 FFN 均被切分，每层通常涉及 2 次 AllReduce（或等效的 AllGather + ReduceScatter）通信操作；具体层数需参考官方技术报告确认。

## Evidence

[质询]Qwen3-27B 的具体层数（60层）及内部通信细节属于特定模型架构的经验事实，无法从第一性原理推导，且当前无可用来源验证其具体数值（如是否为60层）及确切的切分策略。 | 经验事实，逻辑自洽（TP切分下Attention和FFN各需一次通信符合标准Transformer并行原理），但缺来源支持具体层数及架构细节。

## Search Query

Qwen3-27B tensor parallelism communication pattern allreduce per layer
