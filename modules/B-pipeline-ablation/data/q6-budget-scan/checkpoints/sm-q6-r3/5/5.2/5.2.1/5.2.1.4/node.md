# N238: 基准存储成本 C_base 的构成：C_base = C_storage_hw * (S_base / S_total) + C_storage_bw * (R

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N75, N76, N77

## Claim

基准存储成本 C_base 的构成：C_base = C_storage_hw * (S_base / S_total) + C_storage_bw * (R_base / R_total)，其中 S_base 为基准TTL下的缓存占用空间，S_total 为单POP总存储容量（76.8TB），R_base 为基准TTL下的缓存读取带宽，R_total 为单POP总带宽（10Gbps）

## Corrected Claim

基准存储成本 C_base 的构成：C_base = C_storage_hw * (S_base / S_total) + C_storage_bw * (R_base / R_total)，其中 S_base 为基准TTL下的缓存占用空间，S_total 为单POP总存储容量（76.8TB），R_base 为基准TTL下的缓存读取带宽，R_total 为单POP总带宽（10Gbps）

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构符合存储成本按资源占比分摊的线性模型，量纲一致（空间占比与带宽占比分别对应硬件与带宽成本），数值量级合理。
