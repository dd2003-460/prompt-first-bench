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

父节点级核验未通过：不完备（子节点在硬件配置、精度和成本维度上互不重叠（正交），且无冗余。但父节点明确以 'NVIDIA A100 40GB' 为基准进行举例说明（指出需2卡或FP8单卡），而子节点 B1/B2/B3 分别使用了 H100、A100 80GB 和 H200，完全遗漏了父节点中提到的 'A100 40GB' 这一特定工作点的分解（例如：2x A100 40GB 或 1x A100 40GB FP8），导致子节点未能覆盖父节点定义的核心场景。）

## Search Query

NVIDIA A100 40GB memory bandwidth GB/s FP8 inference throughput
