# N110: 双卡推理中 All-Reduce 通信开销占比 η_comm 的计算公式为 η_comm = T_comm / (T_compute + T_comm)，其中 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N26

## Claim

双卡推理中 All-Reduce 通信开销占比 η_comm 的计算公式为 η_comm = T_comm / (T_compute + T_comm)，其中 T_comm ≈ (2 * num_layers * batch_size * hidden_dim * bytes) / bandwidth，对于 Qwen3-27B (64 layers, 4096 hidden_dim, BF16)，每层通信数据量约为 2 * 4096 * 2 * batch_size bytes，需结合具体 batch_size 和计算时间 T_compute 量化

## Corrected Claim

双卡推理中 All-Reduce 通信开销占比 η_comm 的计算公式为 η_comm = T_comm / (T_compute + T_comm)，其中 T_comm ≈ (2 * num_layers * batch_size * hidden_dim * bytes) / bandwidth，对于 Qwen3-27B (64 layers, 4096 hidden_dim, BF16)，每层通信数据量约为 2 * 4096 * 2 * batch_size bytes，需结合具体 batch_size 和计算时间 T_compute 量化

## Evidence

先验知识/题面给定，逻辑校验通过：All-Reduce 通信量公式及占比定义符合分布式计算基本原理，Qwen3-27B 参数（64层, 4096 hidden_dim, BF16=2bytes）代入计算逻辑自洽。

## Search Query

multi-GPU inference all-reduce communication overhead percentage PCIe vs NVLink
