# N290: NVIDIA H100 SXM 在 LLM 推理负载下的实测带宽利用率 (η_H100)：引用 NVIDIA 官方白皮书或 MLPerf 数据，H100 SXM

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N93

## Claim

NVIDIA H100 SXM 在 LLM 推理负载下的实测带宽利用率 (η_H100)：引用 NVIDIA 官方白皮书或 MLPerf 数据，H100 SXM 理论带宽 3.35 TB/s，实测有效带宽通常在 2.8-3.1 TB/s 之间，利用率约 85-92%。

## Corrected Claim

NVIDIA H100 SXM 理论带宽为 3.35 TB/s。在 LLM 推理负载下，实测有效带宽利用率通常较高，但具体数值（如 85-92%）取决于具体模型、Batch Size 及实现优化，需参考特定基准测试数据。

## Evidence

[质询]该陈述属于经验事实（硬件实测性能数据），且声称引用了特定来源（NVIDIA白皮书或MLPerf），但当前检索无可用来源支持，无法验证具体数值区间（2.8-3.1 TB/s）和利用率（85-92%）的准确性。此外，LLM推理负载下的带宽利用率受模型架构、Batch Size、量化方式等影响极大，给出一个固定的窄区间可能过于简化，存在口径混淆的风险。 | 经验事实，逻辑自洽（3.35 TB/s理论带宽下，85-92%利用率对应2.85-3.09 TB/s，数值量级合理），但缺来源支持。

## Search Query

NVIDIA H100 SXM effective memory bandwidth MLPerf inference
