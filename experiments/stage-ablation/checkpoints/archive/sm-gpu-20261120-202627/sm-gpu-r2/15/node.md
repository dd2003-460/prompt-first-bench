# N153: 吞吐量归一化基准值：以 1× H100 80GB 在 BF16 下的实测吞吐量 (假设 60 tokens/s) 作为 1.0 基准。其他硬件的归一化吞吐量 =

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

吞吐量归一化基准值：以 1× H100 80GB 在 BF16 下的实测吞吐量 (假设 60 tokens/s) 作为 1.0 基准。其他硬件的归一化吞吐量 = Actual_Throughput / 60。若 Actual_Throughput 为 15 tokens/s，则归一化值为 0.25。

## Corrected Claim

吞吐量归一化基准值：以 1× H100 80GB 在 BF16 下的实测吞吐量 (假设 60 tokens/s) 作为 1.0 基准。其他硬件的归一化吞吐量 = Actual_Throughput / 60。若 Actual_Throughput 为 15 tokens/s，则归一化值为 0.25。

## Evidence

检索失败: no sources from any channel (all 5 failed)
