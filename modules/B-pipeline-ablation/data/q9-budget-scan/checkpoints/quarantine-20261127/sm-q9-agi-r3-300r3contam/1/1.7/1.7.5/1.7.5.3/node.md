# N150: 代码执行含 I/O 时的 P95 耗时 ~200ms 主要由磁盘随机读延迟贡献，若使用 SSD，单次 4KB 随机读 P95 为 50-100μs，但若涉及文件

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N52

## Claim

代码执行含 I/O 时的 P95 耗时 ~200ms 主要由磁盘随机读延迟贡献，若使用 SSD，单次 4KB 随机读 P95 为 50-100μs，但若涉及文件打开（open/close）系统调用，每次开销约 5-20μs，200ms 更可能源于网络 I/O（如 HTTP 请求）或大文件顺序读，需明确 I/O 类型以修正模型。

## Corrected Claim

代码执行含 I/O 时的 P95 耗时 ~200ms 主要由磁盘随机读延迟贡献，若使用 SSD，单次 4KB 随机读 P95 为 50-100μs，但若涉及文件打开（open/close）系统调用，每次开销约 5-20μs，200ms 更可能源于网络 I/O（如 HTTP 请求）或大文件顺序读，需明确 I/O 类型以修正模型。

## Evidence

先验知识/题面给定，逻辑校验通过：SSD随机读微秒级与200ms毫秒级存在数量级差异，推断200ms非由纯磁盘随机读主导符合物理直觉及系统性能常识。
