# N296: AMD RX 7900 XTX 在 Qwen3-27B FP8 推理下的实测吞吐量（Tokens/s）基准值：需参考 ROCm 6.x + vLLM/Tenso

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N106

## Claim

AMD RX 7900 XTX 在 Qwen3-27B FP8 推理下的实测吞吐量（Tokens/s）基准值：需参考 ROCm 6.x + vLLM/TensorRT 在 32K 上下文下的基准测试，若吞吐量为 RTX 4090 的 80%（例如 4090 为 50 tok/s，7900 XTX 为 40 tok/s），则单位 Token 能耗比（Joule/Token）将增加 25%。

## Corrected Claim

AMD RX 7900 XTX 在 Qwen3-27B FP8 推理下的实测吞吐量基准值需参考具体 ROCm 版本及 vLLM 配置。若其吞吐量为 RTX 4090 的 80%，则单位 Token 能耗比将增加 25%（假设功耗恒定或线性相关）。

## Evidence

[质询]该陈述包含具体的硬件性能基准数据（RTX 4090 50 tok/s, RX 7900 XTX 40 tok/s）及能耗比推导，属于经验事实。检索无可用来源，无法验证具体数值是否准确，且不同模型、上下文长度及软件栈版本下吞吐量波动极大，单一基准值缺乏普适性。 | 经验事实，逻辑自洽但缺来源支持。数学推导部分正确：若吞吐量降低至80%（1/0.8=1.25），在功耗假设不变或线性关系下，单位Token能耗确实增加25%。但具体吞吐量数值（50/40 tok/s）无外部证据支持，且受具体测试条件影响大，故降级。

## Search Query

RX 7900 XTX Qwen3 27B inference throughput tokens per second ROCm benchmark
