# N193: 当 Self-Consistency < 0.85 时，路由决策树的第一级判断为：若任务涉及外部事实检索（Fact-Checking），强制进入 cloud_a

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N68

## Claim

当 Self-Consistency < 0.85 时，路由决策树的第一级判断为：若任务涉及外部事实检索（Fact-Checking），强制进入 cloud_api (GPT-4o/Claude)；若任务为纯逻辑推导或创意生成，进入 human_review 队列。

## Corrected Claim

在某些基于Self-Consistency评分的路由系统中，可能存在如下逻辑：当评分低于特定阈值（如0.85）时，涉及外部事实检索的任务被路由至云端大模型API，而纯逻辑或创意任务则进入人工审核队列。

## Evidence

[质询]该陈述描述了一个具体的系统架构设计（路由决策树逻辑及阈值0.85），属于特定系统的实现细节或经验性配置，并非通用的第一性原理或数学公理。虽然逻辑上自洽（即如果定义了这样的规则，流程是通顺的），但缺乏外部来源证明这是某个标准系统或广泛认可的通用做法，存在‘虚构具体参数’的风险。 | source=knowledge，逻辑自洽（条件分支清晰，无内部矛盾），但该事实包含具体阈值(0.85)和特定路由策略，属于经验性系统设计细节，非普适真理，且无外部来源佐证其普遍性或特定归属，故降级为定性表述。
