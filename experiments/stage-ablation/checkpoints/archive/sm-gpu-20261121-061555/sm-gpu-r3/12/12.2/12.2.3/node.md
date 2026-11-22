# N385: A100 与 RTX 4090 在相同 27B 模型推理负载下的单位 Token 能耗对比（Joules/Token）：结合 N143 (4090 功耗) 和 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N135

## Claim

A100 与 RTX 4090 在相同 27B 模型推理负载下的单位 Token 能耗对比（Joules/Token）：结合 N143 (4090 功耗) 和 N146 (A100 功耗) 以及各自的吞吐量差异（A100 带宽更高但算力密度不同），计算每生成 1K Tokens 的耗电量，以修正 TCO 中的 OpEx 项。

## Corrected Claim

A100 与 RTX 4090 在 27B 模型推理下的单位 Token 能耗需结合实时功耗与吞吐量动态计算；通常 A100 因能效比优化在持续高负载下单位 Token 能耗可能低于 RTX 4090，但具体数值取决于推理框架与批处理策略。

## Evidence

[质询]该陈述声称进行了具体的能耗对比计算（Joules/Token），但缺乏具体的吞吐量数据（Tokens/s）和实测功耗数据，仅凭静态功耗上限（N143/N146）无法得出精确的单位Token能耗，且不同推理框架/批处理大小会导致吞吐量差异巨大，导致计算结果具有高度不确定性。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且具体能耗数值依赖动态负载数据，无法从第一性原理严格推出）

## Search Query

A100 vs RTX 4090 energy efficiency per token LLM inference comparison
