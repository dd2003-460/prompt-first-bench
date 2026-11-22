# N283: LLaMA.cpp 稳定性对比：统计 LLaMA.cpp 在 Qwen3-27B 上的崩溃率（Crash Rate）及平均故障间隔时间（MTBF）；与 vLLM

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N99, N100, N101

## Claim

LLaMA.cpp 稳定性对比：统计 LLaMA.cpp 在 Qwen3-27B 上的崩溃率（Crash Rate）及平均故障间隔时间（MTBF）；与 vLLM 社区 Fork 的稳定性进行对比，量化为每 100 次推理请求中的错误率，预期 LLaMA.cpp 稳定性最高，但吞吐量最低 [待核验]。

## Corrected Claim

LLaMA.cpp 在 Qwen3-27B 上的稳定性表现（如崩溃率、MTBF）及与 vLLM 社区 Fork 的对比数据需通过特定环境下的基准测试获取；通常 LLaMA.cpp 以高稳定性著称但吞吐量较低，具体量化指标（如每 100 次请求错误率）因测试条件而异，需实测验证。

## Evidence

[质询]该陈述包含具体的经验性量化指标（崩溃率、MTBF、每100次请求错误率），这些是依赖于具体硬件环境、软件版本、并发负载及测试方法的经验事实，无法从第一性原理推导，且缺乏任何来源支持其具体数值或相对排名的绝对正确性。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法验证具体量化数据及稳定性排名的绝对准确性）

## Search Query

LLaMA.cpp Qwen3-27B crash rate MTBF stability comparison vLLM
