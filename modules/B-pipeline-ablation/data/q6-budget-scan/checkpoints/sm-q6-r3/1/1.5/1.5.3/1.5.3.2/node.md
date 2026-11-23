# N213: 自建边缘节点的单请求服务时间μ的微观分解：1/μ = T_disk_read + T_network_stack_overhead + T_compressio

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N65

## Claim

自建边缘节点的单请求服务时间μ的微观分解：1/μ = T_disk_read + T_network_stack_overhead + T_compression，其中T_disk_read取决于存储介质（NVMe SSD约0.1-0.5ms，HDD约5-10ms），T_network_stack_overhead为内核协议栈处理时间（Linux约0.05-0.2ms），T_compression为Gzip/Brotli压缩耗时（CPU密集型，约0.5-2ms），需根据硬件配置确定μ的具体数值范围

## Corrected Claim

自建边缘节点的单请求服务时间μ的微观分解：1/μ = T_disk_read + T_network_stack_overhead + T_compression，其中T_disk_read取决于存储介质（NVMe SSD约0.1-0.5ms，HDD约5-10ms），T_network_stack_overhead为内核协议栈处理时间（Linux约0.05-0.2ms），T_compression为Gzip/Brotli压缩耗时（CPU密集型，约0.5-2ms），需根据硬件配置确定μ的具体数值范围

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

edge server disk read latency NVMe SSD network stack overhead compression time breakdown
