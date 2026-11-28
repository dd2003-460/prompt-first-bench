# N279: 动态降级策略的具体执行逻辑应定义为：当滑动窗口（如 10s）内的 AllReduce 平均耗时超过基线值的 1.2 倍时，自动将 TP 并行度从 4 降至 2（

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N88

## Claim

动态降级策略的具体执行逻辑应定义为：当滑动窗口（如 10s）内的 AllReduce 平均耗时超过基线值的 1.2 倍时，自动将 TP 并行度从 4 降至 2（若显存允许）或切换至 Ring-AllReduce 算法以规避 NVLink 热点；需预测试 TP=2 下的推理吞吐量与精度影响，以评估降级后的性能损失是否在可接受范围（如 <15%）。

## Corrected Claim

动态降级策略的具体执行逻辑应定义为：当滑动窗口（如 10s）内的 AllReduce 平均耗时超过基线值的 1.2 倍时，自动将 TP 并行度从 4 降至 2（若显存允许）或切换至 Ring-AllReduce 算法以规避 NVLink 热点；需预测试 TP=2 下的推理吞吐量与精度影响，以评估降级后的性能损失是否在可接受范围（如 <15%）。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

dynamic tensor parallelism degradation strategy ring allreduce fallback performance impact
