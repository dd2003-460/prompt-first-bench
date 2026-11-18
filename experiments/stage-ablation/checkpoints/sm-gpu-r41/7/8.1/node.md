# N81: H100 SXM5 在运行 Qwen3-27B (BF16) 时的实际功耗为 650W-700W，而非理论满载 700W，需根据负载率修正

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N28, N29, N30

## Claim

H100 SXM5 在运行 Qwen3-27B (BF16) 时的实际功耗为 650W-700W，而非理论满载 700W，需根据负载率修正

## Corrected Claim

H100 SXM5 在运行 Qwen3-27B (BF16) 时的实际功耗通常低于其 700W 的 TDP 上限，具体数值（如 650W-700W）需根据实际负载率和推理框架配置进行测量修正。

## Evidence

[质询]具体数值（650W-700W）缺乏直接来源支持，且实际功耗高度依赖于具体的推理框架、Batch Size及并发负载，仅凭模型大小和精度无法确定唯一的功耗区间，存在将特定测试场景泛化为通用事实的风险。 | 来源[1]和[2]均未提供H100运行Qwen3-27B的具体功耗数据，属于经验事实且缺来源直接支持，但逻辑上低于TDP（700W）是合理的。

## Search Query

H100 SXM5 power consumption running LLM inference 27B model watts

## Retrieval Sources

- {'url': 'https://docs.nvidia.com', 'type': None, 'title': 'direct-browser: docs.nvidia.com'}
- {'url': 'http://arxiv.org/abs/2608.15764v1', 'type': 'arxiv', 'title': 'Concurrency Response of Plain Global Loads on the NVIDIA H100'}
