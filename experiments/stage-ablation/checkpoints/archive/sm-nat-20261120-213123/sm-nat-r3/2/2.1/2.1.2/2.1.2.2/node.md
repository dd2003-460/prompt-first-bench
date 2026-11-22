# N91: s_min 取值对归一化容量 c 的杠杆效应：c = C/E[S]，当 s_min 从 1KB 增至 10KB 时，E[S] 从 11.3KB 增至 113KB

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N35

## Claim

s_min 取值对归一化容量 c 的杠杆效应：c = C/E[S]，当 s_min 从 1KB 增至 10KB 时，E[S] 从 11.3KB 增至 113KB，c 从 1.13×10^7 降至 1.13×10^6，即 c 减少 10 倍；由于 k_eff ∝ c^0.9（近似），s_min 的 10 倍变化导致有效驻留对象数减少约 8 倍，直接影响命中率下界。

## Corrected Claim

s_min 取值对归一化容量 c 的杠杆效应：c = C/E[S]，当 s_min 从 1KB 增至 10KB 时，E[S] 从 11.3KB 增至 113KB，c 从 1.13×10^7 降至 1.13×10^6，即 c 减少 10 倍；由于 k_eff ∝ c^0.9（近似），s_min 的 10 倍变化导致有效驻留对象数减少约 8 倍，直接影响命中率下界。

## Evidence

先验知识/题面给定，逻辑校验通过：c与E[S]成反比，E[S]增10倍则c减10倍；k_eff ∝ c^0.9，c减10倍则k_eff减10^0.9≈7.94倍（约8倍），推导自洽。
