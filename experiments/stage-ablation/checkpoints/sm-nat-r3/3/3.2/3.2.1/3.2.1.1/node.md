# N178: 在 LFU 策略下，保留对象集合 S_LFU 的字节加权未命中损失项 L_LFU = Σ_{i∉S_LFU} p_i s_i 的计算，需基于频率阈值 f_thr

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N62

## Claim

在 LFU 策略下，保留对象集合 S_LFU 的字节加权未命中损失项 L_LFU = Σ_{i∉S_LFU} p_i s_i 的计算，需基于频率阈值 f_threshold 确定 S_LFU 边界，并量化因频率统计窗口滞后导致的长尾对象误保留比例。

## Corrected Claim

在 LFU 策略下，保留对象集合 S_LFU 的字节加权未命中损失项 L_LFU = Σ_{i∉S_LFU} p_i s_i 的计算，需基于频率阈值 f_threshold 确定 S_LFU 边界，并量化因频率统计窗口滞后导致的长尾对象误保留比例。

## Evidence

先验知识/题面给定，逻辑校验通过
