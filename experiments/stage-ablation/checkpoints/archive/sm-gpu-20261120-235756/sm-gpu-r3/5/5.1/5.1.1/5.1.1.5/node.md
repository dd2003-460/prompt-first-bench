# N282: SGLang 稳定性对比：统计 SGLang 在 Qwen3-27B 上的崩溃率（Crash Rate）及平均故障间隔时间（MTBF）；与 vLLM 社区 Fo

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N99, N100, N101

## Claim

SGLang 稳定性对比：统计 SGLang 在 Qwen3-27B 上的崩溃率（Crash Rate）及平均故障间隔时间（MTBF）；与 vLLM 社区 Fork 的稳定性进行对比，量化为每 100 次推理请求中的错误率，预期 SGLang 稳定性略低于 vLLM 原生支持，但高于社区 Fork [待核验]。

## Corrected Claim

SGLang 在 Qwen3-27B 上的稳定性表现（如崩溃率、MTBF）需通过实际基准测试量化，并与 vLLM 原生及社区 Fork 版本进行对比，以验证其稳定性是否介于两者之间。

## Evidence

[质询]该陈述包含具体的经验性量化指标（崩溃率、MTBF、每100次请求错误率）及特定模型（Qwen3-27B）下的性能对比结论，属于硬件/软件性能经验事实，无法从第一性原理推导，且缺乏任何来源支持。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）。

## Search Query

SGLang Qwen3-27B crash rate MTBF stability comparison vLLM
