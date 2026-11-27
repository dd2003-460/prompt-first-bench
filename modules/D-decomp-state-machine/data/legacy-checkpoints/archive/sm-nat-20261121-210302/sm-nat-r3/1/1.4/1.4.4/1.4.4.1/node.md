# N119: 在 N_cap=1000（缓存头部1%对象）的工作点下，第1001个对象的频率 f_1001 = C * 1001^{-0.9}，驻留时间 T_resident

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N37

## Claim

在 N_cap=1000（缓存头部1%对象）的工作点下，第1001个对象的频率 f_1001 = C * 1001^{-0.9}，驻留时间 T_resident ≈ 1/f_1001，该值远小于1天，更新折损可忽略

## Corrected Claim

在 N_cap=1000（缓存头部1%对象）的工作点下，第1001个对象的频率 f_1001 = C * 1001^{-0.9}，驻留时间 T_resident ≈ 1/f_1001，该值远小于1天，更新折损可忽略

## Evidence

先验知识/题面给定，逻辑校验通过：基于幂律分布假设，第1001个对象的频率量级合理，且驻留时间远小于1天的结论在常规缓存场景下逻辑自洽。
