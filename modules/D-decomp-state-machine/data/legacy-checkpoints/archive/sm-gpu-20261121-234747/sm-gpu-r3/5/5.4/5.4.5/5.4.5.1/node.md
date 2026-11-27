# N386: PCIe 4.0 x16互联的NCCL All-Reduce实测带宽：在2×RTX 3090配置下，NCCL All-Reduce的实测带宽约为24.5 GB/

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N130

## Claim

PCIe 4.0 x16互联的NCCL All-Reduce实测带宽：在2×RTX 3090配置下，NCCL All-Reduce的实测带宽约为24.5 GB/s（理论峰值32 GB/s的76.6%） [待核验：需基于nccl-tests实测数据]

## Corrected Claim

在2×RTX 3090配置下，PCIe 4.0 x16互联的NCCL All-Reduce实测带宽通常在20-26 GB/s范围内（约为理论峰值32 GB/s的60%-80%），具体数值取决于驱动版本和系统配置。

## Evidence

[质询]该陈述包含具体的硬件性能实测数据（24.5 GB/s），属于经验事实。虽然24.5 GB/s相对于32 GB/s理论峰值的76.6%效率在PCIe 4.0 x16链路下是合理且常见的量级（通常效率在70%-85%之间），但缺乏具体的实测来源支持，无法排除特定驱动版本、拓扑结构或测试方法导致的数值偏差。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

nccl-tests all-reduce bandwidth PCIe 4.0 2x RTX 3090
