# N124: s_max 截断对 E[s] 的影响量化：当 s_max 从 100MB 增至 1GB 时，由于 α=1.1 接近 1，尾部质量显著增加；需计算 ∫_{100M

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N39, N40, N41

## Claim

s_max 截断对 E[s] 的影响量化：当 s_max 从 100MB 增至 1GB 时，由于 α=1.1 接近 1，尾部质量显著增加；需计算 ∫_{100MB}^{1GB} s * f(s) ds 的占比，预计 E[s] 将增加 30-50%，导致 C_norm 进一步降低，影响命中率下界。

## Corrected Claim

s_max 截断对 E[s] 的影响量化：当 s_max 从 100MB 增至 1GB 时，由于 α=1.1 接近 1，尾部质量显著增加，E[s] 将随之增加（具体增幅取决于分布参数，需通过 ∫_{100MB}^{1GB} s * f(s) ds 计算确定），导致 C_norm 进一步降低，影响命中率下界。

## Evidence

[质询]数值量级缺乏依据：对于 α=1.1 的帕累托分布，截断上限从 100MB 增至 1GB（10倍），期望值 E[s] 的增加幅度取决于分布的具体参数（如最小值 s_min）和归一化方式，断言‘预计增加 30-50%’属于无来源支持的经验性猜测，且未提供计算过程或边界条件，存在将特定场景数值泛化的风险。 | 逻辑上，增大截断上限确实会增加尾部质量从而提升 E[s]，方向正确；但具体‘30-50%’的量化结论属于经验事实/特定模型参数推导，检索无可用来源支持，且无法从第一性原理直接推出该特定百分比区间，故降级。

## Search Query

Pareto distribution tail mass between 100MB and 1GB alpha 1.1
