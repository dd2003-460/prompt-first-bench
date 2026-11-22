# N49: 投影2：新鲜度权重 $w_{freshness}$ 的最小调整量 $\Delta w_{freshness}^{min}$ 计算式：$\Delta w_{fre

- **status**: pending
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N14, N15, N16

## Claim

投影2：新鲜度权重 $w_{freshness}$ 的最小调整量 $\Delta w_{freshness}^{min}$ 计算式：$\Delta w_{freshness}^{min} = \frac{\Delta T_{cycle}^{target} - \Delta T_{cycle}^{old}}{\partial T_{cycle} / \partial w_{freshness}}$，其中 $\partial T_{cycle} / \partial w_{freshness}$ 为成交周期对新鲜度权重的偏导数，需基于时间序列数据分析

## Corrected Claim

投影2：新鲜度权重 $w_{freshness}$ 的最小调整量 $\Delta w_{freshness}^{min}$ 计算式：$\Delta w_{freshness}^{min} = \frac{\Delta T_{cycle}^{target} - \Delta T_{cycle}^{old}}{\partial T_{cycle} / \partial w_{freshness}}$，其中 $\partial T_{cycle} / \partial w_{freshness}$ 为成交周期对新鲜度权重的偏导数，需基于时间序列数据分析

## Evidence

父节点级核验失败（LLM 错误）：Invalid \escape: line 5 column 61 (char 126)

## Search Query

transaction cycle time sensitivity to freshness weight time series analysis
