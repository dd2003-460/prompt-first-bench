# N92: 2×RTX 3090在BF16精度下推理Qwen3-27B时，由于模型权重（54GB）超出单卡24GB显存，必须采用张量并行（Tensor Parallelis

- **status**: pending
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

父节点级核验未通过：不完备, 有冗余（子节点1和2本质上是同一公式在不同工作负载（Prefill vs Decode）下的参数化实例，存在结构冗余；同时，父节点明确要求评估‘瓶颈’（即通信量占带宽的百分比/耗时对比），但子节点1仅指出‘远超能力’而未给出具体百分比或耗时，子节点2虽给出耗时但未明确对比计算时间占比，且子节点3引入了父节点未提及的‘实测带宽’变量，导致与父节点定义的‘理论带宽32GB/s’评估标准不一致。）

## Search Query

tensor parallelism communication overhead PCIe 4.0 bandwidth calculation LLM inference
