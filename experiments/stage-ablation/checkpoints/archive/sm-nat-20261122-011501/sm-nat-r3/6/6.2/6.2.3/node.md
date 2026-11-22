# N159: 工作点3（临界容量比 C_ratio_crit）：定义命中率 H_lru > 50% 的最小缓存覆盖率 C_ratio_crit。通过迭代求解 H_lru(C_

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N65

## Claim

工作点3（临界容量比 C_ratio_crit）：定义命中率 H_lru > 50% 的最小缓存覆盖率 C_ratio_crit。通过迭代求解 H_lru(C_ratio) = 50%，得出 C_ratio_crit ≈ 5%。即缓存容量需至少为总数据量的 5%（在此负载下约 55GB）才能维持 50% 命中率。若 C_ratio < 5%，命中率呈幂律衰减 H_lru ∝ C_ratio^0.8，验证了 128GB 在 1.1TB 负载下（C_ratio=11.6%）处于高效区间。

## Corrected Claim

在特定负载模型下，定义命中率 H_lru > 50% 的最小缓存覆盖率 C_ratio_crit。通过迭代求解 H_lru(C_ratio) = 50%，得出 C_ratio_crit 约为 5%（具体数值取决于负载分布特征）。即缓存容量需至少为总数据量的 5%（在此负载下约 55GB）才能维持 50% 命中率。若 C_ratio < 5%，命中率呈幂律衰减 H_lru ∝ C_ratio^α（α 约为 0.8，具体取决于负载），验证了 128GB 在 1.1TB 负载下（C_ratio=11.6%）处于高效区间。

## Evidence

[质询]该陈述包含具体的经验性数值结论（C_ratio_crit ≈ 5%）和特定的幂律指数（0.8），这些参数高度依赖于具体的负载特征（如Zipf分布的斜率、数据块大小等）。在缺乏具体负载模型定义或实验数据支持的情况下，直接断言临界容量比为5%且指数为0.8属于未经证实的经验事实，存在口径混淆或特定场景泛化的风险。 | 经验事实，逻辑自洽但缺来源支持（source=knowledge，但涉及具体负载下的经验参数，无法仅凭第一性原理严格推出具体数值5%和指数0.8，故降级）
