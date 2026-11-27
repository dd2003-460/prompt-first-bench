# N150: 噪声源 R_pref 的品类异质性修正项：σ_pref = σ_base * (1 + α_category * Category_Flag)，其中 α_cat

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N41

## Claim

噪声源 R_pref 的品类异质性修正项：σ_pref = σ_base * (1 + α_category * Category_Flag)，其中 α_category 为品类调节系数（如奢侈品 α>0，日用品 α≈0），需检索不同品类二手交易中的价格敏感度方差差异以量化 α。

## Corrected Claim

噪声源 R_pref 的品类异质性修正项可建模为 σ_pref = σ_base * (1 + α_category * Category_Flag)，其中 α_category 为待量化的品类调节系数，需通过实证数据检索不同品类二手交易中的价格敏感度方差差异来确定其具体数值及符号。

## Evidence

[质询]该陈述包含具体的经验性参数设定（如奢侈品α>0，日用品α≈0）及特定的数学修正公式，属于经验事实。参考来源均为无关领域（R语言偏好包、CFD软件设置），无法提供外部支持。虽然逻辑上自洽（作为模型假设），但缺乏实证数据支持其具体数值关系和品类差异的量化结论。 | 经验事实，逻辑自洽但缺来源支持（来源[1][2][3]均与二手交易价格敏感度无关）

## Search Query

category heterogeneity price sensitivity variance used goods luxury vs daily necessities

## Retrieval Sources

- {'url': 'https://cran.r-universe.dev/rPref/doc/manual.html&rut=0dd4146790e4b12c93f388a45c4a7da42a85e291c5bb68e5b1a08f5b8df152e3', 'type': 'ddg', 'title': "Package 'rPref' reference manual - cran.r-universe.dev"}
- {'url': 'https://ask.csdn.net/questions/9333924&rut=6d568847316cfbdc238ce92facf2c6417fb58c76f1a4f83a6d399dd8e7c36d73', 'type': 'ddg', 'title': 'Fluent中空化数公式如何正确设置以匹配实验工况？_编程语言-CSDN问答'}
- {'url': 'https://search.r-project.org/CRAN/refmans/rPref/html/base_pref_macros.html&rut=7c9776cd20c9ebdf02a35511f50c7a868804f45d46a772a63ac87404ee1e7020', 'type': 'ddg', 'title': 'R: Useful Base Preference Macros'}
