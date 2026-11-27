# N307: 2×RTX 3090 方案的 OpEx_energy 修正：RTX 3090 TDP 为 350W，2 卡总功耗 700W，与 N83 中 4090 方案相同，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N84

## Claim

2×RTX 3090 方案的 OpEx_energy 修正：RTX 3090 TDP 为 350W，2 卡总功耗 700W，与 N83 中 4090 方案相同，但 3090 能效比（Tokens/Joule）通常低于 4090，需结合吞吐量差异计算单位能耗成本；电价参数同 N152 需修正。

## Corrected Claim

2×RTX 3090 方案的 OpEx_energy 修正：RTX 3090 TDP 为 350W，2 卡总功耗 700W，与 N83 中 4090 方案相同，但 3090 能效比（Tokens/Joule）通常低于 4090，需结合吞吐量差异计算单位能耗成本；电价参数同 N152 需修正。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 3090 TDP 350W 及 2 卡 700W 总功耗符合硬件规格常识，能效比低于 4090 符合架构代际差异逻辑，无内部矛盾。
