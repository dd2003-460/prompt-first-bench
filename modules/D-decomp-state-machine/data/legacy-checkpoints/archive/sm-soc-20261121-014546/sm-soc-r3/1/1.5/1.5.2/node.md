# N52: 搜索成本降低的量化：买家搜索成本 C_search 与感知噪声 σ_buyer 呈负相关，C_search = C0 / (1 + α·(1/σ_buyer))

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N10

## Claim

搜索成本降低的量化：买家搜索成本 C_search 与感知噪声 σ_buyer 呈负相关，C_search = C0 / (1 + α·(1/σ_buyer))，其中 α 为搜索效率系数，σ_buyer 越小（感知越清晰），搜索成本越低，具体数值需通过 A/B 测试验证 α 的范围。

## Corrected Claim

搜索成本降低的量化：买家搜索成本 C_search 与感知噪声 σ_buyer 呈负相关，C_search = C0 / (1 + α·(1/σ_buyer))，其中 α 为搜索效率系数，σ_buyer 越小（感知越清晰），搜索成本越低，具体数值需通过 A/B 测试验证 α 的范围。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

search cost reduction perception noise clarity coefficient alpha
