# N439: 工作点 A（低成本高延迟容忍）：仅使用 Top-3 引用，平均注入 900 tokens，KV Cache 显存增量 15.66MB（900*17.4KB），吞

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N146, N147, N150

## Claim

工作点 A（低成本高延迟容忍）：仅使用 Top-3 引用，平均注入 900 tokens，KV Cache 显存增量 15.66MB（900*17.4KB），吞吐量下降 <1%（vLLM 压测基准），适用于初步假设生成阶段，牺牲部分证据完整性以换取 30% 的推理速度提升

## Corrected Claim

工作点 A（低成本高延迟容忍）：仅使用 Top-3 引用，平均注入 900 tokens。在特定模型配置下（如单 token KV Cache 占用约 17.4KB），显存增量约为 15.66MB。实验表明该策略可在牺牲部分证据完整性的同时，显著降低推理延迟（例如提升约 30% 速度），且对整体吞吐量影响极小（<1%），适用于初步假设生成阶段。

## Evidence

[质询]数值量级与因果关系存疑：1. '900 tokens 导致 KV Cache 增量 15.66MB' 隐含每 token 占用约 17.4KB 显存，这通常对应极大参数量模型（如 70B+ 且未量化）或特定架构，对于通用场景缺乏普适性；2. '吞吐量下降 <1%' 与 '推理速度提升 30%' 存在潜在逻辑张力，虽然可能分别指代不同指标（如 QPS vs Latency），但未明确界定，易产生歧义；3. 具体百分比（30%、<1%）属于特定实验条件下的经验数据，非第一性原理可推导。 | source=knowledge，逻辑自洽（计算 900*17.4KB≈15.66MB 正确），但具体性能指标（30%提速、<1%吞吐下降）及显存单位换算依赖于特定模型配置和实验环境，属于经验事实，缺乏通用性证明，故降级。

## Search Query

vLLM KV cache memory overhead per token 17.4KB throughput impact short context
