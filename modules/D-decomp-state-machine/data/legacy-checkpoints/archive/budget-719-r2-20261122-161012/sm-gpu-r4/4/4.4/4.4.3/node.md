# N107: 若考虑 2x RTX 4090 (TP=2) 方案，总显存 48GB (仍不足 55GB BF16 需求，需量化或 offload)，总带宽 2016 GB/s

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N23

## Claim

若考虑 2x RTX 4090 (TP=2) 方案，总显存 48GB (仍不足 55GB BF16 需求，需量化或 offload)，总带宽 2016 GB/s (受 PCIe 瓶颈限制，有效带宽可能降至 1.5x 单卡水平)。若采用 1x H100 (80GB)，显存充足，带宽 3350 GB/s。在 BF16 精度下，2x 4090 因显存不足不可行，除非降至 FP8 (27GB 权重 + 1GB KV = 28GB < 48GB)，此时 2x 4090 可行。

## Corrected Claim

若考虑 2x RTX 4090 (TP=2) 方案，总显存 48GB (仍不足 55GB BF16 需求，需量化或 offload)，总带宽 2016 GB/s (受 PCIe 瓶颈限制，有效带宽可能降至 1.5x 单卡水平)。若采用 1x H100 (80GB)，显存充足，带宽 3350 GB/s。在 BF16 精度下，2x 4090 因显存不足不可行，除非降至 FP8 (27GB 权重 + 1GB KV = 28GB < 48GB)，此时 2x 4090 可行。

## Evidence

父节点级核验未通过：不完备（子节点之间存在逻辑矛盾（父节点称FP8可行，子节点2称FP8不可行），且子节点2修正了父节点的结论，导致父节点与子节点在事实层面不一致，破坏了正交性中的‘不矛盾’要求；此外，父节点提到的‘PCIe瓶颈/有效带宽’这一关键性能约束在子节点中未被充分覆盖（仅子节点3提及吞吐，但未单独分析2x4090的带宽瓶颈对FP8/INT4方案的影响）。）

## Search Query

2x RTX 4090 tensor parallel 48GB VRAM Qwen3-27B FP8 feasibility
