# N115: 卖家流失率预测：预计 15% 低活跃卖家流失的模型基础；需基于卖家效用损失分布和流失倾向函数 Churn_Probability = f(ΔU_seller, 

- **status**: verified
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N32

## Claim

卖家流失率预测：预计 15% 低活跃卖家流失的模型基础；需基于卖家效用损失分布和流失倾向函数 Churn_Probability = f(ΔU_seller, Seller_Activity_Level) 进行模拟，验证 15% 这一数值的合理性。

## Corrected Claim

卖家流失率预测：需基于卖家效用损失分布和流失倾向函数 Churn_Probability = f(ΔU_seller, Seller_Activity_Level) 进行模拟，以验证低活跃卖家流失率的具体数值（如 15%）的合理性。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点逻辑清晰且互不重叠：节点1定义了预测模型（函数形式），节点2定义了输入数据的生成过程（特征分布），节点3定义了验证方法（统计推断）。三者分别对应模型构建、数据准备和结果验证，覆盖了父节点中'模型基础'、'模拟输入'和'验证合理性'的所有关键方面，且不存在参数冗余。）

## Search Query

seller churn rate prediction model utility loss marketplace

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/482994067&rut=0c44df47b650fe71d44486fc4ef155e593f02c8276fde35c647d1317a6849269', 'type': 'ddg', 'title': '干货!用户流失预警模型及策略干预 - 知乎'}
