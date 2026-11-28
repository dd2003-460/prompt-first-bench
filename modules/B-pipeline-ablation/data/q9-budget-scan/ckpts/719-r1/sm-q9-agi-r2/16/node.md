# N107: 人工抽查的最小必要频率（Sampling Rate）应设定为：对于低风险任务（如格式化、简单检索），抽查率为 5%；对于高风险任务（如核心结论推导、异常值解释）

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

人工抽查的最小必要频率（Sampling Rate）应设定为：对于低风险任务（如格式化、简单检索），抽查率为 5%；对于高风险任务（如核心结论推导、异常值解释），抽查率为 30%-50%。该比例基于“贝叶斯风险最小化”模型，假设单次错误的人工修复成本是自动生成的 10 倍。

## Corrected Claim

人工抽查的最小必要频率（Sampling Rate）应设定为：对于低风险任务（如格式化、简单检索），抽查率为 5%；对于高风险任务（如核心结论推导、异常值解释），抽查率为 30%-50%。该比例基于“贝叶斯风险最小化”模型，假设单次错误的人工修复成本是自动生成的 10 倍。

## Evidence

检索失败: no sources from any channel (all 5 failed)
