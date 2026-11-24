# N599: 读取 I/O 放大系数 A_io = Block_Size / Object_Size = 1MB / 128KB = 8，每次读取实际传输数据量为请求数据量的

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N212

## Claim

读取 I/O 放大系数 A_io = Block_Size / Object_Size = 1MB / 128KB = 8，每次读取实际传输数据量为请求数据量的 8 倍

## Corrected Claim

读取 I/O 放大系数 A_io = Block_Size / Object_Size = 1MB / 128KB = 8，每次读取实际传输数据量为请求数据量的 8 倍

## Evidence

先验知识/题面给定，逻辑校验通过：I/O 放大系数定义为块大小除以对象大小，1MB/128KB=8，计算正确且符合存储系统基本原理。
