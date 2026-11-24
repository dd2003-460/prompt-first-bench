# N520: 公有云 CDN 单区域缓存池容量 C_cloud_storage 的实际物理约束取决于底层 NVMe 磁盘阵列配置，典型单节点（如阿里云边缘节点）配置 2-4 

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N169

## Claim

公有云 CDN 单区域缓存池容量 C_cloud_storage 的实际物理约束取决于底层 NVMe 磁盘阵列配置，典型单节点（如阿里云边缘节点）配置 2-4 块 3.84TB NVMe SSD，总物理容量约 7.68-15.36TB，扣除 15%-20% 元数据和文件系统开销后，有效容量 C_eff ≈ 6-13TB，而非 PB 级（PB 级为全集群总量）。

## Corrected Claim

公有云 CDN 单区域缓存池容量受底层存储硬件限制，典型单节点物理容量通常在 TB 级别（如数 TB 至十余 TB），而非 PB 级；具体数值取决于厂商硬件配置（如 NVMe SSD 数量与单盘容量）及文件系统开销。

## Evidence

[质询]具体硬件配置（2-4块3.84TB NVMe）及有效容量数值属于特定厂商的特定时期经验参数，缺乏公开权威来源直接证实，且不同节点/时期配置可能不同，存在以偏概全风险。 | 参考来源[1][2][3]仅涉及CDN缓存策略配置，未涉及底层物理存储硬件规格，无法提供外部支持；该陈述为经验事实，逻辑自洽但缺来源支持。

## Search Query

Alibaba Cloud CDN edge node NVMe SSD capacity specifications per node

## Retrieval Sources

- {'url': 'https://docs.cloudbase.net/storage/pg/cdn&rut=e954aebb8652a65d533e62aee8e5c74e70e630ef989f5795c1a86be571be703a', 'type': 'ddg', 'title': 'CDN 加速与缓存 | 腾讯云开发 CloudBase - AI 原生后端一体化平台'}
- {'url': 'https://cloud.tencent.com/developer/article/1990879&rut=f658c4acfb8d864603317c98547b5012a9cdcefefab76d4070f09759e2b8f2b6', 'type': 'ddg', 'title': '【最佳实践】内容分发网络（Cdn）配置缓存规则 - 腾讯云'}
- {'url': 'https://docs.cloud.google.com/cdn/docs/caching?hl=zh-cn&rut=e8cfb8b7169c19954adb61165dee62a851bcc213bc5f61a12d6cef760edfcce1', 'type': 'ddg', 'title': '缓存概览 | Cloud CDN | Google Cloud Documentation'}
