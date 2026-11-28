# N100: INT4 AWQ 敏感性分析：AWQ (Activation-aware Weight Quantization) 通过保护对激活值影响最大的 1% 权重来减少

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N28

## Claim

INT4 AWQ 敏感性分析：AWQ (Activation-aware Weight Quantization) 通过保护对激活值影响最大的 1% 权重来减少量化误差。然而，对于 Qwen3-27B 这类参数量大的模型，剩余 99% 权重的舍入误差累积导致 ΔPPL 达到 0.1-0.3。具体数值依赖于校准数据集 (Calibration Set) 的代表性；若校准集未覆盖代码或数学领域，ΔPPL 可能高达 0.5。

## Corrected Claim

INT4 AWQ 通过保护对激活值影响最大的约 1% 权重来减少量化误差。对于大模型，剩余权重的舍入误差累积会导致 PPL 上升，具体幅度取决于校准数据集的代表性；若校准集未覆盖特定领域（如代码/数学），PPL 退化可能更为显著。

## Evidence

[质询]具体数值（ΔPPL 0.1-0.3 及 0.5）缺乏通用基准支持，不同校准集和实现细节下波动较大，属于特定实验条件下的经验数据而非普适常数。 | 先验知识/题面给定，逻辑校验通过；但具体数值为经验事实，无来源直接支持，故降级。

## Search Query

AWQ quantization sensitivity calibration set perplexity degradation large language model
