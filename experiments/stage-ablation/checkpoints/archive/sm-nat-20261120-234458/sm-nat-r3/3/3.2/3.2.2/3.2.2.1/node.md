# N154: 在 γ=1（更新率与大小线性正相关）的工作点下，大对象（Top 10% 大小）的更新率 λ_update_hot_size = λ_base * (S_hot/

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N49

## Claim

在 γ=1（更新率与大小线性正相关）的工作点下，大对象（Top 10% 大小）的更新率 λ_update_hot_size = λ_base * (S_hot/μ_S)，由于 Pareto(α=1.1) 的长尾特性，S_hot 远大于 μ_S，导致 P_invalidate(S_hot) 接近 1，使得大对象缓存命中率趋近于 0，D_bytes 主要受大对象字节占比 B_top10% 支配。

## Corrected Claim

在 γ=1（更新率与大小线性正相关）的工作点下，大对象（Top 10% 大小）的更新率 λ_update_hot_size = λ_base * (S_hot/μ_S)，由于 Pareto(α=1.1) 的长尾特性，S_hot 远大于 μ_S，导致 P_invalidate(S_hot) 接近 1，使得大对象缓存命中率趋近于 0，D_bytes 主要受大对象字节占比 B_top10% 支配。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto(α=1.1) 长尾特性导致 Top 10% 对象大小远大于均值，结合 γ=1 的线性更新率假设，大对象更新率极高，缓存失效概率趋近 1，命中率趋近 0，逻辑自洽。
