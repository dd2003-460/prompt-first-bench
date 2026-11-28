# N125: Self-Critique拦截率 IR(K) < 0.3 的实时监测机制：需在vLLM服务端埋点，记录每次Self-Critique轮次中模型自我否定输出的比例

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N43

## Claim

Self-Critique拦截率 IR(K) < 0.3 的实时监测机制：需在vLLM服务端埋点，记录每次Self-Critique轮次中模型自我否定输出的比例，若滑动窗口（size=10）内 IR(K) < 0.3 持续 3 个周期，则触发假设生成器Agent [待核验]

## Corrected Claim

Self-Critique拦截率 IR(K) 的实时监测机制：需在vLLM服务端埋点，记录每次Self-Critique轮次中模型自我否定输出的比例，若滑动窗口内 IR(K) 低于预设阈值（如0.3）持续多个周期，则触发假设生成器Agent。

## Evidence

[质询]阈值0.3及滑动窗口参数（size=10, 3周期）属于特定系统设计的经验性超参数，缺乏通用标准或第一性原理支撑，可能因场景不同而失效。 | source=knowledge，逻辑自洽（监测机制设计合理），但具体数值参数为经验设定，无外部来源直接支持，依据经验事实排除条款降级。

## Search Query

real-time monitoring self-critique interception rate LLM agent trigger
