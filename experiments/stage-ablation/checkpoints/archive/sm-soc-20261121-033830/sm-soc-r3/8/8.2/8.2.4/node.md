# N325: v_baseline 的标准化窗口敏感性：若 v_baseline 采用近 30 天均值，则 v 的波动范围通常为 [-0.5, 0.5]；若采用近 7 天均值

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N104, N105, N106

## Claim

v_baseline 的标准化窗口敏感性：若 v_baseline 采用近 30 天均值，则 v 的波动范围通常为 [-0.5, 0.5]；若采用近 7 天均值，波动范围扩大至 [-0.8, 0.8]，导致 0.3v 项的方差增加 2.56 倍，进而影响系数 0.3 的标准误和显著性水平

## Corrected Claim

v_baseline 的标准化窗口敏感性：若 v_baseline 采用近 30 天均值，则 v 的波动范围通常为 [-0.5, 0.5]；若采用近 7 天均值，波动范围扩大至 [-0.8, 0.8]，导致 0.3v 项的方差增加 2.56 倍，进而影响系数 0.3 的标准误和显著性水平

## Evidence

先验知识/题面给定，逻辑校验通过：方差增加倍数 (0.8/0.5)^2 = 2.56，数学推导自洽
