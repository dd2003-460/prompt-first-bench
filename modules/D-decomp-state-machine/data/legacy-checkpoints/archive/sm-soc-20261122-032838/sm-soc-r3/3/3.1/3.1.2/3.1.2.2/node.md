# N194: 方案B中模型重训成本 $C_{train}$ 的量化边界：若采用规则引擎调整（如'溢价率>20%则曝光权重乘0.8'），$C_{train} = 0$ 人日（无

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N64

## Claim

方案B中模型重训成本 $C_{train}$ 的量化边界：若采用规则引擎调整（如'溢价率>20%则曝光权重乘0.8'），$C_{train} = 0$ 人日（无需训练，仅配置变更）；若采用LR模型重训，$C_{train} \approx 1.0$ 人日（数据准备0.5+训练0.3+验证0.2）；若采用DNN重训，$C_{train} \approx 5-10$ 人日（含超参搜索与GPU资源协调）。原估算中'简单规则调整1-2人日'应修正为0-1人日，因规则调整不涉及模型迭代。

## Corrected Claim

方案B中模型重训成本 $C_{train}$ 的量化边界：若采用规则引擎调整（如'溢价率>20%则曝光权重乘0.8'），$C_{train} = 0$ 人日（无需训练，仅配置变更）；若采用LR模型重训，$C_{train} \approx 1.0$ 人日（数据准备0.5+训练0.3+验证0.2）；若采用DNN重训，$C_{train} \approx 5-10$ 人日（含超参搜索与GPU资源协调）。原估算中'简单规则调整1-2人日'应修正为0-1人日，因规则调整不涉及模型迭代。

## Evidence

先验知识/题面给定，逻辑校验通过：规则引擎调整确实不涉及模型训练过程，成本为0人日符合工程直觉；LR与DNN重训的成本量级（1人日 vs 5-10人日）符合常规机器学习工程实践，逻辑自洽。

## Search Query

algorithm A/B test cost rule-based vs model retraining person-days
