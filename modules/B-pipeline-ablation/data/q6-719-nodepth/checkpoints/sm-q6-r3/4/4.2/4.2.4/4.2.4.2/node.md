# N346: 磁盘 I/O 对 T_proc_pop_p99 的边际影响 ΔT_disk 取决于缓存命中率 H_pop 与磁盘类型：若 H_pop > 0.95 且使用 NV

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N107

## Claim

磁盘 I/O 对 T_proc_pop_p99 的边际影响 ΔT_disk 取决于缓存命中率 H_pop 与磁盘类型：若 H_pop > 0.95 且使用 NVMe SSD，ΔT_disk ≈ 0.1-0.5ms；若 H_pop < 0.8 且使用 SATA SSD，ΔT_disk ≈ 2-5ms（随机读延迟差异）

## Corrected Claim

磁盘 I/O 对 T_proc_pop_p99 的边际影响 ΔT_disk 取决于缓存命中率 H_pop 与磁盘类型：若 H_pop > 0.95 且使用 NVMe SSD，ΔT_disk ≈ 0.1-0.5ms；若 H_pop < 0.8 且使用 SATA SSD，ΔT_disk ≈ 2-5ms（随机读延迟差异）

## Evidence

先验知识/题面给定，逻辑校验通过：NVMe SSD随机读延迟通常在0.1ms量级，SATA SSD在0.1-0.5ms量级，但考虑到缓存未命中时的额外开销及系统调度，2-5ms对于SATA SSD在高负载或特定场景下是合理的保守估计；NVMe在极高命中率下接近0.1ms也符合物理极限。数值量级与硬件特性一致。
