# N163: 修正 N52 的吞吐量估计：若通信开销高达 92%，则有效吞吐极低，N52 中提到的 14-16 tokens/s 可能过于乐观。若采用 Pipeline Pa

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N52

## Claim

修正 N52 的吞吐量估计：若通信开销高达 92%，则有效吞吐极低，N52 中提到的 14-16 tokens/s 可能过于乐观。若采用 Pipeline Parallelism (PP) 或 Model Parallelism (MP) 减少每步通信量，或仅对部分层做 TP，通信开销可降低至 20-30%。需对比 H100 单卡（无通信开销）在相同精度下的实际吞吐（约 25-30 tokens/s），验证 2x 4090 是否真的低于 H100。

## Corrected Claim

修正 N52 的吞吐量估计：若通信开销高达 92%，则有效吞吐极低，N52 中提到的 14-16 tokens/s 可能过于乐观。若采用 Pipeline Parallelism (PP) 或 Model Parallelism (MP) 减少每步通信量，或仅对部分层做 TP，通信开销有望显著降低。需对比 H100 单卡（无通信开销）在相同精度下的实际吞吐，验证 2x 4090 是否真的低于 H100。

## Evidence

[质询]该陈述包含多个具体的经验性数值（如H100单卡25-30 tokens/s、通信开销降低至20-30%），这些属于硬件性能与系统调优的经验事实，无法从第一性原理严格推导，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

2x RTX 4090 Tensor Parallelism vs H100 single card throughput comparison LLM
