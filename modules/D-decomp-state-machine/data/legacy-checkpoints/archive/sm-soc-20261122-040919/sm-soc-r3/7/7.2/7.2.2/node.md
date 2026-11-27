# N370: 有信号时的搜索成本 C_search_with_signal 的量化：信号（如‘快速成交’标签）降低比较数量 n_items 和搜索时间 t_search。若信

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N112

## Claim

有信号时的搜索成本 C_search_with_signal 的量化：信号（如‘快速成交’标签）降低比较数量 n_items 和搜索时间 t_search。若信号使 n_items 从 50 降至 20，t_search 从 10 分钟降至 4 分钟，则 C_search_with_signal ≈ 4*(20/60) + 20*0.5 = 13.3元。

## Corrected Claim

若信号使 n_items 从 50 降至 20，t_search 从 10 分钟降至 4 分钟，假设时间成本为 20元/小时，单位比较成本为 0.5元/次，则 C_search_with_signal ≈ 4*(20/60) + 20*0.5 = 11.3元。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 4*(20/60) + 20*0.5 = 1.333 + 10 = 11.333，与陈述中的 13.3 存在数值偏差，但考虑到这是基于假设参数（时间成本率、单位比较成本）的示例性量化模型，且 source 为 knowledge，重点在于逻辑自洽与量级合理。然而，仔细检查计算：4分钟是 4/60 小时，若时间成本为 20元/小时，则 4/60 * 20 = 1.33元。比较成本 20 * 0.5 = 10元。总和 11.33元。陈述中写的是 13.3元。这里存在明显的算术错误。11.33 != 13.3。这是一个硬逻辑/算术错误。
