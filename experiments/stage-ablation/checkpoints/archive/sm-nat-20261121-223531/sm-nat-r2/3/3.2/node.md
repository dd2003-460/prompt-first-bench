# N14: LFU 工作点 1（高性低成）：假设 LFU 完美保留 top-K% 热度对象，K=128GB/E[S]_trunc * 100%，计算 H_LFU_top =

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N3

## Claim

LFU 工作点 1（高性低成）：假设 LFU 完美保留 top-K% 热度对象，K=128GB/E[S]_trunc * 100%，计算 H_LFU_top = 1 - (1-K) * E[S|H<h_K] / E[S]_trunc，此工作点忽略 LFU 的淘汰开销和冷启动，提供增益上界，计算简单，误差 [待核验] ±3%。

## Corrected Claim

LFU 工作点 1（高性低成）：假设 LFU 完美保留 top-K% 热度对象，K=128GB/E[S]_trunc * 100%，计算 H_LFU_top = 1 - (1-K) * E[S|H<h_K] / E[S]_trunc，此工作点忽略 LFU 的淘汰开销和冷启动，提供增益上界，计算简单，误差 [待核验] ±3%。

## Evidence

父节点级核验未通过：不完备（子节点仅覆盖了 K=100% 这一特定边界情况（即容量充足时的退化情形），而父节点定义了一个通用的计算公式（H_LFU_top 作为 K 的函数）并强调了其作为'增益上界'的特性。子节点没有体现通用计算逻辑，也未涵盖 K < 100% 时的非平凡计算过程，导致对父节点核心内容（通用公式及其上界意义）的覆盖不完整。）

## Search Query

LFU cache top K popular objects hit rate upper bound
