# N219: 1×A100 80GB 在 BF16 下运行 Qwen3-27B 32K 上下文，理论上无需量化即可完整容纳权重与 KV Cache，单卡 BF16 推理吞吐量

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N70, N71, N72

## Claim

1×A100 80GB 在 BF16 下运行 Qwen3-27B 32K 上下文，理论上无需量化即可完整容纳权重与 KV Cache，单卡 BF16 推理吞吐量在 10-15 tokens/s 范围内波动，TCO/Throughput 约为 $0.020-$0.025/token，延迟稳定性优于多卡方案。

## Corrected Claim

1×A100 80GB 在 BF16 下运行 Qwen3-27B 32K 上下文，理论上无需量化即可完整容纳权重与 KV Cache，单卡 BF16 推理吞吐量受内存带宽限制，具体数值需实测确定，TCO/Throughput 估算约为 $0.020-$0.025/token，延迟稳定性在低并发场景下优于多卡方案。

## Evidence

[质询]吞吐量数值（10-15 tokens/s）与延迟稳定性结论缺乏具体硬件配置（如PCIe版本、内存带宽）及软件栈（如vLLM版本、batch size）支撑，且单卡80GB显存容纳27B模型权重（~54GB）后剩余显存有限，32K上下文下的KV Cache压力可能导致实际性能波动远超该范围，或需量化才能稳定运行。 | 先验知识/题面给定，逻辑校验通过：A100 80GB显存足以容纳Qwen3-27B BF16权重（~54GB）及32K上下文KV Cache（约10-20GB，取决于具体实现），显存容量逻辑自洽；但吞吐量与TCO为经验事实，无外部来源支持，且单卡推理延迟稳定性优于多卡方案的说法在特定高并发场景下可能不成立，故降级。

## Search Query

A100 80GB BF16 Qwen3-27B 32K context throughput TCO
