# N55: RTO目标值的敏感性边界：若温数据RTO从4h收紧至1h，NVMe阵列优势扩大（恢复时间从~1h降至~15min），HDD分层方案因恢复时间>1h而被过滤；若R

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N22

## Claim

RTO目标值的敏感性边界：若温数据RTO从4h收紧至1h，NVMe阵列优势扩大（恢复时间从~1h降至~15min），HDD分层方案因恢复时间>1h而被过滤；若RTO放宽至8h，HDD分层方案恢复时间~5h仍在可接受范围，成本优势（硬件成本低¥200,000）可能抵消RTO风险成本

## Corrected Claim

RTO目标值的敏感性边界：若温数据RTO从4h收紧至1h，NVMe阵列优势扩大（恢复时间从~1h降至~15min），HDD分层方案因恢复时间>1h而被过滤；若RTO放宽至8h，HDD分层方案恢复时间~5h仍在可接受范围，成本优势（硬件成本低¥200,000）可能抵消RTO风险成本

## Evidence

先验知识/题面给定，逻辑校验通过：NVMe恢复速度显著快于HDD，RTO收紧时NVMe优势扩大符合物理直觉；RTO放宽时HDD成本优势抵消风险符合经济逻辑，数值量级合理。
