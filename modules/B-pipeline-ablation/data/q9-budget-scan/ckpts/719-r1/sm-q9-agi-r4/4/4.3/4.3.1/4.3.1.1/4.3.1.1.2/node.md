# N619: Alertmanager 规则评估周期（evaluation_interval）默认为 15s，产生的额外延迟遵循 U(0, 15s)，平均延迟 7.5s；若配

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N220

## Claim

Alertmanager 规则评估周期（evaluation_interval）默认为 15s，产生的额外延迟遵循 U(0, 15s)，平均延迟 7.5s；若配置为默认值，总检测延迟理论最小值为 0s（立即触发），最大值为 30s+15s+通知延迟

## Corrected Claim

Alertmanager 规则评估周期（evaluation_interval）默认为 15s，产生的额外延迟遵循 U(0, 15s)，平均延迟 7.5s；若配置为默认值，总检测延迟理论最小值为 0s（立即触发），最大值为 30s+15s+通知延迟

## Evidence

先验知识/题面给定，逻辑校验通过：Alertmanager 默认 evaluation_interval 为 15s，基于均匀分布 U(0, T) 的随机相位假设，平均等待时间为 T/2 = 7.5s，最大等待时间为 T = 15s，符合基本概率与系统调度逻辑。
