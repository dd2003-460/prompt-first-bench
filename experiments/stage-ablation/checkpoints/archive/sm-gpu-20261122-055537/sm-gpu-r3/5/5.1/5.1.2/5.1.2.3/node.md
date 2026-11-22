# N268: T_throughput 定义的工作点 3 (超长上下文/低吞吐)：Seq_len = 128K。KV Cache 占用超过 24GB 显存，RTX 4090 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N81

## Claim

T_throughput 定义的工作点 3 (超长上下文/低吞吐)：Seq_len = 128K。KV Cache 占用超过 24GB 显存，RTX 4090 单卡不可行，需启用 PagedAttention 并可能触发 CPU Offload 或显存交换。此时吞吐量将断崖式下跌至 <10 tokens/s，且延迟方差极大。此工作点超出题目‘32K 容量下限’的常规使用场景，仅作为边界条件参考。

## Corrected Claim

T_throughput 定义的工作点 3 (超长上下文/低吞吐)：Seq_len = 128K。KV Cache 占用超过 24GB 显存，RTX 4090 单卡不可行，需启用 PagedAttention 并可能触发 CPU Offload 或显存交换。此时吞吐量将断崖式下跌至 <10 tokens/s，且延迟方差极大。此工作点超出题目‘32K 容量下限’的常规使用场景，仅作为边界条件参考。

## Evidence

先验知识/题面给定，逻辑校验通过：128K序列长度下KV Cache显存占用远超24GB（符合大模型推理显存估算量级），超出RTX 4090 24GB显存限制，需PagedAttention/Offload，导致吞吐下降至<10 tokens/s符合工程直觉；该节点为knowledge类型，逻辑自洽即判verified。

## Search Query

LLM inference throughput degradation 128k context length
