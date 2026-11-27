# N251: 2× RTX 4090 在 INT8 量化下，若采用 Pipeline Parallelism (PP=2) 而非 Tensor Parallelism (TP

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N91, N92, N93

## Claim

2× RTX 4090 在 INT8 量化下，若采用 Pipeline Parallelism (PP=2) 而非 Tensor Parallelism (TP=2)，可完全避免每层 AllReduce 通信，仅需在层间传递隐藏状态（hidden_size=4096, BF16/INT8 约 8-16 KB/step），通信延迟可忽略不计（<0.1ms/step），此时实测吞吐接近理论带宽上限的 85-90%，即约 59-62 tokens/s。

## Corrected Claim

2× RTX 4090 在 INT8 量化下，若采用 Pipeline Parallelism (PP=2) 而非 Tensor Parallelism (TP=2)，可完全避免每层 AllReduce 通信，仅需在层间传递隐藏状态（hidden_size=4096, BF16/INT8 约 8-16 KB/step），通信延迟可忽略不计（<0.1ms/step）。此时实测吞吐取决于具体模型规模与序列长度，通常可接近理论带宽上限的 85-90%。

## Evidence

[质询]吞吐数值（59-62 tokens/s）缺乏具体模型规模（参数量）和序列长度上下文，且对于2x RTX 4090（总显存48GB，总带宽~1.6TB/s）而言，若运行大模型（如70B+），该吞吐值可能偏低或偏高取决于具体模型；若运行小模型，该值可能偏低。此外，'接近理论带宽上限的85-90%'这一效率假设在PP模式下虽通信少，但计算利用率受限于单卡算力与内存带宽平衡，具体数值高度依赖模型架构，属于经验事实而非纯逻辑推导。 | 经验事实，逻辑自洽但缺来源支持。PP=2确实消除了层内AllReduce，仅保留层间Hidden State传输（4096*2bytes=8KB或4096*1bytes=4KB，量级正确），通信延迟<0.1ms合理。但具体吞吐59-62 tokens/s是特定模型下的经验值，无法从第一性原理严格推出，且无外部来源验证该具体数值。
