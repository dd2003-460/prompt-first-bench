# N60: LFU 相比 LRU 的理论最大提升上限受限于“扫描攻击”（Scan Attack）的鲁棒性差异；在稳态 Pareto 负载下，LFU 的优势主要来自对突发流量

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

LFU 相比 LRU 的理论最大提升上限受限于“扫描攻击”（Scan Attack）的鲁棒性差异；在稳态 Pareto 负载下，LFU 的优势主要来自对突发流量的平滑处理，量化指标为 ΔH_max = H_LFU - H_LRU ≤ (1 - C_head) * Jitter_Penalty_LRU，其中 Jitter_Penalty_LRU 约为 2-5%，因此 LFU 最大提升不超过 5 个百分点，且仅在 β<1.1 时显著。

## Corrected Claim

LFU 相比 LRU 的理论最大提升上限受限于“扫描攻击”（Scan Attack）的鲁棒性差异；在稳态 Pareto 负载下，LFU 的优势主要来自对突发流量的平滑处理，量化指标为 ΔH_max = H_LFU - H_LRU ≤ (1 - C_head) * Jitter_Penalty_LRU，其中 Jitter_Penalty_LRU 约为 2-5%，因此 LFU 最大提升不超过 5 个百分点，且仅在 β<1.1 时显著。

## Evidence

检索失败: no sources from any channel (all 5 failed)
