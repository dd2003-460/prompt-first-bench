# N137: 数据包组装与发送延迟 T_send 取决于内核网络栈效率：Linux内核发送延迟约为 0.1-0.5ms，若启用TCP_NODELAY且无拥塞则接近 0ms，若

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N41

## Claim

数据包组装与发送延迟 T_send 取决于内核网络栈效率：Linux内核发送延迟约为 0.1-0.5ms，若启用TCP_NODELAY且无拥塞则接近 0ms，若发生TCP重传则增加 1 RTT。

## Corrected Claim

数据包组装与发送延迟 T_send 取决于内核网络栈效率：Linux内核发送延迟约为 0.1-0.5ms，若启用TCP_NODELAY且无拥塞则接近 0ms，若发生TCP重传则增加 1 RTT。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

Linux kernel network stack send latency ms
