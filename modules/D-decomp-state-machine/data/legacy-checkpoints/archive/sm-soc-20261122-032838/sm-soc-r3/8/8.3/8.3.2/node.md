# N301: 平台改变算法权重的边际成本 $C_{platform}$ 的分解：$C_{platform} = C_{dev} + C_{retrain} + C_{risk

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N101

## Claim

平台改变算法权重的边际成本 $C_{platform}$ 的分解：$C_{platform} = C_{dev} + C_{retrain} + C_{risk}$。$C_{dev}$ 为开发成本，$C_{retrain}$ 为模型重训练的数据与算力成本，$C_{risk}$ 为因算法调整导致短期用户流失的预期损失。若 $C_{risk} > R_{platform}$，则平台即使有技术能力也不会改变 $W$。[待核验] 需估算模型重训练的典型算力成本及短期流失率对长期 LTV 的影响。

## Corrected Claim

平台改变算法权重的边际成本 $C_{platform}$ 的分解：$C_{platform} = C_{dev} + C_{retrain} + C_{risk}$。$C_{dev}$ 为开发成本，$C_{retrain}$ 为模型重训练的数据与算力成本，$C_{risk}$ 为因算法调整导致短期用户流失的预期损失。若 $C_{risk} > R_{platform}$，则平台即使有技术能力也不会改变 $W$。[待核验] 需估算模型重训练的典型算力成本及短期流失率对长期 LTV 的影响。

## Evidence

先验知识/题面给定，逻辑校验通过：成本分解符合经济学基本逻辑，决策规则（成本>收益则不执行）自洽，无外部来源矛盾。

## Search Query

cost of retraining recommendation algorithm platform user churn risk cost estimation
