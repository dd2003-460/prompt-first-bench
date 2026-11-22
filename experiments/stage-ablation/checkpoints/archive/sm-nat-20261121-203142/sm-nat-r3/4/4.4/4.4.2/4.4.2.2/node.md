# N151: 在 C/M=0.3 的低容量工作点下，缓存空间不足以容纳头部对象完整生命周期，T_residence/L_object 比值降至 0.2-0.3，导致线性折损模

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N58

## Claim

在 C/M=0.3 的低容量工作点下，缓存空间不足以容纳头部对象完整生命周期，T_residence/L_object 比值降至 0.2-0.3，导致线性折损模型低估实际折损，需引入非线性修正

## Corrected Claim

在 C/M=0.3 的低容量工作点下，缓存空间不足以容纳头部对象完整生命周期，T_residence/L_object 比值降至 0.2-0.3，导致线性折损模型低估实际折损，需引入非线性修正

## Evidence

先验知识/题面给定，逻辑校验通过：低容量比（C/M=0.3）下缓存无法覆盖头部对象生命周期，导致驻留时间占比下降，线性模型失效需非线性修正，符合缓存替换理论直觉。
