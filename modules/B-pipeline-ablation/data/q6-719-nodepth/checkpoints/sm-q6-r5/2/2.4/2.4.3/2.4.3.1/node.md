# N191: 到达率 λ (req/s) 的计算：λ = R_daily * K_peak / 86400，其中 R_daily = 1.34×10^9 req/day（基于

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N61

## Claim

到达率 λ (req/s) 的计算：λ = R_daily * K_peak / 86400，其中 R_daily = 1.34×10^9 req/day（基于2TB/1.5MB），K_peak 取峰值系数 4，得 λ ≈ 62,000 req/s

## Corrected Claim

到达率 λ (req/s) 的计算：λ = R_daily * K_peak / 86400，其中 R_daily = 1.34×10^9 req/day（基于2TB/1.5MB），K_peak 取峰值系数 4，得 λ ≈ 62,000 req/s

## Evidence

父节点级核验未通过：不完备（子节点分别描述了峰值和低谷期的系统状态与策略，二者在时间维度和负载水平上互斥，具有正交性。然而，父节点明确给出了基于 K_peak=4 的具体计算过程和结果（λ ≈ 62,000 req/s），而子节点仅引用了结果并扩展了工程含义，完全缺失了父节点中核心的“计算逻辑”和“参数定义”（如 R_daily 的推导、K_peak 的选取依据），导致信息不完备。此外，子节点引入了父节点未提及的“带宽成本”和“后台任务”等无关信息，超出了父节点“到达率计算”的主题范围。）
