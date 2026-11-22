# N35: AMD MI210 (64GB) 在BF16精度下运行 Qwen3-27B 的稳态生成吞吐率（Token/s）约为 25-35，价格约为 $10,000-$12

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N6

## Claim

AMD MI210 (64GB) 在BF16精度下运行 Qwen3-27B 的稳态生成吞吐率（Token/s）约为 25-35，价格约为 $10,000-$12,000，性价比指数（Token/s per $）约为 2.1-3.5

## Corrected Claim

AMD MI210 (64GB) 支持在BF16精度下运行 Qwen3-27B，具体稳态生成吞吐率与性价比指数需参考实际基准测试数据，当前缺乏确切数值支持。

## Evidence

[质询]来源仅提及部署配置（2x MI210, BF16, vLLM），未提供具体的稳态生成吞吐率数值（25-35 Token/s）或硬件价格（$10,000-$12,000），属于经验事实且缺乏直接数据支持。 | 来源[1]确认了AMD MI210运行Qwen3-27B (BF16)的场景，但未提供吞吐率和价格的具体数值，无法直接验证量化指标；逻辑上量级合理，但作为经验事实缺来源直接支持。

## Search Query

AMD MI210 64GB Qwen3-27B BF16 inference throughput tokens per second price

## Retrieval Sources

- {'url': 'https://github.com/zebrax0r/AMD_MI210_Bunya_LLM_tools_Qwen3.8-27B/tree/main&rut=680a00ab0fa71ec9de4ddfdd624826a420badb6c3654b8d1de4a5568240be8d0', 'type': 'ddg', 'title': "Qwen3.8-27B on Bunya's AMD MI210 nodes - GitHub"}
