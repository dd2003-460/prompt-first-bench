# N600: 温数据每日扫描 2 次，原始读取量 V_read = 100TB * 2 = 200TB/天，合并后实际网络传输量 V_trans = V_read * A_i

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N212

## Claim

温数据每日扫描 2 次，原始读取量 V_read = 100TB * 2 = 200TB/天，合并后实际网络传输量 V_trans = V_read * A_io = 1600TB/天

## Corrected Claim

温数据每日扫描 2 次，原始读取量 V_read = 100TB * 2 = 200TB/天，合并后实际网络传输量 V_trans = V_read * A_io = 1600TB/天

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算 100*2=200 及 200*8=1600 正确，符合温数据扫描与IO放大系数的常规定义。
