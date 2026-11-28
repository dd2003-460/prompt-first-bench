# N22: 定义路由决策函数 Route(task_type, complexity_score, budget_constraint) -> {local_27b, cl

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4, N5, N6

## Claim

定义路由决策函数 Route(task_type, complexity_score, budget_constraint) -> {local_27b, cloud_api, small_model_local}，其中 complexity_score 基于任务所需推理步数（CoT depth）和检索范围量化，cloud_api 仅在 local_27b 预估准确率 < 阈值 T_acc 且 (cost_cloud - cost_local) < value_of_accuracy_gain 时被触发。

## Corrected Claim

定义路由决策函数 Route(task_type, complexity_score, budget_constraint) -> {local_27b, cloud_api, small_model_local}，其中 complexity_score 基于任务所需推理步数（CoT depth）和检索范围量化，cloud_api 仅在 local_27b 预估准确率 < 阈值 T_acc 且 (cost_cloud - cost_local) < value_of_accuracy_gain 时被触发。

## Evidence

先验知识/题面给定，逻辑校验通过：路由决策函数的定义在逻辑上自洽，复杂度评分基于推理深度和检索范围符合常识，云端API触发的成本效益分析（准确率增益价值 > 成本差）符合经济学直觉，无内部矛盾。
