# N189: 目标函数对高价低周转商品的惩罚阈值：当 TTS_i 超过 T_baseline 的 1/ (GMV_i/P_median) 倍时（如 2倍价格需 TTS < 0

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N59

## Claim

目标函数对高价低周转商品的惩罚阈值：当 TTS_i 超过 T_baseline 的 1/ (GMV_i/P_median) 倍时（如 2倍价格需 TTS < 0.5*T_baseline），该商品在算法排序中的得分将低于基准商品，触发降权。

## Corrected Claim

目标函数对高价低周转商品的惩罚阈值：当 TTS_i 超过 T_baseline 的 1/ (GMV_i/P_median) 倍时（如 2倍价格需 TTS < 0.5*T_baseline），该商品在算法排序中的得分将低于基准商品，触发降权。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 TTS_i > T_baseline / (GMV_i/P_median) 在 GMV_i/P_median=2 时推导为 TTS_i > 0.5*T_baseline，与示例一致，量纲与逻辑自洽。
