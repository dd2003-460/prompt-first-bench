# N362: TP=2 场景下，每生成 1 token 的 All-Reduce 通信量与计算时间比 (Comm/Compute Ratio) 计算：Comm_Vol = 2

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N114

## Claim

TP=2 场景下，每生成 1 token 的 All-Reduce 通信量与计算时间比 (Comm/Compute Ratio) 计算：Comm_Vol = 2 × hidden_dim × bytes_per_element × num_heads_per_partition (对于 Qwen3-27B FP16, 约 16KB/layer)，Compute_Time = (2 × params_per_layer × hidden_dim × seq_len) / (FLOPS_peak × MFU)。在 32K 上下文 Batch=1 下，计算该比值以判断通信是否为瓶颈。

## Corrected Claim

TP=2 场景下，每生成 1 token 的 All-Reduce 通信量主要取决于隐藏层维度 (hidden_dim) 和数据类型，公式应为 Comm_Vol ≈ 2 × hidden_dim × bytes_per_element（忽略头数因子，或明确 hidden_dim 为单头维度）。对于 Qwen3-27B (hidden_dim=4096, FP16)，单层通信量约为 8KB-16KB 量级，需结合具体 MFU 和 FLOPS 计算比值。

## Evidence

[质询]公式中 `num_heads_per_partition` 的引入缺乏理论依据。在标准的 Tensor Parallelism (TP) 中，All-Reduce 通信量通常取决于隐藏层维度 (hidden_dim) 或注意力头维度 (head_dim)，而非直接乘以 `num_heads_per_partition`。若 `hidden_dim` 已包含所有头的维度，再乘以头数会导致通信量被高估一个数量级（例如 Qwen3-27B hidden_dim=4096，若再乘以头数，数值将远超 16KB 的合理量级，除非 `hidden_dim` 在此处被错误地定义为单头维度，但这与常规命名冲突）。此外，16KB/layer 的估算对于 27B 模型（hidden_dim 通常 > 4000）在 FP16 下（4096*2=8KB）可能偏低或偏高，取决于具体架构细节，公式本身的逻辑自洽性存疑。 | source=knowledge，但公式逻辑存在内部矛盾：All-Reduce 通信量不应简单由 hidden_dim 乘以 num_heads 决定，且 16KB 的估算与常见大模型 hidden_dim 量级（通常 4K-8K+）在 FP16 下的字节数（8KB-16KB+）虽在数量级上勉强兼容，但公式结构错误导致无法从第一性原理严格推出，属于经验事实且逻辑校验未通过。
