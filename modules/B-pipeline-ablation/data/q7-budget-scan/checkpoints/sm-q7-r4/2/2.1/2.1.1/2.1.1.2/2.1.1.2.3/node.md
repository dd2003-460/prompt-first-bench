# N479: 基于占空比的年电力成本重构：年电力成本 C_power = (P_idle_total * 8760h + (P_active_total - P_idle_t

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N161

## Claim

基于占空比的年电力成本重构：年电力成本 C_power = (P_idle_total * 8760h + (P_active_total - P_idle_total) * T_busy_hours) * PUE * Unit_Price。其中 T_busy_hours 取决于温数据扫描频率与单次耗时，需结合N386的占空比33.3%计算，而非简单按满负荷或纯静态计算。

## Corrected Claim

基于占空比的年电力成本重构：年电力成本 C_power = (P_idle_total * 8760h + (P_active_total - P_idle_total) * T_busy_hours) * PUE * Unit_Price。其中 T_busy_hours 取决于温数据扫描频率与单次耗时，需结合N386的占空比33.3%计算，而非简单按满负荷或纯静态计算。

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构符合电力成本计算的基本物理定义（能量=功率×时间），且明确指出了需结合特定占空比（N386）进行动态计算，避免了静态估算的逻辑谬误。
