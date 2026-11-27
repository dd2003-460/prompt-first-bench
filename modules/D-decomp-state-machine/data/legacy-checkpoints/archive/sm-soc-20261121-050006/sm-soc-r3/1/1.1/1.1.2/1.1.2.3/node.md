# N121: 特征敏感度系数 λ_x 的回归系数向量为 [0.2, -0.1, 0.15, 0.05]（对应品类、品牌、成色、图片数量），表明非标品类显著增加偏好噪声方差。

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N34

## Claim

特征敏感度系数 λ_x 的回归系数向量为 [0.2, -0.1, 0.15, 0.05]（对应品类、品牌、成色、图片数量），表明非标品类显著增加偏好噪声方差。

## Corrected Claim

特征敏感度系数 λ_x 的回归系数向量为 [0.2, -0.1, 0.15, 0.05]（对应品类、品牌、成色、图片数量），表明非标品类对偏好噪声方差有正向影响（具体幅度需结合模型上下文确认）。

## Evidence

[质询]参考来源均为Lasso回归的通用教程或代码示例，未包含任何关于“特征敏感度系数 λ_x”的具体数值、特定业务场景（品类/品牌等）或“非标品类增加偏好噪声方差”的实证结论，属于来源与事实主题不匹配，无法提供直接支持。 | 逻辑上，回归系数向量表示特征对目标变量的线性影响，若“非标品类”对应系数为正（0.2），且目标变量为“偏好噪声方差”，则逻辑自洽；但参考来源[1][2][3]仅讨论Lasso回归原理，与该具体事实无关，无外部证据支持。

## Search Query

regression coefficients feature sensitivity preference noise variance

## Retrieval Sources

- {'url': 'https://blog.csdn.net/HBLKMMU/article/details/157358983&rut=0da94bf29abe784c970542bb8fbdd302f8766dcc1fa3a30cca6f9902d860a9c4', 'type': 'ddg', 'title': 'R语言实战：Lasso回归实现及结果解读 - CSDN博客'}
- {'url': 'https://blog.csdn.net/u013172930/article/details/142389580&rut=4a5359eeefe80644d229819b14d3ef2ea92a040ead487b6ac9f05d3e8c62a363', 'type': 'ddg', 'title': 'LASSO回归（L1回归L1正则化）举例说明：正则化项使不重要的特征系数逐渐为零0的过程_lasso回归前的数据标准化-'}
- {'url': 'https://ask.csdn.net/questions/8366023&rut=16a67547b057d134fae5faf2505713ab228a7b656e6060e891db53c28cde0be6', 'type': 'ddg', 'title': 'Lasso回归中，如何通过Lambda值变化解释特征选择过程？_编程语言-CSDN问答'}
