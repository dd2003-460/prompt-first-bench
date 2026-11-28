# N117: 人工评审新颖度评分的偏差校正：Human Novelty Score_raw 受评审者偏好影响，需通过标准化处理 Score_normalized = (Sco

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N40

## Claim

人工评审新颖度评分的偏差校正：Human Novelty Score_raw 受评审者偏好影响，需通过标准化处理 Score_normalized = (Score_raw - Mean_reviewer_bias) / Std_dev，其中 Mean_reviewer_bias 为多位评审者对同一组假设评分的平均偏差；若未经校正，27B 模型生成的假设可能被低估 0.5-1.0 分，导致误判为能力瓶颈；需收集至少 10 位领域专家的评分以计算可靠的 Bias 参数。

## Corrected Claim

人工评审新颖度评分的偏差校正：Human Novelty Score_raw 受评审者偏好影响，需通过标准化处理 Score_normalized = (Score_raw - Mean_reviewer_bias) / Std_dev 进行校正，以避免因评审偏差导致对模型生成假设能力的误判；Bias 参数的计算通常需要收集足够数量的领域专家评分以保证统计可靠性。

## Evidence

[质询]该陈述包含具体的经验参数（如“低估0.5-1.0分”、“至少10位专家”），这些数值并非从第一性原理或数学公理中严格推导出的必然结论，而是依赖于特定实验环境、评审群体和模型版本的经验观察值，缺乏普适的理论基础。 | 逻辑自洽（标准化公式符合统计学常识，偏差校正方向合理），但作为knowledge节点，其包含的具体量化阈值（0.5-1.0分、10人）属于经验事实，虽无来源矛盾，但无法仅凭逻辑推导确认为绝对真理，故降级为定性表述。

## Search Query

human evaluation bias correction LLM generated hypotheses
