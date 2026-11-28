# N136: TP=4 执行 All-Reduce 操作时，单卡需发送的数据量为 hidden_size * batch_size * dtype_size。假设 Qwen3

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N42

## Claim

TP=4 执行 All-Reduce 操作时，单卡需发送的数据量为 hidden_size * batch_size * dtype_size。假设 Qwen3.8-27B hidden_size=4096, dtype=FP16 (2 bytes), batch_size=1 (单序列推理)，单次 All-Reduce 通信量为 8 KB；由于 NVLink 双向带宽 300 GB/s，单次通信理论延迟 < 0.001 ms，通信开销可忽略不计。

## Corrected Claim

TP=4 执行 All-Reduce 操作时，基于 Ring 算法，单卡实际传输的数据量约为 1.5 * hidden_size * batch_size * dtype_size。假设 Qwen3.8-27B hidden_size=4096, dtype=FP16, batch_size=1，单次 All-Reduce 单卡传输量约为 12 KB。NVLink 带宽下延迟极低（微秒级），单次开销小，但在高频率调用下累积开销需考虑。

## Evidence

[质询]数值计算错误：hidden_size(4096) * batch_size(1) * dtype_size(2 bytes) = 8192 bytes = 8 KB，这部分正确。但是，All-Reduce 的通信量通常指 Ring All-Reduce 算法下的总通信量，对于 N 个 GPU，每个 GPU 需要发送的数据量约为 2*(N-1)/N * DataSize。在 TP=4 的情况下，单卡发送量约为 1.5 * 8KB = 12KB，而非简单的 8KB。更关键的错误在于延迟计算：8KB / 300GB/s ≈ 0.000026 ms (26微秒)，虽然小于 0.001ms，但陈述中隐含的“通信开销可忽略”在高频调用下可能不准确，且主要错误在于对 All-Reduce 通信量的简化理解（忽略了算法系数）以及将“发送数据量”等同于“通信量”的口径混淆。此外，Qwen3.8-27B 的具体 hidden_size 是否为 4096 属于经验事实，需核实（通常 27B 模型的 hidden size 可能在 4096-8192 之间，若为 4096 则计算基础成立，但 All-Reduce 通信量描述不严谨）。 | 逻辑校验发现 All-Reduce 通信量计算忽略了 Ring 算法的系数（应为 ~1.5x 数据量），且将‘单卡发送数据量’直接等同于‘通信量’存在口径混淆；虽 source 为 knowledge 允许逻辑自洽即 verified，但此处存在明显的技术细节逻辑瑕疵（通信量定义不准），故降档。

## Search Query

Tensor Parallelism AllReduce communication volume calculation LLM
