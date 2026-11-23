# N382: 边缘节点固定开销 $L_{edge}$ 的量化估算：包括网络接口延迟、路由转发延迟及系统调用开销；典型值为 $1-3 \text{ ms}$，取决于硬件性能（如

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N143

## Claim

边缘节点固定开销 $L_{edge}$ 的量化估算：包括网络接口延迟、路由转发延迟及系统调用开销；典型值为 $1-3 \text{ ms}$，取决于硬件性能（如网卡 DMA 效率）和操作系统内核参数（如 TCP 缓冲区大小）。

## Corrected Claim

边缘节点固定开销 $L_{edge}$ 的量化估算：包括网络接口延迟、路由转发延迟及系统调用开销；典型值为 $1-3 \text{ ms}$，取决于硬件性能（如网卡 DMA 效率）和操作系统内核参数（如 TCP 缓冲区大小）。

## Evidence

先验知识/题面给定，逻辑校验通过
