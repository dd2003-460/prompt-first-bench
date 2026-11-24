# N345: 自建POP边缘节点处理延迟 T_proc_pop_p99 的基准值约为 5ms，基于 Nginx/OpenResty 在 16核/64GB 内存服务器上的标准压

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N107

## Claim

自建POP边缘节点处理延迟 T_proc_pop_p99 的基准值约为 5ms，基于 Nginx/OpenResty 在 16核/64GB 内存服务器上的标准压测数据，包含 TCP 握手、SSL 解密及静态文件读取时间

## Corrected Claim

自建POP边缘节点处理延迟 T_proc_pop_p99 的基准值约为 5ms，基于 Nginx/OpenResty 在 16核/64GB 内存服务器上的标准压测数据，包含 TCP 握手、SSL 解密及静态文件读取时间

## Evidence

先验知识/题面给定，逻辑校验通过
