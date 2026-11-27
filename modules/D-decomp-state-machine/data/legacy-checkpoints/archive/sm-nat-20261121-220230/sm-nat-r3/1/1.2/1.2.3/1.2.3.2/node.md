# N121: LRU 驻留集合变化率 ΔC 的量化公式：ΔC = (N_evicted + N_inserted) / N_cached，其中 N_evicted 取决于请求

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N39, N40, N41

## Claim

LRU 驻留集合变化率 ΔC 的量化公式：ΔC = (N_evicted + N_inserted) / N_cached，其中 N_evicted 取决于请求到达率 λ 与驱逐阈值 h_th 的交互；在稳态下，ΔC 与 1/T_resident 成正比，需结合 N71 的 T_resident 估算具体百分比。

## Corrected Claim

LRU 驻留集合变化率 ΔC 的量化公式：ΔC = (N_evicted + N_inserted) / N_cached，其中 N_evicted 取决于请求到达率 λ 与驱逐阈值 h_th 的交互；在稳态下，ΔC 与 1/T_resident 成正比，需结合 N71 的 T_resident 估算具体百分比。

## Evidence

先验知识/题面给定，逻辑校验通过
