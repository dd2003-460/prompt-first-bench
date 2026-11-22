# N37: T_resident 的具体数值依赖于 N_cap 和访问间隔分布：对于第 i 个最热门对象，其驻留时间由第 N_cap+1 个对象的访问间隔决定，需通过 Pa

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N8

## Claim

T_resident 的具体数值依赖于 N_cap 和访问间隔分布：对于第 i 个最热门对象，其驻留时间由第 N_cap+1 个对象的访问间隔决定，需通过 Pareto(β=0.9) 的逆 CDF 计算第 N_cap 个对象的平均访问间隔 Δt_Ncap 作为 T_resident 的近似。

## Corrected Claim

T_resident 的具体数值依赖于 N_cap 和访问间隔分布：对于第 i 个最热门对象，其驻留时间由第 N_cap+1 个对象的访问间隔决定，需通过 Pareto(β=0.9) 的逆 CDF 计算第 N_cap 个对象的平均访问间隔 Δt_Ncap 作为 T_resident 的近似。

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点本质上是同一通用公式（T_resident ≈ 1/f_{N_cap+1}）在三个不同 N_cap 参数下的具体实例，存在高度冗余；且父节点明确提到的核心计算步骤‘通过 Pareto(β=0.9) 的逆 CDF 计算第 N_cap 个对象的平均访问间隔 Δt_Ncap’在子节点中完全缺失，仅给出了频率近似，未覆盖父节点关于‘如何从分布计算驻留时间’的方法论关键方面。）
