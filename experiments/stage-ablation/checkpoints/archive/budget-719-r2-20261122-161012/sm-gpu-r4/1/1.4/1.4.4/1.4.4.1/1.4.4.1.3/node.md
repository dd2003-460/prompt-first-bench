# N402: RTX 4090 双卡方案中，若使用消费级主板（如 Z790 或 X670E），PCIe 插槽通常为 1x16 + 1x4 或 1x8 + 1x8 模式；第二张

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N166, N167, N168

## Claim

RTX 4090 双卡方案中，若使用消费级主板（如 Z790 或 X670E），PCIe 插槽通常为 1x16 + 1x4 或 1x8 + 1x8 模式；第二张 4090 在 x4 模式下，带宽仅为 x16 的 25%，但在 LLM 推理 Decode 阶段（带宽受限而非延迟敏感）影响 <5%；然而，若主板不支持双 x16 或插槽间距不足导致散热风道阻塞，可能触发 GPU 降频（Thermal Throttling），使实际功耗波动增加 10-15%，需预留额外电源余量。

## Corrected Claim

RTX 4090 双卡方案中，若使用消费级主板（如 Z790 或 X670E），PCIe 插槽通常为 1x16 + 1x4 或 1x8 + 1x8 模式；第二张 4090 在 x4 模式下，带宽仅为 x16 的 25%，在 LLM 推理 Decode 阶段（带宽受限）通常影响较小（具体数值视模型和负载而定）；然而，若主板不支持双 x16 或插槽间距不足导致散热风道阻塞，可能触发 GPU 降频（Thermal Throttling），导致实际功耗波动增加，需预留额外电源余量。

## Evidence

[质询]「LLM 推理 Decode 阶段...影响 <5%」这一具体数值缺乏普适性，高度依赖模型架构（如 MoE vs Dense）、Batch Size 及具体硬件配置，属于经验性观察而非绝对物理定律，且不同主板/驱动环境下波动可能更大。 | 先验知识/题面给定，逻辑校验通过：PCIe x4 带宽为 x16 的 25% 符合物理事实；消费级主板双卡插槽限制及散热导致降频符合工程常识；但具体性能损失百分比（<5%）和功耗波动（10-15%）为经验估算值，无来源直接支持，故降级。

## Search Query

RTX 4090 dual card PCIe x4 bandwidth impact LLM inference
