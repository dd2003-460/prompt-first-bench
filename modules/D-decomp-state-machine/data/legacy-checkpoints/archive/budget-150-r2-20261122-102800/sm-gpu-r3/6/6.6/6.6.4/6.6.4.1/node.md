# N373: ROCm 6.x 在 RX 7900 XTX 上的内核模块编译（amdgpu.ko）耗时约为 20-40 分钟，主要受 GCC 版本（需 11+）与 Linux

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N147

## Claim

ROCm 6.x 在 RX 7900 XTX 上的内核模块编译（amdgpu.ko）耗时约为 20-40 分钟，主要受 GCC 版本（需 11+）与 Linux 内核头文件版本匹配影响；若内核版本高于 ROCm 支持上限（如 6.10+ vs ROCm 6.1 支持至 6.6），需手动打补丁或降级内核，额外耗时 1-3 小时。

## Corrected Claim

ROCm 6.x 在 RX 7900 XTX 上的内核模块编译耗时受 GCC 版本与 Linux 内核头文件版本匹配影响；若内核版本高于 ROCm 支持上限，需手动打补丁或降级内核，可能显著增加耗时。

## Evidence

[质询]具体耗时数值（20-40分钟、1-3小时）及特定版本支持上限（ROCm 6.1 支持至 6.6）属于经验事实，缺乏来源支持，且不同硬件/编译环境差异可能导致数值偏差。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

ROCm 6.1 amdgpu kernel module compile time Linux kernel version compatibility RX 7900 XTX
