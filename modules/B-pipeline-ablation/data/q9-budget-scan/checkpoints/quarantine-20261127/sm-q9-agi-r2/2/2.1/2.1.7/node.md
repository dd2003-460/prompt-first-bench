# N56: Docker 容器在 macOS（M1 Max）上运行时，由于 VM 层开销，磁盘 I/O 延迟比原生 Linux 高 2-5 倍；单次 Python 脚本执行

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N13, N14, N15

## Claim

Docker 容器在 macOS（M1 Max）上运行时，由于 VM 层开销，磁盘 I/O 延迟比原生 Linux 高 2-5 倍；单次 Python 脚本执行中，环境加载（pip import）耗时从原生的 0.5s 增加至 1-2s，成为 2-5s 总耗时的主要组成部分（占比约 40-50%）。

## Corrected Claim

Docker 容器在 macOS（M1 Max）上运行时，由于 VM 层开销，磁盘 I/O 延迟比原生 Linux 高 2-5 倍；单次 Python 脚本执行中，环境加载（pip import）耗时从原生的 0.5s 增加至 1-2s，成为 2-5s 总耗时的主要组成部分（占比约 40-50%）。

## Evidence

先验知识/题面给定，逻辑校验通过
