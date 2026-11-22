# N641: 法律/医疗咨询场景下的质量损失阈值修正：若应用场景为法律/医疗咨询，PPL 阈值收紧至 <0.2 的同时，需引入 Factuality Score (基于 RA

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N264

## Claim

法律/医疗咨询场景下的质量损失阈值修正：若应用场景为法律/医疗咨询，PPL 阈值收紧至 <0.2 的同时，需引入 Factuality Score (基于 RAGAS 或 TruLens 框架)；BF16 的 Factuality Score 通常为 0.95+，FP8 可能降至 0.93-0.94，INT4 可能降至 0.85-0.90；若 Factuality Score < 0.92，则判定为不可接受，需强制使用 BF16。

## Corrected Claim

在法律/医疗咨询场景下，若PPL阈值收紧至<0.2，建议引入Factuality Score进行监控。通常量化精度降低（如从BF16降至INT4）会导致Factuality Score下降（例如从0.95+降至0.85-0.90区间）。若Factuality Score低于设定阈值（如0.92），应判定为不可接受并强制使用更高精度（如BF16）。

## Evidence

[质询]具体数值（如BF16 0.95+, FP8 0.93-0.94, INT4 0.85-0.90）及阈值（0.92）属于特定模型、数据集和评估框架下的经验统计结果，并非普适的物理或数学定律，不同模型和场景下波动较大，直接断言为固定区间存在过度泛化风险。 | 先验知识/题面给定，逻辑校验通过（量化精度降低通常导致事实性得分下降，量级合理），但具体数值为经验事实，缺乏通用性保证，故降级。

## Search Query

legal medical LLM factuality score quantization BF16 FP8
