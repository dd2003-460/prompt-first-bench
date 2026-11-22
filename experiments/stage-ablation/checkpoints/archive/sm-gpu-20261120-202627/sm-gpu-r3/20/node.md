# N473: 在32K长上下文场景下，INT8量化KV Cache相比BF16 KV Cache导致的生成文本一致性下降量化指标：在LongBench或RULER基准测试中，

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

在32K长上下文场景下，INT8量化KV Cache相比BF16 KV Cache导致的生成文本一致性下降量化指标：在LongBench或RULER基准测试中，INT8 KV Cache的准确率通常比BF16低1-3%。需引用具体测试数据以验证在32K长度下，INT8 KV Cache的质量损失是否可忽略，从而支持采用INT8权重+INT8 KV Cache的低成本方案。

## Corrected Claim

在32K长上下文场景下，INT8量化KV Cache相比BF16 KV Cache导致的生成文本一致性下降量化指标：在LongBench或RULER基准测试中，INT8 KV Cache的准确率通常比BF16低1-3%。需引用具体测试数据以验证在32K长度下，INT8 KV Cache的质量损失是否可忽略，从而支持采用INT8权重+INT8 KV Cache的低成本方案。

## Evidence

检索失败: no sources from any channel (all 5 failed)
