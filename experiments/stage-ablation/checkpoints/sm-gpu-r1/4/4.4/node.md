# N21: 故障域分析：单卡方案故障率 = λ_single，多卡方案故障率 = 1 - (1 - λ_single)^N，其中 N 为卡数；假设消费级 GPU 年故障率约

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N4, N5

## Claim

故障域分析：单卡方案故障率 = λ_single，多卡方案故障率 = 1 - (1 - λ_single)^N，其中 N 为卡数；假设消费级 GPU 年故障率约为 5-10% [待核验]，数据中心级约为 1-3% [待核验]，则 2×消费卡年故障概率约为 9.75-19.5%，1×数据中心卡为 1-3%，需量化 MTBF 差异对 TCO 的影响

## Corrected Claim

故障域分析：单卡方案故障率 = λ_single，多卡方案故障率 = 1 - (1 - λ_single)^N；消费级与数据中心级GPU年故障率存在显著差异（通常消费级高于数据中心级），需根据具体硬件规格量化MTBF差异对TCO的影响。

## Evidence

[质询]具体数值（消费级5-10%，数据中心级1-3%）属于经验事实，缺乏权威来源直接支持，且不同厂商/负载下差异巨大，存在口径混淆风险。 | 故障域公式逻辑自洽，但具体故障率数值为经验事实，参考来源[1]仅涉及FMEDA方法论，未提供具体GPU故障率数据，故降级。

## Search Query

GPU failure rate MTBF consumer vs datacenter annual

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/663419419&rut=3c32dc26f1c8c38017bce860b6e9676d3601199e732ac1f676a1d8c18fef295e', 'type': 'ddg', 'title': '功能安全——硬件架构度量评估（上） - 知乎'}
