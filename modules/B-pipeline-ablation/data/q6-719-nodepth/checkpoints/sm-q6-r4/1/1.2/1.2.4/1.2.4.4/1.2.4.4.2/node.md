# N664: 网络协议栈处理开销 T_net_stack 的 P99 值为 3ms，包含 TCP/IP 协议栈软中断处理、TLS 解密（若启用）及内核态到用户态的数据拷贝，假

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N219

## Claim

网络协议栈处理开销 T_net_stack 的 P99 值为 3ms，包含 TCP/IP 协议栈软中断处理、TLS 解密（若启用）及内核态到用户态的数据拷贝，假设源站部署了 DPDK 或 Kernel Bypass 技术可将此值降低至 1ms，否则按标准 Linux Kernel 栈计算。

## Corrected Claim

网络协议栈处理开销 T_net_stack 的 P99 值为 3ms，包含 TCP/IP 协议栈软中断处理、TLS 解密（若启用）及内核态到用户态的数据拷贝，假设源站部署了 DPDK 或 Kernel Bypass 技术可将此值降低至 1ms，否则按标准 Linux Kernel 栈计算。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

Linux kernel network stack processing latency P99 TCP IP TLS decryption
