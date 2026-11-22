# N88: 推荐价差 P_rec 的基准值设定为 5%，即推荐价格 P_rec_price = C_ref * (1 - 5%)，其中 C_ref 为近期同品类成交均价，需

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N20

## Claim

推荐价差 P_rec 的基准值设定为 5%，即推荐价格 P_rec_price = C_ref * (1 - 5%)，其中 C_ref 为近期同品类成交均价，需根据商品标准化程度调整 [待核验]

## Corrected Claim

推荐价差 P_rec 的基准值设定为 5%（需根据具体业务场景或平台规则验证），即推荐价格 P_rec_price = C_ref * (1 - 5%)，其中 C_ref 为近期同品类成交均价。

## Evidence

[质询]该陈述包含具体的经验参数（5%基准值）和特定的业务逻辑（基于近期同品类成交均价调整），属于经验事实。参考来源[1]和[2]讨论的是推荐算法的评估指标（如Precision, Recall），与定价策略无关；来源[3]讨论的是亚马逊平台的Buy Box推荐报价百分比，虽然涉及推荐价格，但并未提及“5%”这一具体基准值，也未提及“近期同品类成交均价”作为基准C_ref的定义。因此，缺乏直接来源支持该具体数值和逻辑。 | 经验事实，逻辑自洽但缺来源支持。来源[1][2]主题无关，来源[3]主题相关但未提供具体数值支持。

## Search Query

dynamic pricing recommendation algorithm secondhand market discount rate

## Retrieval Sources

- {'url': 'https://blog.csdn.net/qq_39381654/article/details/114546621&rut=f2e949ab85b9c71786925df2d8a058a4415d46096d0ee1bbe1ba0643bb47aa39', 'type': 'ddg', 'title': '【科研分享】推荐算法指标总结（ACC，Precision，Recall，F1，FPR，TPR，ROC，AUC，MAP，M'}
- {'url': 'https://blog.csdn.net/Mr_Suda/article/details/122025282&rut=c56d84ec811bdbf225572d345991c164944400515eef18194ac96905660127d6', 'type': 'ddg', 'title': '召回率（rec），准确率（acc），精确率（pre），F1值-CSDN博客'}
- {'url': 'https://www.10100.com/encyclopedia/6/50637205&rut=4386a2eea72ffa0b0eb80b4a51b234abf1db24033d85cb5d1df15dc37649ab3e', 'type': 'ddg', 'title': '亚马逊推荐报价百分比是什么_跨境百科'}
