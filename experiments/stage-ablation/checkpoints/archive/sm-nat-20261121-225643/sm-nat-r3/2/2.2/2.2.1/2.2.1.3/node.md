# N74: LFU 对 top 10% 对象的锁定率 L_LFU_top10 的推导：LFU 通过频率计数器锁定高频对象，其锁定率取决于频率衰减窗口 T_window 与对

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N26

## Claim

LFU 对 top 10% 对象的锁定率 L_LFU_top10 的推导：LFU 通过频率计数器锁定高频对象，其锁定率取决于频率衰减窗口 T_window 与对象访问间隔的比值；在稳态下，L_LFU_top10 ≈ 1 - exp(-λ_top * T_window)，需确定 λ_top（头部对象平均访问率）以验证 0.75 的数值。

## Corrected Claim

LFU 对 top 10% 对象的锁定率 L_LFU_top10 的推导：LFU 通过频率计数器锁定高频对象，其锁定率取决于频率衰减窗口 T_window 与对象访问间隔的比值；在稳态下，L_LFU_top10 ≈ 1 - exp(-λ_top * T_window)，需确定 λ_top（头部对象平均访问率）以验证 0.75 的数值。

## Evidence

先验知识/题面给定，逻辑校验通过：该公式符合泊松过程下事件发生概率的数学推导（1 - exp(-λt)），量纲与逻辑自洽。
