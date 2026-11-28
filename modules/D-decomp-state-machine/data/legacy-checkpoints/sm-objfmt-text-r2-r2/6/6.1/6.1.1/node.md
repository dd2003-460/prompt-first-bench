# N98: 风冷数据中心 GPU 的基础设施额外成本主要来自 PSU 效率损失与噪音处理，其增量成本占比约为 3-5% [待核验]，远低于液冷的 10-15%；具体计算需引

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N31

## Claim

风冷数据中心 GPU 的基础设施额外成本主要来自 PSU 效率损失与噪音处理，其增量成本占比约为 3-5% [待核验]，远低于液冷的 10-15%；具体计算需引入电源转换效率 η_psu (通常 0.90-0.95) 和噪音治理费用 F_noise。

## Corrected Claim

风冷数据中心 GPU 的基础设施额外成本主要来自 PSU 效率损失与噪音处理，其增量成本通常低于液冷方案；具体量化需结合电源转换效率 η_psu 和噪音治理费用 F_noise 进行个案计算。

## Evidence

[质询]具体数值（3-5% vs 10-15%）及PSU效率范围（0.90-0.95）属于经验性工程估算，缺乏通用标准支持，且不同负载率、PUE目标下波动较大，易产生口径混淆。 | 来源[1]仅定性讨论风冷与液冷的TCO逻辑及散热对架构的影响，未提供具体的成本占比数值或PSU效率参数，无法直接支持具体数值；但逻辑上风冷基础设施额外成本低于液冷符合常识，故降级为定性表述。

## Search Query

data center GPU air cooling infrastructure cost overhead percentage

## Retrieval Sources

- {'url': 'https://www.toutiao.com/article/7555512387521004066/&rut=f69cee9ed2db6869fdd1b29e685c1c0e4ff6e0eddb1e11ac066ae81d20488562', 'type': 'ddg', 'title': 'AI数据中心的"用电与散热"逻辑：从风冷到液冷，谁在决定TCO？'}
