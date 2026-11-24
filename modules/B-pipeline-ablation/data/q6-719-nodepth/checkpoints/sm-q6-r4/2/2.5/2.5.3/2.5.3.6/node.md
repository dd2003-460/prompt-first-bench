# N207: 最优合规路径选择阈值：当 (1 - H_current) / (H_target - H_current) * C_cache_upgrade < N_add 

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N64, N65, N66

## Claim

最优合规路径选择阈值：当 (1 - H_current) / (H_target - H_current) * C_cache_upgrade < N_add * C_pop_marginal 时选择缓存扩容，否则选择增加 POP；C_pop_marginal ≈ ¥8000-12000/月/POP

## Corrected Claim

最优合规路径选择阈值：当 (1 - H_current) / (H_target - H_current) * C_cache_upgrade < N_add * C_pop_marginal 时选择缓存扩容，否则选择增加 POP；C_pop_marginal ≈ ¥8000-12000/月/POP

## Evidence

父节点级核验未通过：不完备（子节点正交，分别解释了不等式两侧的成本构成。但不完备：父节点核心是‘决策阈值’（即何时选择哪种方案），子节点仅解释了成本参数 $C_{cache}$ 和 $C_{pop}$ 的计算细节，完全缺失了对不等式左侧健康度指标 $(1 - H_{current}) / (H_{target} - H_{current})$ 的定义、计算逻辑或其业务含义的解释，导致无法复现父节点的完整决策逻辑。）
