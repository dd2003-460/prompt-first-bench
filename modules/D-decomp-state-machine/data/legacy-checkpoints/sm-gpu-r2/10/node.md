# N28: 多卡互联开销与 TCO 修正：对于 2x 消费级 GPU 方案，PCIe 4.0 x16 链路带宽约为 64 GB/s，远低于 NVLink 的 900 GB/

- **status**: pending
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

多卡互联开销与 TCO 修正：对于 2x 消费级 GPU 方案，PCIe 4.0 x16 链路带宽约为 64 GB/s，远低于 NVLink 的 900 GB/s。在 32K 上下文下，若需跨卡传输 KV Cache 或激活值，通信开销将增加 10-20% 的延迟，并可能降低有效吞吐量。TCO 计算中需引入 Communication_Overhead_Factor (COF)，建议对多卡方案的吞吐量乘以 0.85-0.90 的折减系数以反映互联瓶颈。

## Corrected Claim

多卡互联开销与 TCO 修正：对于 2x 消费级 GPU 方案，PCIe 4.0 x16 链路带宽约为 64 GB/s，远低于 NVLink 的 900 GB/s。在 32K 上下文下，若需跨卡传输 KV Cache 或激活值，通信开销将增加 10-20% 的延迟，并可能降低有效吞吐量。TCO 计算中需引入 Communication_Overhead_Factor (COF)，建议对多卡方案的吞吐量乘以 0.85-0.90 的折减系数以反映互联瓶颈。

## Evidence

父节点级核验失败（LLM 错误）：Unterminated string starting at: line 9 column 5 (char 827)
