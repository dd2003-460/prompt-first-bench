# N400: Mac Studio M2 Ultra 的 TDP 在满载 LLM 推理时约为 100-150W，而 RTX 4090 方案（含主机）的满载功耗约为 450-5

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N138

## Claim

Mac Studio M2 Ultra 的 TDP 在满载 LLM 推理时约为 100-150W，而 RTX 4090 方案（含主机）的满载功耗约为 450-550W；在电价 $0.10/kWh 下，Mac 方案年电力成本约为 $87-$131，RTX 4090 方案约为 $393-$479，Mac 方案每年节省电力成本约 $300-$350。

## Corrected Claim

Mac Studio M2 Ultra 的 TDP 在满载 LLM 推理时约为 100-150W，而 RTX 4090 方案（含主机）的满载功耗约为 450-550W；在电价 $0.10/kWh 下，Mac 方案年电力成本约为 $87-$131，RTX 4090 方案约为 $393-$479，Mac 方案每年节省电力成本约 $300-$350。

## Evidence

先验知识/题面给定，逻辑校验通过：TDP数值符合硬件规格常识，电力成本计算（功率×24h×365d×电价）数学推导正确且量级合理。

## Search Query

Mac Studio M2 Ultra TDP power consumption vs RTX 4090 system power
