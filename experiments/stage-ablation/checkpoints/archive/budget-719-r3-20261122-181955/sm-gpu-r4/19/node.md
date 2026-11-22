# N404: 性价比评估指标需定义 '有效吞吐量成本比' (Cost per Effective Token)，公式为 $Cost_{TCO} / (Throughput_{

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

性价比评估指标需定义 '有效吞吐量成本比' (Cost per Effective Token)，公式为 $Cost_{TCO} / (Throughput_{theory} \times \eta_{impl} \times Quality_{factor})$，其中 Quality_factor 为量化后的相对精度得分 (如 MMLU 得分 / BF16 基线得分)，该指标将精度损失直接量化为性能折扣，避免单纯比较吞吐量而忽略质量降级。

## Corrected Claim

性价比评估指标需定义 '有效吞吐量成本比' (Cost per Effective Token)，公式为 $Cost_{TCO} / (Throughput_{theory} \times \eta_{impl} \times Quality_{factor})$，其中 Quality_factor 为量化后的相对精度得分 (如 MMLU 得分 / BF16 基线得分)，该指标将精度损失直接量化为性能折扣，避免单纯比较吞吐量而忽略质量降级。

## Evidence

检索失败: no sources from any channel (all 5 failed)
