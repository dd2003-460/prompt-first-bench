# N749: 工作点 A（高性低成）：采用 2 块 10Gbps 网卡 + 32 核 CPU + Nginx + 本地 NVMe SSD，单台服务器稳定 QPS 容量 C_q

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N250, N252, N253

## Claim

工作点 A（高性低成）：采用 2 块 10Gbps 网卡 + 32 核 CPU + Nginx + 本地 NVMe SSD，单台服务器稳定 QPS 容量 C_qps 约为 25,000，瓶颈在于 CPU 上下文切换及 TLS 握手开销，网络利用率仅 40%。

## Corrected Claim

工作点 A（高性低成）：采用 2 块 10Gbps 网卡 + 32 核 CPU + Nginx + 本地 NVMe SSD，单台服务器稳定 QPS 容量 C_qps 约为 25,000，瓶颈在于 CPU 上下文切换及 TLS 握手开销，网络利用率仅 40%。

## Evidence

先验知识/题面给定，逻辑校验通过
