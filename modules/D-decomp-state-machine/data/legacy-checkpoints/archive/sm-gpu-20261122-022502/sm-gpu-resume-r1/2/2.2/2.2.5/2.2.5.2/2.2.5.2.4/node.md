# N609: ROCm 故障修复时间 MTTR 的分布需基于 AMD 官方支持 SLA（通常为 48-72 小时）与社区补丁平均响应时间（约 1-2 周）的加权平均计算

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N186

## Claim

ROCm 故障修复时间 MTTR 的分布需基于 AMD 官方支持 SLA（通常为 48-72 小时）与社区补丁平均响应时间（约 1-2 周）的加权平均计算

## Corrected Claim

ROCm 故障修复时间 MTTR 的分布通常受 AMD 官方支持 SLA 和社区补丁响应时间共同影响，具体数值需根据支持等级和故障类型确定，而非简单的固定加权平均。

## Evidence

[质询]该陈述将MTTR定义为两个特定时间段的加权平均，缺乏理论或工程标准支持；且'48-72小时'和'1-2周'的具体数值属于经验事实，无来源佐证，可能因具体故障类型、支持等级（如白金/黄金）或社区活跃度而显著波动，简单加权平均可能无法反映真实分布。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）

## Search Query

AMD ROCm support SLA average patch response time
