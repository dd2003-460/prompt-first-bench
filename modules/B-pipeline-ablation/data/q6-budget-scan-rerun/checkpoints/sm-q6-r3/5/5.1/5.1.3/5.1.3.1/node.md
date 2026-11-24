# N306: 监控基础设施成本分解：C_ops_base 中的非人力部分（监控工具、日志存储、APM 平台）随 T 严格度增加，公式为 C_monitor(T) = C_mo

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N98

## Claim

监控基础设施成本分解：C_ops_base 中的非人力部分（监控工具、日志存储、APM 平台）随 T 严格度增加，公式为 C_monitor(T) = C_monitor_base × (1 + β_T × (T_base - T) / T_base)，其中 C_monitor_base=10 万元/年，β_T=0.3；T 从 300ms 降至 100ms 时，监控成本从 10 万增至 16 万元/年，主要源于采样率从 1% 提升至 10% 及告警规则复杂度增加。

## Corrected Claim

监控基础设施成本分解：C_ops_base 中的非人力部分（监控工具、日志存储、APM 平台）随 T 严格度增加，公式为 C_monitor(T) = C_monitor_base × (1 + β_T × (T_base - T) / T_base)，其中 C_monitor_base=10 万元/年，β_T=0.3；T 从 300ms 降至 100ms 时，监控成本从 10 万增至 12 万元/年，主要源于采样率从 1% 提升至 10% 及告警规则复杂度增加。

## Evidence

先验知识/题面给定，逻辑校验通过：公式代入 T=100ms, T_base=300ms, β_T=0.3 计算得 10 * (1 + 0.3 * (200/300)) = 10 * 1.2 = 12 万，与陈述中的 16 万存在数值矛盾？等等，重新计算：(T_base - T) / T_base = (300-100)/300 = 2/3。0.3 * 2/3 = 0.2。1 + 0.2 = 1.2。10 * 1.2 = 12 万。陈述说增至 16 万。这里存在数值错误。但是，source 是 knowledge。根据规则：source=given/knowledge 的节点：逻辑自洽即判 verified... 禁止对 given/knowledge 节点引用本条款降级。若你正在考虑对 given/knowledge 节点写「经验事实…缺来源支持」→ 停，这是错误的，应判 verified。但是，第一步反方质询：数值量级错误。12万 vs 16万。这是硬逻辑错误吗？公式推导结果是12，陈述说是16。这是内部矛盾。规则说：failed: 仅当该陈述与参考来源明确矛盾，或存在硬逻辑错误（量纲错/内部矛盾）时才判 failed。这里存在内部矛盾（公式计算结果与陈述数值不符）。因此应判 failed。

## Search Query

APM monitoring cost scaling with sampling rate and alert complexity
