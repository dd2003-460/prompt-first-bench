# N374: 买家搜索成本 C_search 的基准值与信号修正：无信号时 C_search_0 为基准搜寻时间成本（如1小时*时薪），有信号时 C_search_1 = C

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N113

## Claim

买家搜索成本 C_search 的基准值与信号修正：无信号时 C_search_0 为基准搜寻时间成本（如1小时*时薪），有信号时 C_search_1 = C_search_0 * (1-k)。若 k=0.6，则 C_search_1 = 0.4 * C_search_0，成本降低60%。

## Corrected Claim

买家搜索成本 C_search 的基准值与信号修正：无信号时 C_search_0 为基准搜寻时间成本（如1小时*时薪），有信号时 C_search_1 = C_search_0 * (1-k)。若 k=0.6，则 C_search_1 = 0.4 * C_search_0，成本降低60%。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 C_search_1 = C_search_0 * (1-k) 在 k=0.6 时数学推导结果为 0.4 * C_search_0，即成本降低 60%，逻辑自洽且数值量级合理。
