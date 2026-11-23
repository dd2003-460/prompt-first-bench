# N33: 边缘缓存命中率 $H$ 对 P99 延迟的影响遵循非线性关系：当 $H < 90\%$ 时，P99 延迟主要受回源链路 $L_{backhaul}$ 主导；当 

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

边缘缓存命中率 $H$ 对 P99 延迟的影响遵循非线性关系：当 $H < 90\%$ 时，P99 延迟主要受回源链路 $L_{backhaul}$ 主导；当 $H > 95\%$ 时，P99 延迟收敛至边缘节点处理延迟 $L_{edge}$（约 5-10ms），此时增加缓存容量对延迟改善边际递减。

## Corrected Claim

边缘缓存命中率 $H$ 对 P99 延迟的影响遵循非线性关系：当 $H < 90\%$ 时，P99 延迟主要受回源链路 $L_{backhaul}$ 主导；当 $H > 95\%$ 时，P99 延迟收敛至边缘节点处理延迟 $L_{edge}$（约 5-10ms），此时增加缓存容量对延迟改善边际递减。

## Evidence

检索失败: no sources from any channel (all 5 failed)
