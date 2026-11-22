# N57: 128GB 保留对象的访问概率覆盖率 Prob_Coverage_128 = [∫_{0}^{R_128} r · f_R(r) dr] / E[R]，其中 R

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N14

## Claim

128GB 保留对象的访问概率覆盖率 Prob_Coverage_128 = [∫_{0}^{R_128} r · f_R(r) dr] / E[R]，其中 R_128 为热度截断点，需通过大小-热度负相关 ρ=-0.3 映射 S_128 到 R_128

## Corrected Claim

128GB 保留对象的访问概率覆盖率 Prob_Coverage_128 = [∫_{0}^{R_128} r · f_R(r) dr] / E[R]，其中 R_128 为热度截断点，需通过大小-热度负相关 ρ=-0.3 映射 S_128 到 R_128

## Evidence

先验知识/题面给定，逻辑校验通过：公式定义符合概率密度函数积分求期望覆盖率的数学逻辑，量纲一致，且大小-热度负相关映射在缓存/存储系统建模中是合理的经验假设。
