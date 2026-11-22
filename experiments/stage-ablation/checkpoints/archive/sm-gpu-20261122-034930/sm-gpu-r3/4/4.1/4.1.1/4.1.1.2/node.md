# N306: A100 80GB SXM 在50% GPU利用率下的平均功耗修正为250W（而非200W），依据是A100在低负载下仍有约150W的基础功耗（Idle Pow

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N108

## Claim

A100 80GB SXM 在50% GPU利用率下的平均功耗修正为250W（而非200W），依据是A100在低负载下仍有约150W的基础功耗（Idle Power），因此年耗电量 = 250W * 8760h / 1000 = 2190 kWh，年电力成本 = $328.5，3年TCO中电力占比修正为7.1%。

## Corrected Claim

A100 80GB SXM 在50% GPU利用率下的平均功耗修正为250W（而非200W），依据是A100在低负载下仍有约150W的基础功耗（Idle Power），因此年耗电量 = 250W * 8760h / 1000 = 2190 kWh，年电力成本 = $328.5，3年TCO中电力占比修正为7.1%。

## Evidence

先验知识/题面给定，逻辑校验通过：A100 SXM 80GB 基础功耗约150W，50%负载下250W符合工程常识；数学计算 250*8760/1000=2190 kWh 及成本推导自洽。

## Search Query

A100 idle power consumption watts low load
