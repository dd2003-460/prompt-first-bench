# N28: 模型幻觉量化监控：利用 Logit 分布熵和 Token 概率阈值监测实时幻觉风险。定义幻觉风险指数 HR = P(token | context) < 0.7

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4, N5, N6

## Claim

模型幻觉量化监控：利用 Logit 分布熵和 Token 概率阈值监测实时幻觉风险。定义幻觉风险指数 HR = P(token | context) < 0.7 的 token 比例，当 HR > 0.15 时触发强制检索验证流程；同时统计长程依赖任务中的事实漂移率（Fact Drift Rate），即第 N 步结论与第 1 步前提的逻辑矛盾次数。

## Corrected Claim

模型幻觉量化监控：利用 Logit 分布熵和 Token 概率阈值监测实时幻觉风险。定义幻觉风险指数 HR = P(token | context) < 0.7 的 token 比例，当 HR > 0.15 时触发强制检索验证流程；同时统计长程依赖任务中的事实漂移率（Fact Drift Rate），即第 N 步结论与第 1 步前提的逻辑矛盾次数。

## Evidence

先验知识/题面给定，逻辑校验通过
