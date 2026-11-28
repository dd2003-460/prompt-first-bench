# N77: 引用准确率 (Citation Precision) = 正确引用的文献数 / 总引用文献数；引用召回率 (Citation Recall) = 被正确引用的关

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N25

## Claim

引用准确率 (Citation Precision) = 正确引用的文献数 / 总引用文献数；引用召回率 (Citation Recall) = 被正确引用的关键文献数 / 实际支持结论的关键文献总数；需构建 Ground Truth 关键文献集，Precision 阈值 0.95，Recall 阈值 0.80，综合得分公式 Score = 0.4*FactScore + 0.3*P(logic) + 0.3*(0.5*Prec + 0.5*Rec)。

## Corrected Claim

引用准确率 (Citation Precision) = 正确引用的文献数 / 总引用文献数；引用召回率 (Citation Recall) = 被正确引用的关键文献数 / 实际支持结论的关键文献总数；需构建 Ground Truth 关键文献集，Precision 阈值 0.95，Recall 阈值 0.80，综合得分公式 Score = 0.4*FactScore + 0.3*P(logic) + 0.3*(0.5*Prec + 0.5*Rec)。

## Evidence

先验知识/题面给定，逻辑校验通过：定义符合信息检索标准范式，权重和为1，量纲一致，无内部矛盾。

## Search Query

citation precision recall calculation formula academic paper evaluation
