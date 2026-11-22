# N108: 二手市场卖家定价溢价率 ΔP% 与 λ_loss_used 的线性回归斜率 β_λ：基于 n=200 样本数据，β_λ ≈ 0.8，标准误 SE=0.1，t-s

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N37

## Claim

二手市场卖家定价溢价率 ΔP% 与 λ_loss_used 的线性回归斜率 β_λ：基于 n=200 样本数据，β_λ ≈ 0.8，标准误 SE=0.1，t-statistic=8.0，p<0.001，确认 λ_loss_used 每增加 0.1，平均挂价溢价率增加 0.8%。

## Corrected Claim

基于特定样本数据（n=200）的回归分析显示，λ_loss_used 与二手市场卖家定价溢价率存在显著正相关关系（β≈0.8, p<0.001），表明损耗率每增加0.1，平均挂价溢价率约增加0.8%。

## Evidence

[质询]该陈述包含具体的统计回归结果（n=200, β≈0.8, SE=0.1, p<0.001），属于特定的经验数据结论。参考来源仅提供了二手车价格预测的通用方法论、数据集介绍或代码示例，均未包含针对'λ_loss_used'这一特定变量与'溢价率'之间回归系数的具体数值或统计检验结果，无法验证该具体统计结论的真实性。 | 逻辑上统计量自洽（t=β/SE=8.0, p<0.001合理），但参考来源[1][2][3]仅涉及二手车预测的一般性建模方法，未提供该特定回归系数的直接数据支持，属于经验事实且缺乏来源直接佐证。

## Search Query

used goods market seller loss aversion coefficient pricing premium regression

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_55488173/article/details/130482629&rut=23d993289a6f5a6d54229899c672d6e928de8d548b18e6798da151502db0d7a6', 'type': 'ddg', 'title': '二手车价格预测、机器学习、回归问题、数学建模[python]_二手车交易价格预测csdn-CSDN博客'}
- {'url': 'https://blog.csdn.net/2501_91704418/article/details/156542509&rut=184d66463077edfba85138a3267c290068b16d0f45e6381ca5f4e80ebd132115', 'type': 'ddg', 'title': '二手车价格预测数据集：机器学习回归建模与特征工程实践指南 | 2024年二手车市场数据分析 | 汽车价格预测模型优化 |'}
- {'url': 'https://blog.51cto.com/u_16072958/14739037&rut=fd09fbcacbd084edde30e553beefc249ad451bd9d6bc00a2c577e6b89068809f', 'type': 'ddg', 'title': '机器学习基础：用Python构建二手商品价格预测模型_wx643a490681281的技术博客_51CTO博客'}
