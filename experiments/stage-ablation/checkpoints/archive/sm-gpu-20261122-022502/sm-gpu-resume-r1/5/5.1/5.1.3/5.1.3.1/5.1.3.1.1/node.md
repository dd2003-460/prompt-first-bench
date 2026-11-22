# N854: Mac Studio M2 Ultra 在持续 100% 负载（如 LLM 推理）下的实际稳态功耗并非固定的 365W，而是随负载类型波动；实测数据显示其最大功

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N266, N267, N268

## Claim

Mac Studio M2 Ultra 在持续 100% 负载（如 LLM 推理）下的实际稳态功耗并非固定的 365W，而是随负载类型波动；实测数据显示其最大功耗限制（Power Limit）约为 200W-250W（取决于具体配置和散热），365W 可能是峰值或误读，需修正为 [待核验: 实测稳态功耗 W]。

## Corrected Claim

Mac Studio M2 Ultra 的 365W 通常指电源适配器的最大输出功率，而非芯片或整机的稳态功耗；其实际稳态功耗随负载波动，最大功耗限制（Power Limit）远低于 365W，具体数值需依据实测数据修正。

## Evidence

[质询]365W 通常指 Mac Studio 电源适配器的最大输出功率，而非芯片或整机的稳态功耗上限；将适配器功率误读为芯片功耗限制是常见的口径混淆，且 M2 Ultra 的 TDP 远低于此值。 | 经验事实，逻辑自洽但缺来源支持（检索失败，无法外部核验具体数值，但 365W 为适配器功率而非芯片稳态功耗的逻辑判断成立）

## Search Query

Mac Studio M2 Ultra sustained power consumption under load W
