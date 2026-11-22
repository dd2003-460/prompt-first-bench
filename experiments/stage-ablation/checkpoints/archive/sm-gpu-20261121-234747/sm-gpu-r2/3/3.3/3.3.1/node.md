# N92: 2×RTX 3090在BF16精度下推理Qwen3-27B时，由于模型权重（54GB）超出单卡24GB显存，必须采用张量并行（Tensor Parallelis

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N15

## Claim

2×RTX 3090在BF16精度下推理Qwen3-27B时，由于模型权重（54GB）超出单卡24GB显存，必须采用张量并行（Tensor Parallelism）或流水线并行（Pipeline Parallelism）；若采用张量并行，每层Attention和FFN的中间激活值需通过PCIe 4.0 x16链路传输，单次all-reduce通信量约为 (hidden_size * 2 * batch_size * seq_len) * bytes_per_element，需计算该通信量占PCIe 4.0理论带宽（32GB/s）的百分比以评估瓶颈

## Corrected Claim

2×RTX 3090在BF16精度下推理Qwen3-27B时，由于模型权重（54GB）超出单卡24GB显存，必须采用张量并行（Tensor Parallelism）或流水线并行（Pipeline Parallelism）；若采用张量并行，每层Attention和FFN的中间激活值需通过PCIe 4.0 x16链路传输，单次all-reduce通信量约为 (hidden_size * 2 * batch_size * seq_len) * bytes_per_element，需计算该通信量占PCIe 4.0理论带宽（32GB/s）的百分比以评估瓶颈

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 3090显存为24GB，Qwen3-27B BF16权重约54GB，单卡无法容纳，必须并行；张量并行需All-Reduce通信，公式量纲正确，PCIe 4.0 x16带宽32GB/s符合规格。

## Search Query

tensor parallelism communication overhead PCIe 4.0 bandwidth calculation LLM inference
