# N120: 量化负相关 ρ=-0.3 下 LRU 驱逐损失的最小化效应：在 LRU 驱逐边界（第 k+1 个对象）处，独立假设下驱逐对象的热度字节流为 r_{k+1} s_

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N45

## Claim

量化负相关 ρ=-0.3 下 LRU 驱逐损失的最小化效应：在 LRU 驱逐边界（第 k+1 个对象）处，独立假设下驱逐对象的热度字节流为 r_{k+1} s_{k+1}^{indep}；负相关下，由于大对象更冷，被驱逐的尾部对象平均热度 r_{tail} 更低，计算相对损失比 R_ρ = (r_{tail}^{ρ} s_{tail}^{ρ}) / (r_{tail}^{indep} s_{tail}^{indep})，预期 R_ρ < 1，从而直接推导 H_LRU_ρ - H_LRU_independent ≈ (1 - R_ρ) * (驱逐字节流占比)。

## Corrected Claim

在量化负相关 ρ=-0.3 的假设下，若忽略时间维度的动态交互，仅从静态尾部对象属性分析，被驱逐对象的平均热度字节流可能低于独立假设，从而推测 LRU 驱逐损失相对减小，但该结论需结合具体访问模式动态模拟验证。

## Evidence

[质询]该陈述将复杂的缓存驱逐动力学简化为静态的尾部对象属性比较，忽略了LRU算法中时间维度（访问间隔）与空间维度（对象大小）的耦合效应，且假设负相关仅通过降低尾部热度来线性影响损失比，缺乏对驱逐频率和缓存命中率动态变化的严谨推导，属于过度简化的经验性直觉而非严格数学推导。 | 经验事实/理论模型结论，逻辑自洽但缺来源支持，且推导过程存在简化假设，无法从第一性原理严格推出，故降级。

## Search Query

LRU eviction cost reduction under negative size-frequency correlation Pareto model
