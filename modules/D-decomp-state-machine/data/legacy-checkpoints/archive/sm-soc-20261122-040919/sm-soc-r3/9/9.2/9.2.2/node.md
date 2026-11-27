# N391: 信任度下降系数 d 的实证校准：d 应通过逻辑回归模型 P(no_click | price_drop, features) 估计，其中 price_drop 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N119

## Claim

信任度下降系数 d 的实证校准：d 应通过逻辑回归模型 P(no_click | price_drop, features) 估计，其中 price_drop = (P_ask - P_ref)/P_ref。若回归系数 β_drop 显著为负，则 d = -β_drop。在二手车市场实证中，d 通常介于 0.2 至 0.5 之间。

## Corrected Claim

信任度下降系数 d 可通过逻辑回归模型 P(no_click | price_drop, features) 估计，其中 price_drop = (P_ask - P_ref)/P_ref。若回归系数 β_drop 显著为负，则 d 可近似为 -β_drop。具体数值需根据特定市场数据实证校准，通常需结合具体行业背景确定。

## Evidence

[质询]该陈述包含具体的实证数值范围（d 介于 0.2 至 0.5 之间）和特定的市场场景（二手车），属于经验事实。参考来源均讨论深度学习/LLM 的置信度校准，与二手车市场或价格变动对点击率的影响完全无关，无法提供外部支持。此外，将逻辑回归系数直接等同于信任度下降系数 d 的假设在缺乏具体模型定义的情况下存在口径混淆风险。 | 经验事实，逻辑自洽但缺来源支持（来源 [1][2] 均与二手车市场实证无关，仅涉及 AI 模型校准理论）

## Search Query

used car market price drop buyer trust coefficient regression analysis

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/462034308&rut=ac08c3fbd93214f75ac55556dd3f78f4f2d614a401fb7816df28e61e8022dd90', 'type': 'ddg', 'title': '深度学习模型中的信任危机及校正方法 - 知乎'}
- {'url': 'https://zhuanlan.zhihu.com/p/2044531606715627026&rut=ab9d5550d4236bfa798508c51f97636b82586a9843eb0ffdc7b397f71dafc4fa', 'type': 'ddg', 'title': '模型说"我很确定"其实是在瞎猜？Iclr 2026六种校准方案让llm学会诚实'}
