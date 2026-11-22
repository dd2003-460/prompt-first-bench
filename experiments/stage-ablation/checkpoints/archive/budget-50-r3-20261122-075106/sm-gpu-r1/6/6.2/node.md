# N36: Intel Gaudi 3 (128GB) 在BF16精度下运行 Qwen3-27B 的稳态生成吞吐率（Token/s）约为 20-30，价格约为 $8,000

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N6

## Claim

Intel Gaudi 3 (128GB) 在BF16精度下运行 Qwen3-27B 的稳态生成吞吐率（Token/s）约为 20-30，价格约为 $8,000-$10,000，性价比指数（Token/s per $）约为 2.0-3.0

## Corrected Claim

Intel Gaudi 3 (128GB) 可用于加速 Qwen3-27B 模型，但具体BF16精度下的稳态生成吞吐率（Token/s）和价格需参考官方详细基准测试报告。

## Evidence

[质询]来源仅提供了测试硬件配置（1或4个Gaudi 3加速器），未提供具体的BF16精度下Qwen3-27B的稳态生成吞吐率数值（20-30 Token/s）或价格信息，无法直接验证具体数值。 | 来源[1]确认了Intel Gaudi 3用于加速Qwen3模型，但未提供具体吞吐率数值和价格，属于间接支持；经验事实（具体性能参数和价格）缺乏直接来源支持，故降级。

## Search Query

Intel Gaudi 3 128GB Qwen3-27B BF16 inference throughput tokens per second price

## Retrieval Sources

- {'url': 'https://www.intel.com/content/www/us/en/developer/articles/technical/accelerate-qwen3-large-language-models.html&rut=13bb1f1bde7cc782f44e27cba8f2a484309a263ba299b4173610f675890a4a76', 'type': 'ddg', 'title': 'Intel® AI Solutions Accelerate Qwen3 Large Language Models'}
