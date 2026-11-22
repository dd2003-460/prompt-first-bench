# N26: 负相关修正因子 K_ρ 的矩匹配估算：K_ρ = E[S|f > f_median]^{-1} * E[S]，其中 f_median 为热度分布的中位数，需通过

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N7

## Claim

负相关修正因子 K_ρ 的矩匹配估算：K_ρ = E[S|f > f_median]^{-1} * E[S]，其中 f_median 为热度分布的中位数，需通过联合分布积分计算条件期望，预期 K_ρ ≈ 1.05-1.15 基于 ρ=-0.3 的模拟结果。

## Corrected Claim

负相关修正因子 K_ρ 的矩匹配估算公式为 K_ρ = E[S|f > f_median]^{-1} * E[S]。由于 S 与 f 负相关，理论上 K_ρ > 1，具体数值需依赖联合分布模拟确定（原陈述中 1.05-1.15 为特定模拟结果，缺乏通用来源支持）。

## Evidence

[质询]该陈述包含具体的经验性数值范围（K_ρ ≈ 1.05-1.15）和特定的模拟参数（ρ=-0.3），属于经验事实。参考来源仅涉及信号处理中的匹配滤波器定义，与该统计修正因子的具体数值估算完全无关，无法提供外部支持。 | 逻辑上，若S与f负相关，则E[S|f>f_median] < E[S]，故K_ρ > 1，量级合理；但参考来源[1][2]均与主题无关，且该数值为经验模拟结果，非第一性原理可推导，依据经验事实排除条款降级。

## Search Query

Gaussian copula moment matching negative correlation cache hit rate correction factor

## Retrieval Sources

- {'url': 'https://baike.baidu.com/item/%E5%8C%B9%E9%85%8D%E6%BB%A4%E6%B3%A2/2707915&rut=87892ec5491c1b6f468263716576cb1528481f74f2482d801483d233406b945d', 'type': 'ddg', 'title': '匹配滤波_百度百科'}
- {'url': 'https://zh.wikipedia.org/zh-cn/%E5%8C%B9%E9%85%8D%E6%BF%BE%E6%B3%A2%E5%99%A8&rut=29160dfdc919422173f46447c174dc26e44f0d8d394306b8ff1a0d70365f53df', 'type': 'ddg', 'title': '匹配滤波器 - 维基百科，自由的百科全书'}
