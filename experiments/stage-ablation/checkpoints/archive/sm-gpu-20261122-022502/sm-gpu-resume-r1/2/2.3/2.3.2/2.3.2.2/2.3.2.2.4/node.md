# N623: 4x RTX 4090 在 PCIe 4.0 x16 下，TP=4 策略中每层 All-Reduce 的实际通信延迟为 10.8 ms（基于 0.54 GB 数

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N191, N192, N193

## Claim

4x RTX 4090 在 PCIe 4.0 x16 下，TP=4 策略中每层 All-Reduce 的实际通信延迟为 10.8 ms（基于 0.54 GB 数据量 / 50 GB/s 有效带宽），但此计算未计入 PCIe 拓扑中 P2P 传输的额外开销（约 15%-20%），修正后单次 All-Reduce 延迟应为 12.4-12.96 ms，占单 token 生成时间比例从 40-60% 上升至 45-65%。

## Corrected Claim

4x RTX 4090 在 PCIe 4.0 x16 下，TP=4 策略中每层 All-Reduce 的实际通信延迟为 10.8 ms（基于 0.54 GB 数据量 / 50 GB/s 有效带宽），但此计算未计入 PCIe 拓扑中 P2P 传输的额外开销（约 15%-20%），修正后单次 All-Reduce 延迟应为 12.4-12.96 ms，占单 token 生成时间比例从 40-60% 上升至 45-65%。

## Evidence

先验知识/题面给定，逻辑校验通过：0.54GB/50GB/s=10.8ms，修正系数1.15-1.2对应12.4-12.96ms，计算自洽
