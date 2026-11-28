# N29: 评估基准对齐：'可发表级' 输出需通过三个指标：(1) 事实一致性（Factuality Score > 0.9，基于 n-gram 重叠），(2) 逻辑连贯性

- **status**: degraded
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N4, N5, N6

## Claim

评估基准对齐：'可发表级' 输出需通过三个指标：(1) 事实一致性（Factuality Score > 0.9，基于 n-gram 重叠），(2) 逻辑连贯性（Coherence Score > 0.85，基于 LLM-as-judge），(3) 新颖性（Novelty Index > 0.3，基于引用网络距离）。

## Corrected Claim

在该特定评估框架中，‘可发表级’输出被定义为需满足：事实一致性分数>0.9、逻辑连贯性分数>0.85、新颖性指数>0.3。

## Evidence

[质询]阈值设定（0.9, 0.85, 0.3）及具体评估方法（n-gram, LLM-as-judge, 引用网络距离）属于特定研究框架或项目定义的经验性标准，并非学术界公认的通用‘可发表级’硬性指标，存在将局部标准普遍化的风险。 | source=knowledge，逻辑自洽（指标定义清晰且量纲合理），但作为经验性阈值缺乏通用权威来源支持，依据经验事实排除条款降级。
