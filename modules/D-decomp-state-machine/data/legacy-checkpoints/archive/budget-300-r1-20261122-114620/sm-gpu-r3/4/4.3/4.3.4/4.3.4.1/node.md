# N343: 在 batch_size=1 的本地推理场景下，PCIe 双卡方案的吞吐损失主要来自 Decode 阶段的通信等待，实际吞吐损失百分比约为 50-70% (而非

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N111

## Claim

在 batch_size=1 的本地推理场景下，PCIe 双卡方案的吞吐损失主要来自 Decode 阶段的通信等待，实际吞吐损失百分比约为 50-70% (而非 15-30%)，因为 Decode 阶段计算时间极短而通信时间固定，需修正 η_comm 对吞吐的影响模型

## Corrected Claim

在 batch_size=1 的本地推理场景下，PCIe 双卡方案的吞吐损失主要来自 Decode 阶段的通信等待，实际吞吐损失显著高于 Prefill 阶段（通常远超 15-30%），需修正 η_comm 对吞吐的影响模型以反映通信延迟主导的特性。

## Evidence

[质询]具体数值区间（50-70%）缺乏通用性，高度依赖于模型大小、PCIe带宽版本及具体硬件配置，将其作为固定事实陈述存在过度泛化风险。 | 先验知识/题面给定，逻辑校验通过：在batch_size=1的Decode阶段，计算量极小，通信延迟占比确实显著高于Prefill阶段，导致吞吐损失大幅上升，逻辑自洽；但具体百分比为经验估计，无来源直接支持，故降级。
