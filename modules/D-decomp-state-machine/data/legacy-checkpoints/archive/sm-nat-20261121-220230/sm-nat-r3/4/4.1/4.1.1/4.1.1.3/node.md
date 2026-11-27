# N188: 工作点C（Joe-Clayton Copula, θ=0.8）：使用 Joe-Clayton Copula 建模负相关 ρ=-0.3，参数 θ≈0.8。Joe-

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N64

## Claim

工作点C（Joe-Clayton Copula, θ=0.8）：使用 Joe-Clayton Copula 建模负相关 ρ=-0.3，参数 θ≈0.8。Joe-Clayton 支持负相关，且在尾部相关性捕捉上优于 Frank。计算复杂度中等，解析近似误差 <2%。该工作点代表中性价比最优场景，适用于需要精确量化 LFU 增益上限的场景。

## Corrected Claim

工作点C（Joe-Clayton Copula）：使用 Joe-Clayton Copula 建模负相关 ρ=-0.3。Joe-Clayton 支持负相关，且在尾部相关性捕捉上优于 Frank。计算复杂度中等。该工作点代表中性价比最优场景，适用于需要精确量化 LFU 增益上限的场景。

## Evidence

[质询]Joe-Clayton Copula 的参数 θ 通常定义在 [0, 1] 区间，且 θ=0 对应独立（ρ=0），θ 越大相关性越强。对于负相关 ρ=-0.3，θ 应为正值但较小（通常远小于 0.8，具体取决于公式定义，若使用标准 Joe-Clayton 公式，负相关通常对应 θ 在 0 到 1 之间，但 ρ=-0.3 对应的 θ 值需通过特定公式计算，通常不会恰好是 0.8 这样较大的值，除非使用了非标准的参数化或符号约定。此外，'解析近似误差 <2%' 是一个具体的经验性能指标，缺乏通用理论支持，属于特定实现或特定场景下的经验数据，而非 Copula 本身的固有属性。 | 先验知识/题面给定，逻辑校验通过。虽然 Joe-Clayton 确实支持负相关且常用于尾部依赖建模，但 θ≈0.8 对应 ρ=-0.3 的具体数值映射存在疑点（通常 θ 与 ρ 的关系是非线性的，且负相关时 θ 值通常较小或需特定公式转换），且 '误差 <2%' 为经验性断言。鉴于 source 为 knowledge，逻辑大体自洽（Copula 类型选择合理），但具体参数数值和误差指标缺乏严格推导支持，故降级为 degraded 以保留定性描述。

## Search Query

Joe-Clayton Copula negative correlation tail dependence
