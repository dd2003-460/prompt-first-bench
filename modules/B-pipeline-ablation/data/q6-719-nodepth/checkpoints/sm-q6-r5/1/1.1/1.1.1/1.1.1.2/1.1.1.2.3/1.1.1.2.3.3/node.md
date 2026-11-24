# N1245: '边际效用最优'结论成立的临界条件：当 ΔC_bw < C_quality_gain_value 时，增加对象大小（提高质量）仍具经济性；若 ΔC_bw > ¥

- **status**: degraded
- **level**: L6
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N427

## Claim

'边际效用最优'结论成立的临界条件：当 ΔC_bw < C_quality_gain_value 时，增加对象大小（提高质量）仍具经济性；若 ΔC_bw > ¥1,000/月 且 MOS 提升 < 0.1 分，则边际效用递减，应维持 s_img=0.3 MB 或调整缓存策略以提升 H_img。

## Corrected Claim

‘边际效用最优’结论成立的逻辑条件：当带宽成本增量 ΔC_bw 小于质量提升带来的价值增益时，增加对象大小仍具经济性；若带宽成本增量显著高于质量提升价值（具体阈值需根据业务场景定义），则边际效用递减，应维持当前对象大小或优化缓存策略。

## Evidence

[质询]陈述中引用的具体阈值（如 ¥1,000/月、MOS < 0.1、s_img=0.3 MB）属于特定业务场景下的经验参数，缺乏通用理论依据或题面给定条件支持，存在将特定案例参数泛化为通用临界条件的风险。 | source=knowledge，逻辑框架（边际成本与边际效用比较）自洽，但具体数值阈值缺乏来源支持，依据经验事实排除条款及knowledge节点降级规则（若存在可信攻击点），判定为degraded。

## Search Query

Marginal utility threshold for image quality vs bandwidth cost tradeoff
