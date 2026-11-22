# N150: 工作点3（中性-基准）：在 $D \in [0, 5\%]$ 的基准组内部，$\Delta T_{short}$ 应趋近于 0 且方差最小。具体量化：若基准组内

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N62

## Claim

工作点3（中性-基准）：在 $D \in [0, 5\%]$ 的基准组内部，$\Delta T_{short}$ 应趋近于 0 且方差最小。具体量化：若基准组内部分层（$D=0\%$ vs $D=5\%$），其成交时间差异 $\Delta T_{neutral} < 1$ 天，且 $CV(\Delta T_{neutral}) < 0.1$。此工作点用于验证测量误差的下限：若基准组内部波动已接近 1 天，则任何 $|\Delta T_{short}| < 1$ 天的差异均视为统计不显著，不应解读为信号效应。

## Corrected Claim

工作点3（中性-基准）：在 $D \in [0, 5\%]$ 的基准组内部，$\Delta T_{short}$ 应趋近于 0 且方差最小。具体量化：若基准组内部分层（$D=0\%$ vs $D=5\%$），其成交时间差异 $\Delta T_{neutral} < 1$ 天，且 $CV(\Delta T_{neutral}) < 0.1$。此工作点用于验证测量误差的下限：若基准组内部波动已接近 1 天，则任何 $|\Delta T_{short}| < 1$ 天的差异均视为统计不显著，不应解读为信号效应。

## Evidence

先验知识/题面给定，逻辑校验通过：该陈述定义了基准组（D∈[0,5%]）的统计特性（趋近于0且方差最小），并基于此设定了测量误差下限（1天）作为显著性阈值，逻辑自洽且符合实验设计常识。

## Search Query

baseline sale time variability control group second hand market statistical noise
