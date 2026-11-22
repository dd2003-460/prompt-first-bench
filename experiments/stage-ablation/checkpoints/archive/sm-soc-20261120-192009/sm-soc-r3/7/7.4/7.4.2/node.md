# N313: 算法权重敏感性阈值：若平台排序分 Score = w_ctr * CTR + w_conv * Conv，当 w_ctr / w_conv > 5 时，高挂价商

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N107

## Claim

算法权重敏感性阈值：若平台排序分 Score = w_ctr * CTR + w_conv * Conv，当 w_ctr / w_conv > 5 时，高挂价商品（CTR 高但 Conv 低）的曝光时长 T_exposure_high 才会显著高于正常组；需通过 A/B 测试或日志回归估计 w_ctr / w_conv 的实际比值，若比值 < 3 则 Ratio_Exposure ≈ 1.0，假设失效。

## Corrected Claim

算法权重敏感性：若平台排序分 Score = w_ctr * CTR + w_conv * Conv，当 w_ctr / w_conv 显著大于 1 时，高挂价商品（CTR 高但 Conv 低）的曝光时长 T_exposure_high 可能高于正常组；具体阈值需通过 A/B 测试或日志回归估计，若比值接近 1 则 Ratio_Exposure ≈ 1.0。

## Evidence

[质询]该陈述中的具体数值阈值（w_ctr/w_conv > 5 和 < 3）属于特定平台或实验的经验性参数，并非通用物理或数学定律，且参考来源未提供这些具体数值，存在将特定场景经验值泛化为通用规则的风险。 | 逻辑上，若CTR权重远高于Conv权重，高CTR低Conv商品确实会获得更高排序分，逻辑自洽；但参考来源[1]仅讨论电商搜索系统架构，未涉及具体权重敏感性阈值，属于经验事实且缺乏直接来源支持。

## Search Query

e-commerce platform ranking algorithm weight click-through rate vs conversion rate empirical estimation

## Retrieval Sources

- {'url': 'https://arxiv.org/pdf/2405.05606&rut=67e27ed91078713be0620677843e0dbcf58b1a40089376988b329723dc4cd70b', 'type': 'ddg', 'title': 'Optimizing E-commerce Search: Toward a Generalizable and Rank ...'}
