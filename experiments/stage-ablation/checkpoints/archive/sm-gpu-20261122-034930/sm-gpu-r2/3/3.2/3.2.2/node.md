# N93: A100 40GB 在典型 LLM 推理负载下的平均功耗约为 240-280W（TDP 400W 的 60-70%）[待核验]，年电力成本约为 $104-$12

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N23

## Claim

A100 40GB 在典型 LLM 推理负载下的平均功耗约为 240-280W（TDP 400W 的 60-70%）[待核验]，年电力成本约为 $104-$121（基于 $0.1/kWh），低于 N23 中基于满载 TDP 计算的 $173，需修正 TCO 模型中的电力成本项。

## Corrected Claim

A100 40GB 在典型 LLM 推理负载下的平均功耗通常低于其 400W TDP（具体数值需实测或参考特定基准测试），基于此估算的年电力成本低于基于满载 TDP 计算的 $173，建议修正 TCO 模型中的电力成本项以反映实际平均功耗。

## Evidence

[质询]该陈述包含具体的硬件功耗经验数据（A100在LLM推理下的平均功耗240-280W）及由此推导的经济成本，属于经验事实而非第一性原理可推导内容。由于检索失败无外部来源支持，且不同负载下功耗波动较大，具体数值区间缺乏实证依据。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）。

## Search Query

A100 40GB average power consumption LLM inference load
