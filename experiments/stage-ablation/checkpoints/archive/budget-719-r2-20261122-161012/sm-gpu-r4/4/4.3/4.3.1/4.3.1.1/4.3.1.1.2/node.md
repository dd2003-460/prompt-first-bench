# N518: 在 PCIe 5.0 x16 链路 (带宽 ~64 GB/s) 下，8.192 KB 的 All-Reduce 通信延迟约为 0.13 µs，远低于 Decod

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N213

## Claim

在 PCIe 5.0 x16 链路 (带宽 ~64 GB/s) 下，8.192 KB 的 All-Reduce 通信延迟约为 0.13 µs，远低于 Decode 单 token 延迟 (~50-100 ms)，因此通信开销占比 < 0.001%，可忽略不计；但在 NVLink 缺失的消费级多卡方案中，若采用 P2P 内存拷贝而非 Ring All-Reduce，延迟可能增加 10-20 倍，仍需 < 1 ms，结论是通信非瓶颈，N213 的数值修正对最终 TCO 排序无实质影响，可标记为 [低优先级]。

## Corrected Claim

在 PCIe 5.0 x16 链路 (带宽 ~64 GB/s) 下，8.192 KB 的 All-Reduce 通信延迟约为 0.13 µs，远低于 Decode 单 token 延迟 (~50-100 ms)，因此通信开销占比 < 0.001%，可忽略不计；但在 NVLink 缺失的消费级多卡方案中，若采用 P2P 内存拷贝而非 Ring All-Reduce，延迟可能增加 10-20 倍，仍需 < 1 ms，结论是通信非瓶颈，N213 的数值修正对最终 TCO 排序无实质影响，可标记为 [低优先级]。

## Evidence

先验知识/题面给定，逻辑校验通过：PCIe 5.0 x16 带宽约 64 GB/s，传输 8.192 KB 数据耗时约 0.13 µs，远小于 Decode 延迟（50-100 ms），通信占比极低，结论合理。

## Search Query

PCIe 5.0 P2P latency LLM multi-GPU inference overhead negligible
