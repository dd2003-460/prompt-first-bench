# N153: RTX 4090 在 LLM 推理 Decode 阶段的实际功耗并非恒定 450W，而是随显存带宽利用率动态变化，实测峰值功耗约 400-450W，平均功耗（持

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N32

## Claim

RTX 4090 在 LLM 推理 Decode 阶段的实际功耗并非恒定 450W，而是随显存带宽利用率动态变化，实测峰值功耗约 400-450W，平均功耗（持续生成）约为 350-400W，需按实际负载曲线积分计算年均电力成本而非简单乘以 TDP。

## Corrected Claim

RTX 4090 在 LLM 推理 Decode 阶段的实际功耗并非恒定 450W（TDP），而是随负载动态变化，实测峰值功耗可达 450W，平均功耗通常低于 TDP，需按实际负载曲线积分计算年均电力成本而非简单乘以 TDP。

## Evidence

[质询]来源仅提供了RTX 4090的TDP/最大功耗（450W）及基于此的月度电费估算，未提供LLM Decode阶段具体的“平均功耗350-400W”或“随显存带宽利用率动态变化”的实测数据，具体数值缺乏直接证据支持。 | 来源[1]和[3]确认RTX 4090 TDP为450W，但未覆盖LLM推理Decode阶段的平均功耗具体数值（350-400W），属于经验事实且缺乏直接来源支持，仅逻辑上合理（平均功耗低于峰值）。

## Search Query

RTX 4090 actual power consumption LLM inference decode vs prefill watts

## Retrieval Sources

- {'url': 'https://www.promptquorum.com/local-llms/local-llm-power-consumption&rut=299898e8c33149f5d5b4de2be4a5d12ca490cf300903bf7d449d2cf2fd8ed1a3', 'type': 'ddg', 'title': 'Local LLM Power Consumption 2026: RTX 4090 450W = $39/mo'}
- {'url': 'https://psucheck.com/power-consumption/rtx-4090/&rut=ab908e116eadb0077a7f71bc1ac5271bd4a17bf271b414182c5da0f67fae955f', 'type': 'ddg', 'title': 'NVIDIA GeForce RTX 4090 Real-World Power Consumption'}
- {'url': 'https://www.promptquorum.com/ja/local-llms/local-llm-power-consumption&rut=bcd1669e6c7740e3a7bfb9622b3a6566d70500244d11144b817579d20c16508f', 'type': 'ddg', 'title': 'ローカルLLM電力消費2026: RTX 4090 450W = ¥5,200/月 | PromptQuorum'}
