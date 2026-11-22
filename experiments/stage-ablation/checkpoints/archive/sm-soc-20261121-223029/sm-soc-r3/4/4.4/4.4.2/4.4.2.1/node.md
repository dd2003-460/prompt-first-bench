# N260: 周期缩短幅度 T_pre/T_post 的敏感性分析：若 T_post = 0.8 * T_pre，则 Q_unit_time 提升 25%；若 T_post 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N87

## Claim

周期缩短幅度 T_pre/T_post 的敏感性分析：若 T_post = 0.8 * T_pre，则 Q_unit_time 提升 25%；若 T_post = 0.6 * T_pre，则提升 67%。需确定 T_post/T_pre 的合理区间（如 0.6-0.8）以评估 ΔP 的波动范围。

## Corrected Claim

周期缩短幅度 T_pre/T_post 的敏感性分析：若 T_post = 0.8 * T_pre，则 Q_unit_time 提升 25%；若 T_post = 0.6 * T_pre，则提升 67%。需确定 T_post/T_pre 的合理区间（如 0.6-0.8）以评估 ΔP 的波动范围。

## Evidence

先验知识/题面给定，逻辑校验通过：Q_unit_time 与周期 T 成反比，T_post=0.8*T_pre 时 Q 变为 1/0.8=1.25 倍（提升 25%），T_post=0.6*T_pre 时 Q 变为 1/0.6≈1.67 倍（提升 67%），数值计算准确且逻辑自洽。
