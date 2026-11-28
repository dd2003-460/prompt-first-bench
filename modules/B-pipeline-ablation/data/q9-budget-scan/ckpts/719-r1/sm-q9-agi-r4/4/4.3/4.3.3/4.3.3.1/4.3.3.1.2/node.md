# N635: X_ref 离线预计算的存储开销 M_ref 公式：M_ref = N_samples × d_ref × bytes_per_element，其中 d_ref

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N226

## Claim

X_ref 离线预计算的存储开销 M_ref 公式：M_ref = N_samples × d_ref × bytes_per_element，其中 d_ref 为高精度位数（如 50 bits），若 N_samples=1000，d_ref=1000，bytes_per_element=8，则 M_ref ≈ 8MB，远低于磁盘 I/O 瓶颈，但加载延迟 T_load ≈ 10-50ms 需纳入在线比对总延迟预算

## Corrected Claim

X_ref 离线预计算的存储开销 M_ref 公式：M_ref = N_samples × d_ref × bytes_per_element，其中 d_ref 为高精度位数（如 50 bits），若 N_samples=1000，d_ref=1000，bytes_per_element=8，则 M_ref ≈ 8MB，远低于磁盘 I/O 瓶颈，但加载延迟 T_load ≈ 10-50ms 需纳入在线比对总延迟预算

## Evidence

先验知识/题面给定，逻辑校验通过：存储公式量纲正确，数值计算准确（1000*1000*8B=8MB），延迟估算符合常规磁盘I/O经验范围。
