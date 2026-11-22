# N256: NVIDIA H100 数据中心 GPU 在本地物理机部署时的软件许可成本为 $0，因其 EULA 明确允许本地推理使用；但需注意 H100 驱动包中可能包含针

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N76

## Claim

NVIDIA H100 数据中心 GPU 在本地物理机部署时的软件许可成本为 $0，因其 EULA 明确允许本地推理使用；但需注意 H100 驱动包中可能包含针对云环境的遥测组件，本地部署时需手动禁用以符合数据隐私合规要求，此合规配置工时约为 2 小时（一次性）。

## Corrected Claim

NVIDIA H100 数据中心 GPU 在本地物理机部署时的软件许可成本为 $0，因其 EULA 明确允许本地推理使用；关于驱动遥测组件及合规配置工时的具体描述缺乏公开证据支持，建议以实际部署环境的安全审计结果为准。

## Evidence

[质询]声称H100驱动包中“可能包含针对云环境的遥测组件”且需“手动禁用”以符合合规，这一具体技术细节缺乏公开文档支持，且NVIDIA标准驱动通常不包含此类需用户手动禁用的云特定遥测功能，存在过度推测或混淆了特定云厂商定制驱动与标准本地部署驱动的风险。 | source=knowledge，逻辑自洽但缺乏来源直接支持具体遥测组件及2小时工时这一经验性细节，依据经验事实排除条款降级。

## Search Query

NVIDIA H100 EULA local inference license cost telemetry disable
