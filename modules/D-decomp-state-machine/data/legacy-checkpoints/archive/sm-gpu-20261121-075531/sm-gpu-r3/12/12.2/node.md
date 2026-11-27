# N375: RTX 5090 在 27B INT8 推理满载状态下的实际功耗 (P_active_5090) 受 TDP 限制为 575W，但实际推理负载通常仅占用 80-

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N127

## Claim

RTX 5090 在 27B INT8 推理满载状态下的实际功耗 (P_active_5090) 受 TDP 限制为 575W，但实际推理负载通常仅占用 80-90% TDP，即约 460-518W，用于计算 P_avg 的 Active 分量。

## Corrected Claim

RTX 5090 在 27B INT8 推理满载状态下的实际功耗 (P_active_5090) 受 TDP 限制为 575W，但实际推理负载通常仅占用 80-90% TDP，即约 460-518W，用于计算 P_avg 的 Active 分量。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 5090 TDP 575W 符合 NVIDIA 官方规格，80-90% 负载占比符合 GPU 推理功耗特性，数值计算（460-518W）准确。
