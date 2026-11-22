# N208: 量化校准数据（Calibration Data）在推理阶段的显存占用：校准数据（如 128 条样本）仅在量化生成阶段（Offline Quantization）

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N54, N56, N57

## Claim

量化校准数据（Calibration Data）在推理阶段的显存占用：校准数据（如 128 条样本）仅在量化生成阶段（Offline Quantization）使用，用于计算 Scale 和 Zero Point。在推理阶段（Inference），校准数据**不驻留**显存，其显存占用为 $0$GB。因此，N56 中提到的 'Calibration Data 额外占用' 在推理 TCO 计算中应修正为 0，仅保留 Scale/Zero Point 的开销。

## Corrected Claim

量化校准数据（Calibration Data）在推理阶段的显存占用：校准数据（如 128 条样本）仅在量化生成阶段（Offline Quantization）使用，用于计算 Scale 和 Zero Point。在推理阶段（Inference），校准数据**不驻留**显存，其显存占用为 $0$GB。因此，N56 中提到的 'Calibration Data 额外占用' 在推理 TCO 计算中应修正为 0，仅保留 Scale/Zero Point 的开销。

## Evidence

先验知识/题面给定，逻辑校验通过：量化校准数据仅用于离线计算Scale/ZeroPoint，推理阶段不加载，显存占用为0符合技术原理。
