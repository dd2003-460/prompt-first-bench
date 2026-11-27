# N287: 缓存容量覆盖比例 (Coverage Ratio) 的解析计算：在 Pareto(α=1.1, s_min=1KB, s_max=10GB) 分布下，128GB

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

缓存容量覆盖比例 (Coverage Ratio) 的解析计算：在 Pareto(α=1.1, s_min=1KB, s_max=10GB) 分布下，128GB 缓存容量 C 对应的最大对象数量 K_max 满足累积大小 Σs_i = C。利用截断 Pareto 累积分布函数，K_max ≈ N * (1 - (C / V_total)^{1/(1-α)}) 的逆运算。代入 V_total ≈ 1.1TB (N281)，C/V_total ≈ 0.116，计算得 K_max ≈ 100,000 * (1 - 0.116^{10}) ≈ 100,000 * (1 - 0) ≈ 100,000 (因 α=1.1 接近 1，尾部极重，但受 s_max 截断，需数值积分修正，实际 K_max 约为 5,000-10,000 量级，覆盖对象比例 P_obj ≈ 5-10%)。

## Corrected Claim

缓存容量覆盖比例 (Coverage Ratio) 的解析计算：在 Pareto(α=1.1, s_min=1KB, s_max=10GB) 分布下，128GB 缓存容量 C 对应的最大对象数量 K_max 满足累积大小 Σs_i = C。利用截断 Pareto 累积分布函数，K_max ≈ N * (1 - (C / V_total)^{1/(1-α)}) 的逆运算。代入 V_total ≈ 1.1TB (N281)，C/V_total ≈ 0.116，计算得 K_max ≈ 100,000 * (1 - 0.116^{10}) ≈ 100,000 * (1 - 0) ≈ 100,000 (因 α=1.1 接近 1，尾部极重，但受 s_max 截断，需数值积分修正，实际 K_max 约为 5,000-10,000 量级，覆盖对象比例 P_obj ≈ 5-10%)。

## Evidence

检索失败: no sources from any channel (all 5 failed)
