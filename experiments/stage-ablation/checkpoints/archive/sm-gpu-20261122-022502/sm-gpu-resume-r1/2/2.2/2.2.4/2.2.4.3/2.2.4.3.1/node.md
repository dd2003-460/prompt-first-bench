# N600: vLLM 在 MI300X 上启用 PagedAttention 时的实测吞吐损失率为 15%（相对于理论峰值），主要源于 ROCm 对非连续内存块（Paged

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N184

## Claim

vLLM 在 MI300X 上启用 PagedAttention 时的实测吞吐损失率为 15%（相对于理论峰值），主要源于 ROCm 对非连续内存块（Paged Blocks）的 Gather/Scatter 操作优化不足，导致内存访问局部性差。

## Corrected Claim

vLLM 在 MI300X 上启用 PagedAttention 时可能存在一定的吞吐损失，主要源于非连续内存块（Paged Blocks）导致的内存访问局部性差及 ROCm 相关操作优化问题，但具体损失率需依据实际基准测试确定。

## Evidence

[质询]该陈述包含具体的实测数值（15%）和特定的技术归因（ROCm Gather/Scatter优化不足），属于经验事实。在缺乏任何参考来源支持的情况下，无法验证该具体数值和归因的准确性，且不同配置下损失率可能波动，单一数值可能具有误导性。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）。PagedAttention 确实涉及非连续内存访问，可能导致性能损失，但具体 15% 的数值及归因无法通过第一性原理推导，需外部数据佐证。

## Search Query

vLLM PagedAttention performance loss AMD MI300X ROCm benchmark
