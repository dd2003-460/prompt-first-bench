# N577: RTX 4090 双卡系统的峰值瞬时功耗（Peak Transient Power）高于持续 TDP，实测峰值可达持续功耗的 1.5-2 倍（约 1350W-1

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N241

## Claim

RTX 4090 双卡系统的峰值瞬时功耗（Peak Transient Power）高于持续 TDP，实测峰值可达持续功耗的 1.5-2 倍（约 1350W-1800W），这决定了电源选型必须基于峰值而非平均 TDP，否则会导致系统断电。

## Corrected Claim

RTX 4090 双卡系统的峰值瞬时功耗（Peak Transient Power）高于持续 TDP，实测峰值可达持续功耗的 1.5-2 倍（约 1350W-1800W），这决定了电源选型必须基于峰值而非平均 TDP，否则会导致系统断电。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 单卡 TDP 为 450W，双卡持续功耗 900W；根据 NVIDIA 官方文档及硬件工程常识，GPU 峰值瞬时功耗（Transient Power）确实可达 TDP 的 1.5-2 倍甚至更高，双卡峰值 1350W-1800W 符合物理规律与工程实测数据，电源选型需基于峰值是正确结论。
