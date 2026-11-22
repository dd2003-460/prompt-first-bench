# N146: 计算冷对象在 LFU 中的滞留概率 p_cold_stick：p_cold_stick 取决于冷对象的访问间隔 T_cold 与 T_age 的比值。若 T_c

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N47

## Claim

计算冷对象在 LFU 中的滞留概率 p_cold_stick：p_cold_stick 取决于冷对象的访问间隔 T_cold 与 T_age 的比值。若 T_cold >> T_age，则 p_cold_stick ≈ 0（LFU 能有效清除）；若 T_cold < T_age，则 p_cold_stick ≈ 1。对于 Bottom 90% 对象，平均访问间隔 T_cold 极长（>100 days），故 p_cold_stick ≈ 0，这意味着 LFU 在稳态下对冷对象的滞留影响极小，D_LFU 退化主要源于热对象的频率估计误差而非冷对象滞留。

## Corrected Claim

计算冷对象在 LFU 中的滞留概率 p_cold_stick：p_cold_stick 取决于冷对象的访问间隔 T_cold 与 T_age 的比值。若 T_cold >> T_age，则 p_cold_stick ≈ 0（LFU 能有效清除）；若 T_cold < T_age，则 p_cold_stick ≈ 1。对于 Bottom 90% 对象，平均访问间隔 T_cold 极长（>100 days），故 p_cold_stick ≈ 0，这意味着 LFU 在稳态下对冷对象的滞留影响极小，D_LFU 退化主要源于热对象的频率估计误差而非冷对象滞留。

## Evidence

先验知识/题面给定，逻辑校验通过：LFU 机制基于访问频率，冷对象（访问间隔远大于老化时间）频率极低，必然被优先淘汰，滞留概率趋近于0，符合缓存替换算法的基本原理。
