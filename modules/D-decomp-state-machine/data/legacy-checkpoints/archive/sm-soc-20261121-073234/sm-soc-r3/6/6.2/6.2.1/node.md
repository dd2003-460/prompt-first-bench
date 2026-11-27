# N315: 价格溢价率与决策时间回归模型中，商品类别虚拟变量（Category_dummies）的控制系数：不同类别（如3C数码 vs 服装）的基础决策时间差异显著，需列出

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N106

## Claim

价格溢价率与决策时间回归模型中，商品类别虚拟变量（Category_dummies）的控制系数：不同类别（如3C数码 vs 服装）的基础决策时间差异显著，需列出主要类别的截距项偏移量 δ_category，以排除类别混淆偏差。

## Corrected Claim

在价格溢价率与决策时间回归模型中，应引入商品类别虚拟变量（Category_dummies）以控制类别混淆偏差；不同类别（如3C数码与服装）的基础决策时间是否存在显著差异，需依据具体数据集的回归系数显著性检验结果确定。

## Evidence

[质询]该陈述包含具体的经验性结论（如“3C数码 vs 服装的基础决策时间差异显著”），这属于特定数据集下的统计结果，无法从第一性原理或通用理论中直接推导得出，且参考来源仅提供了方法论支持，未提供该具体场景下的实证数据。 | 来源[1]和[2]直接支持使用虚拟变量控制类别混淆偏差的方法论（逻辑自洽），但均为通用教程，未提供“3C数码与服装决策时间差异显著”这一具体经验事实的直接证据，故依据经验事实排除条款降级。

## Search Query

regression analysis price premium decision time controlling for product category fixed effects second hand market

## Retrieval Sources

- {'url': 'https://blog.csdn.net/qq_40206371/article/details/122789335&rut=0ce640cb8bbd4371d0c55482258d6f11f6a07aa63a95ee5de60df5e783b1f144', 'type': 'ddg', 'title': '机器学习（时间序列）：线性回归之虚拟变量 dummy variables'}
- {'url': 'https://www.cnblogs.com/haohai9309/p/18475191&rut=be95fa9d4e03d95473329db69d0f0dd72b98a65b24595e60c0133282025a4d61', 'type': 'ddg', 'title': '计量经济学 (十二)——虚拟变量回归模型 - 郝hai - 博客园'}
