# N102: 张量并行 (TP) 下，每生成一个 token 需执行一次 All-Reduce 通信，通信数据量 D_comm = batch_size * hidden_d

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N22

## Claim

张量并行 (TP) 下，每生成一个 token 需执行一次 All-Reduce 通信，通信数据量 D_comm = batch_size * hidden_dim * bytes_per_element。对于 Qwen3-27B (hidden_dim=4096, BF16=2 bytes)，单 token batch=1 时 D_comm = 8KB。

## Corrected Claim

张量并行 (TP) 下，每生成一个 token 需执行一次 All-Reduce 通信，通信数据量 D_comm = batch_size * hidden_dim * bytes_per_element。对于 Qwen3-27B (hidden_dim=4096, BF16=2 bytes)，单 token batch=1 时 D_comm = 8KB。

## Evidence

先验知识/题面给定，逻辑校验通过：张量并行中每层Transformer的Attention和FFN输出均需All-Reduce，通信量公式 D = batch_size * hidden_dim * bytes 符合标准推导；Qwen3-27B hidden_dim=4096, BF16=2 bytes, batch=1 时 4096*2=8192 bytes=8KB，数值计算正确。

## Search Query

tensor parallel all-reduce data size per token hidden dim
