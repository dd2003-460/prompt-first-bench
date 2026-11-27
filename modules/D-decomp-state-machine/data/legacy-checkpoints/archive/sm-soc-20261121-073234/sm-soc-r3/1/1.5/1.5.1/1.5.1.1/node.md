# N147: 商品情感依附指数 I_type 的量化计算：I_type = w1*(品牌稀缺性评分/10) + w2*(买家平均持有年限/5)，其中 w1=0.6, w2=0

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N43

## Claim

商品情感依附指数 I_type 的量化计算：I_type = w1*(品牌稀缺性评分/10) + w2*(买家平均持有年限/5)，其中 w1=0.6, w2=0.4，需通过历史成交数据回归确定权重以验证 γ > 0 的显著性。

## Corrected Claim

商品情感依附指数 I_type 可通过品牌稀缺性与持有年限加权计算，具体权重需通过历史数据回归确定，以验证其与情感依附的正相关性。

## Evidence

[质询]该公式及具体权重（w1=0.6, w2=0.4）属于特定模型或假设下的经验性设定，并非通用的第一性原理推导结果；参考来源仅提及品牌情感/价值评估的宏观概念，未提供该具体量化公式或权重参数，存在来源不支持具体数值细节的风险。 | 逻辑自洽（量纲归一化合理，回归验证逻辑通顺），但参考来源[1][2]仅涉及品牌情感评估的定性或宏观框架，未直接支持该特定公式及权重数值，属于经验事实且缺直接来源支持。

## Search Query

sentiment attachment index formula second hand market pricing

## Retrieval Sources

- {'url': 'https://blog.csdn.net/2501_91474102/article/details/149942737&rut=4261b4f7b31d6de59f2060718d42f00466b43b949c2ee215558d3b6ca4aed597', 'type': 'ddg', 'title': '干货：品牌价值评估的AI量化指标计算手册，架构师都在查的工具书_品牌情感倾向指数ai-CSDN博客'}
- {'url': 'https://blog.csdn.net/2501_91490244/article/details/152787493&rut=b6867e156dd07eeb52395b7568e5efe19eef8621546fd229fbe4dfc2a5c6da36', 'type': 'ddg', 'title': '多智能体系统在品牌情感联系评估中的应用：超越财务指标-csdn博客'}
