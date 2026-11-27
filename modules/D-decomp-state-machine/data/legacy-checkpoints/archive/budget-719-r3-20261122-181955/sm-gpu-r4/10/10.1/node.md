# N123: 2x RTX 4090 通过 PCIe 4.0 x16 互联时的实际带宽为 64 GB/s (双向)，而 NVLink 4.0 带宽为 900 GB/s；在 T

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N37

## Claim

2x RTX 4090 通过 PCIe 4.0 x16 互联时的实际带宽为 64 GB/s (双向)，而 NVLink 4.0 带宽为 900 GB/s；在 TP=2 推理中，All-Reduce 通信量与模型层数成正比，通信开销占比 = (通信时间 / 总推理时间)，需具体计算在 32K 上下文下，每层 All-Reduce 的数据量（如 2 * n_kv_heads * head_dim * seq_len * dtype_size）及对应的 PCIe 传输时间。

## Corrected Claim

2x RTX 4090 通过 PCIe 4.0 x16 互联时的实际带宽为 64 GB/s (双向)，而 NVLink 4.0 带宽为 900 GB/s；在 TP=2 推理中，All-Reduce 通信量与模型层数成正比，通信开销占比 = (通信时间 / 总推理时间)，需具体计算在 32K 上下文下，每层 All-Reduce 的数据量（如 2 * n_kv_heads * head_dim * seq_len * dtype_size）及对应的 PCIe 传输时间。

## Evidence

父节点级核验失败（LLM 错误）：Unterminated string starting at: line 9 column 5 (char 796)
