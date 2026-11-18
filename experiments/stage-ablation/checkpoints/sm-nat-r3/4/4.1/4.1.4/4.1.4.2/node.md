# N136: 工作点 B 中 R_inv_B 的精确值计算：T_B = D_B / f_B，其中 D_B 为热度 1%-10% 对象在 LRU 栈中的平均深度，f_B 为其平

- **status**: failed
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N57

## Claim

工作点 B 中 R_inv_B 的精确值计算：T_B = D_B / f_B，其中 D_B 为热度 1%-10% 对象在 LRU 栈中的平均深度，f_B 为其平均访问频率；若 D_B ≈ 5000（假设），f_B ≈ 0.3 * 5e7 / 9000 ≈ 1667/s，则 T_B ≈ 5000 / (1667 * 86400) ≈ 3.46e-6 天，R_inv_B ≈ 0.01 * 3.46e-6 = 3.46e-8，远小于 N57 中的 6.7e-9，需修正计算逻辑。

## Corrected Claim

工作点 B 中 R_inv_B 的计算存在错误。若 D_B ≈ 5000, f_B ≈ 1667/s，则平均驻留时间 T_B ≈ 5000/1667 ≈ 3 秒。若 R_inv_B 定义为热度占比乘以归一化时间或其他指标，需重新定义公式。原陈述中“远小于 6.7e-9”的结论与计算值 3.46e-8 矛盾，且单位使用错误。

## Evidence

[质询]陈述内部存在严重的逻辑矛盾和数值错误：1. 计算出的 R_inv_B (3.46e-8) 实际上大于 N57 中的 6.7e-9，但陈述却声称“远小于”；2. 量纲分析错误，T_B 计算结果单位应为秒（s），而非天（days），导致后续 R_inv_B 的量级和物理意义完全错误。 | 逻辑校验失败：数值比较方向错误（3.46e-8 > 6.7e-9）且时间单位换算错误（5000/1667 ≈ 3s，而非 3.46e-6 天）。

## Search Query

LRU residency time stack depth frequency calculation
