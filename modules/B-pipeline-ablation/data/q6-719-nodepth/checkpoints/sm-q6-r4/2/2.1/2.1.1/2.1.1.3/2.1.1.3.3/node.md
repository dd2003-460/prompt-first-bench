# N597: 支持 RDMA (RoCEv2) 的 10Gbps 双口 NIC (如 Mellanox ConnectX-4 Lx) 的 2024 年市场均价约为 ¥4,00

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N205

## Claim

支持 RDMA (RoCEv2) 的 10Gbps 双口 NIC (如 Mellanox ConnectX-4 Lx) 的 2024 年市场均价约为 ¥4,000-6,000/张，溢价约 100-200%，其核心价值在于内核旁路 (Kernel Bypass) 和低延迟 (微秒级)，适用于对 P99 延迟极端敏感 (<5ms) 的场景；对于普通 CDN 缓存节点，RDMA 带来的延迟收益 (<1ms) 通常不足以抵消其高额成本，除非用于内部高速存储集群互联。

## Corrected Claim

支持 RDMA (RoCEv2) 的 10Gbps 双口 NIC (如 Mellanox ConnectX-4 Lx) 具备内核旁路和低延迟特性，适用于对 P99 延迟极端敏感的场景；对于普通 CDN 缓存节点，RDMA 带来的延迟收益通常不足以抵消其相对较高的成本，除非用于内部高速存储集群互联。

## Evidence

[质询]2024年市场均价¥4,000-6,000及溢价比例属于具体商业数据，缺乏实时市场报价支持，且ConnectX-4 Lx作为较老型号，其价格波动大，该数值区间可能不准确或仅适用于特定渠道/批量采购，无法从通用来源直接验证。 | 来源[1]直接支持ConnectX-4 Lx支持RDMA、10Gbps及低延迟特性，但未提供2024年具体市场价格数据；价格部分为经验事实，逻辑自洽但缺来源直接支持。

## Search Query

Mellanox ConnectX-4 Lx RoCE NIC price 2024 latency benefit CDN edge node

## Retrieval Sources

- {'url': 'https://www.nvidia.com/en-in/networking/ethernet/connectx-4-lx/&rut=f5b0691bd516be9aa383b6996bc74cc6a22722d78ed87a92628ac5505ad106cf', 'type': 'ddg', 'title': 'NVIDIA Mellanox ConnectX-4 Lx Ethernet Adapter | NVIDIA'}
