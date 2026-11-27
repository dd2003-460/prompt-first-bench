# N24: 代表工作点 B（数据中心高容量）：以 NVIDIA A100 40GB (1.6 TB/s) 为例，单卡无法容纳 BF16 Qwen3-27B (54GB)，需

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

代表工作点 B（数据中心高容量）：以 NVIDIA A100 40GB (1.6 TB/s) 为例，单卡无法容纳 BF16 Qwen3-27B (54GB)，需 2 卡；若使用 FP8 (27GB) 单卡可容纳，理论 Decode 吞吐上限约为 1600 / 27 ≈ 59.3 tokens/s，展示高带宽数据中心卡的优势。

## Corrected Claim

代表工作点 B（数据中心高容量）：以 NVIDIA A100 40GB (1.6 TB/s) 为例，单卡无法容纳 BF16 Qwen3-27B (54GB)，需 2 卡；若使用 FP8 (27GB) 单卡可容纳，理论 Decode 吞吐上限约为 1600 / 27 ≈ 59.3 tokens/s，展示高带宽数据中心卡的优势。

## Evidence

父节点级核验未通过：非正交, 有冗余（子节点B1和B2在硬件规格（带宽2039 GB/s）和理论性能（75.5 tokens/s）上完全重复，仅价格不同，导致非正交；且B1/B2/B3本质上是同一公式（带宽/模型大小）在不同硬件参数下的取值，存在结构性冗余。）

## Search Query

NVIDIA A100 40GB memory bandwidth GB/s FP8 inference throughput
