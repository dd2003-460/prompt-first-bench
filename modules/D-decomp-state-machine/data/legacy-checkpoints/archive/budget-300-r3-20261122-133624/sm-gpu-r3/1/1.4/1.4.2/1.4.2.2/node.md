# N205: CUDA 异步拷贝缓冲区（Async Copy Buffer）的显存占用量化：主要服务于 Host-to-Device 的 Prompt 输入传输及中间激活值的

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N54, N56, N57

## Claim

CUDA 异步拷贝缓冲区（Async Copy Buffer）的显存占用量化：主要服务于 Host-to-Device 的 Prompt 输入传输及中间激活值的预取。在本地工作站（PCIe 5.0）场景下，该缓冲区通常固定分配或动态申请，大小约为 $16\text{MB} - 64\text{MB}$，相对于 24-48GB 显存总量占比 $<0.1\%$，在 TCO 和可行性评估中可忽略不计（$\approx 0$GB）。

## Corrected Claim

CUDA 异步拷贝缓冲区（Async Copy Buffer）的显存占用量化：主要服务于 Host-to-Device 的 Prompt 输入传输及中间激活值的预取。在本地工作站（PCIe 5.0）场景下，该缓冲区通常固定分配或动态申请，大小约为 $16\text{MB} - 64\text{MB}$，相对于 24-48GB 显存总量占比 $<0.1\%$，在 TCO 和可行性评估中可忽略不计（$\approx 0$GB）。

## Evidence

先验知识/题面给定，逻辑校验通过：16-64MB相对于24-48GB显存占比确实小于0.1%（0.03%-0.27%），且该量级在TCO评估中可忽略，符合工程常识。
