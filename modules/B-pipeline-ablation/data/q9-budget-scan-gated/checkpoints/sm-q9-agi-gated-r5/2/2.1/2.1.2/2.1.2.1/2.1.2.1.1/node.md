# N124: 修正N58通信量公式：TP=4 AllReduce通信量仅取决于batch_size和hidden_dim，与seq_len无关（KV Cache读取无AllR

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N58

## Claim

修正N58通信量公式：TP=4 AllReduce通信量仅取决于batch_size和hidden_dim，与seq_len无关（KV Cache读取无AllReduce，仅Attention Output投影后同步）。公式为 2 * batch_size * hidden_dim * bytes_per_element。在batch_size=1, hidden_dim=4096, fp16(2bytes)下，通信量为16KB，而非N58隐含的依赖seq_len的128KB量级。

## Corrected Claim

修正N58通信量公式：TP=4 AllReduce通信量仅取决于batch_size和hidden_dim，与seq_len无关（KV Cache读取无AllReduce，仅Attention Output投影后同步）。公式为 2 * batch_size * hidden_dim * bytes_per_element。在batch_size=1, hidden_dim=4096, fp16(2bytes)下，通信量为16KB，而非N58隐含的依赖seq_len的128KB量级。

## Evidence

先验知识/题面给定，逻辑校验通过：AllReduce通信量确实仅取决于参与同步张量的维度（batch_size * hidden_dim），与序列长度无关；计算 2 * 1 * 4096 * 2 = 16384 bytes = 16KB 正确。
