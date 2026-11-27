# N104: 损失厌恶系数 λ 的品类异质性：λ 并非全局常数，而是随商品品类（如奢侈品 vs 日用品）变化，需建立 λ = f(category, brand_tier) 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N26, N27, N28

## Claim

损失厌恶系数 λ 的品类异质性：λ 并非全局常数，而是随商品品类（如奢侈品 vs 日用品）变化，需建立 λ = f(category, brand_tier) 的回归模型，估计不同品类下的 λ 均值及置信区间。

## Corrected Claim

损失厌恶系数 λ 在前景理论中通常被视为一个反映个体对损失敏感度的参数（典型值约为2-2.5），但在具体应用建模中，可假设其随商品品类（如奢侈品 vs 日用品）变化，需通过实证数据建立 λ = f(category, brand_tier) 的回归模型来估计不同品类下的 λ 均值及置信区间。

## Evidence

[质询]参考来源仅提供了损失厌恶系数λ的一般定义和典型量级（2-2.5倍），并未提供关于λ随商品品类（如奢侈品vs日用品）变化的实证数据或回归模型证据，属于将一般性理论参数具体化为特定品类异质性模型的过度推断。 | 来源[1]和[2]确认了λ作为损失厌恶系数的定义及一般量级，但未覆盖品类异质性这一具体经验事实，逻辑上自洽但缺乏直接来源支持。

## Search Query

loss aversion coefficient heterogeneity by product category luxury vs everyday items

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2037969346610319770&rut=9a70962219a42a66575d64dde1987b011fc59cd86a5da8f87ce40dcac1e7e926', 'type': 'ddg', 'title': '损失厌恶（loss aversion）测量方式归纳 - 知乎'}
- {'url': 'https://zh.wikipedia.org/zh-hans/%E6%8D%9F%E5%A4%B1%E8%A7%84%E9%81%BF&rut=60b54fb2d055a0b3c497c717054d2531b227311ac378633bb85f1e3630f6f837', 'type': 'ddg', 'title': '损失规避 - 维基百科，自由的百科全书'}
