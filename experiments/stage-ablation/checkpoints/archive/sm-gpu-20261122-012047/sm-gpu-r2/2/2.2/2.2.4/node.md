# N79: RTX 4090 在 LLM 推理负载下的实际平均功耗约为 380-420W（低于 TDP 450W 的 84-93%），因为推理过程包含大量内存等待时间，GP

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N15

## Claim

RTX 4090 在 LLM 推理负载下的实际平均功耗约为 380-420W（低于 TDP 450W 的 84-93%），因为推理过程包含大量内存等待时间，GPU 核心并非 100% 满载；H100 SXM5 在相同负载下实际平均功耗约为 600-650W（低于 TDP 700W 的 86-93%）。

## Corrected Claim

RTX 4090 在 LLM 推理负载下的实际平均功耗约为 380-420W（低于 TDP 450W 的 84-93%）；H100 SXM5 在相同负载下的实际平均功耗数据需进一步核实，通常低于其 700W TDP。

## Evidence

[质询]H100 SXM5 的功耗数据（600-650W）在提供的参考来源中完全缺失，且该数值属于经验事实，无法仅凭逻辑推导验证；RTX 4090 的数据虽有来源支持，但整体陈述因部分数据缺乏证据而存在不确定性。 | RTX 4090 部分有来源 [2] 直接支持（AI 推理实测 398W，符合 380-420W 区间）及来源 [3] 确认 TDP 为 450W；但 H100 SXM5 部分无任何来源覆盖，属于经验事实且缺来源支持，故降级。

## Search Query

RTX 4090 H100 actual power consumption LLM inference benchmark average wattage

## Retrieval Sources

- {'url': 'https://cloud.tencent.com/developer/article/2741154&rut=6fd9f56f7ee63da93621d0f40e7e45a5099c43c56976295fe6dd96d90e69bf96', 'type': 'ddg', 'title': '在租来的 Rtx 4090 上实测 Llm 量化能耗：Nf4 过了 3b 才省电，Int8 全军覆没'}
- {'url': 'https://blog.csdn.net/m0_57112626/article/details/159352968&rut=cd391fd52071fd93872760da4ffdf06f2aaa0d0cf5518cf4fed9a3de0a0669d3', 'type': 'ddg', 'title': 'Rtx 4090三类负载功耗实测 - Csdn博客'}
- {'url': 'https://www.promptquorum.com/local-llms/local-llm-power-consumption&rut=299898e8c33149f5d5b4de2be4a5d12ca490cf300903bf7d449d2cf2fd8ed1a3', 'type': 'ddg', 'title': 'Local LLM Power Consumption 2026: RTX 4090 450W = $39/mo'}
