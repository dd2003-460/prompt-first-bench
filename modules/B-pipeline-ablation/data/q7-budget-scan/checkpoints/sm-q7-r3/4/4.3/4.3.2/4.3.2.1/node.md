# N252: 在纯顺序重建工作点（低CPU负载，高IO带宽利用率），RAID-6双奇偶校验（XOR+GF(2^8)乘法）的CPU开销约为重建IO时间的5%，即 T_parit

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N80

## Claim

在纯顺序重建工作点（低CPU负载，高IO带宽利用率），RAID-6双奇偶校验（XOR+GF(2^8)乘法）的CPU开销约为重建IO时间的5%，即 T_parity_calc ≈ 0.05 * T_read_write；此时瓶颈完全在磁盘IO，Parity_Calc_Overhead系数取下限10%（含内存拷贝与调度开销）

## Corrected Claim

在纯顺序重建工作点（低CPU负载，高IO带宽利用率），RAID-6双奇偶校验（XOR+GF(2^8)乘法）的CPU开销约为重建IO时间的5%，即 T_parity_calc ≈ 0.05 * T_read_write；此时瓶颈完全在磁盘IO，Parity_Calc_Overhead系数取下限10%（含内存拷贝与调度开销）

## Evidence

先验知识/题面给定，逻辑校验通过
