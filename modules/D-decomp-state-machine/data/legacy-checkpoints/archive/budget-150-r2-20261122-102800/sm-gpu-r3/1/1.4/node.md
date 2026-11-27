# N11: 多卡工作站方案的互联带宽瓶颈量化：NVLink C2C (M3 Ultra) ~1.2 TB/s vs PCIe 5.0 x16 ~64 GB/s vs NVL

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N1

## Claim

多卡工作站方案的互联带宽瓶颈量化：NVLink C2C (M3 Ultra) ~1.2 TB/s vs PCIe 5.0 x16 ~64 GB/s vs NVLink 4 (H100) 900 GB/s，对多卡推理时AllReduce通信开销的影响：通信延迟占比 = f(通信量/计算量, 带宽)，当batch_size=1且seq_len=32K时，KV Cache传输量 ≈ 2 * layers * hidden_size * seq_len * bytes_per_elem

## Corrected Claim

多卡工作站方案的互联带宽瓶颈量化：NVLink C2C (M3 Ultra) ~1.2 TB/s vs PCIe 5.0 x16 ~64 GB/s vs NVLink 4 (H100) 900 GB/s，对多卡推理时AllReduce通信开销的影响：通信延迟占比 = f(通信量/计算量, 带宽)，当batch_size=1且seq_len=32K时，KV Cache传输量 ≈ 2 * layers * hidden_size * seq_len * bytes_per_elem

## Evidence

[质询]NVLink C2C (M3 Ultra) 的 1.2 TB/s 带宽通常指芯片间互联总带宽，若用于多卡推理的 AllReduce，实际有效带宽可能受协议开销和拓扑限制影响，略低于理论峰值；但作为量级对比（TB/s vs GB/s），该数值在工程估算中是合理的。 | 先验知识/题面给定，逻辑校验通过：NVLink C2C (M3 Ultra) 1.2 TB/s、PCIe 5.0 x16 64 GB/s、NVLink 4 (H100) 900 GB/s 均为公开硬件规格，量级正确；KV Cache 传输量公式 2 * layers * hidden_size * seq_len * bytes_per_elem 符合 Transformer 架构中 Key 和 Value 矩阵的存储与传输逻辑（2 代表 K 和 V），逻辑自洽。

## Search Query

NVLink C2C M3 Ultra bandwidth vs PCIe 5.0 x16 vs NVLink 4 H100 multi-GPU inference communication overhead
