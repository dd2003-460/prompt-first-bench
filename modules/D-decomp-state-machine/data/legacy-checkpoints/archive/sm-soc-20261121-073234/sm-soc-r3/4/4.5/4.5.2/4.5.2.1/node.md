# N285: 初始感知质量 Q0 需通过买家对未展示降价历史的同类商品的平均质量评分确定，需控制商品类别和卖家信用等级。

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N93

## Claim

初始感知质量 Q0 需通过买家对未展示降价历史的同类商品的平均质量评分确定，需控制商品类别和卖家信用等级。

## Corrected Claim

初始感知质量 Q0 的确定方法需参考具体的平台算法文档或计量经济学模型设定，通常涉及对同类商品评分的回归分析以控制混淆变量，但当前提供的SAP来源无法证实此具体操作细节。

## Evidence

[质询]来源主题不匹配：参考来源讨论的是SAP ERP系统中的供应商质量信息记录（QIR）配置，属于企业资源计划软件操作范畴；而关键事实节点讨论的是电商平台中基于买家评分的初始感知质量（Q0）确定方法，属于计量经济学或平台算法设计范畴。两者领域完全不同，来源无法支持该事实。 | 逻辑上，控制混淆变量（类别、卖家信用）以确定基线质量是合理的统计方法，但参考来源[1][2]均关于SAP QM模块，与电商感知质量评估无关，无可用外部证据支持。

## Search Query

baseline perceived quality score for used goods without price history

## Retrieval Sources

- {'url': 'https://blog.csdn.net/Lucas1211/article/details/111225940&rut=f4db3fb08ff739b0c643a93f63226ebf1d48a714f1447b7a0308ed72a766fd68', 'type': 'ddg', 'title': '跟着团子学SAP QM-供应商质量信息记录 QI01/QI02/QI03_sap质量信息记录-CSDN博客'}
- {'url': 'https://blog.csdn.net/u5v6w7/article/details/152597427&rut=e4f5bf1d3f8c416efd0b5fb16bcad2d81e4139214246365b53954efa15f71dc1', 'type': 'ddg', 'title': '深入解析sap Qm中的供应商质量信息记录：从qi01到qi03的实战指南-csdn博客'}
