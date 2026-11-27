# N45: 噪声对买家搜索成本的传导：买家在 σ_used 较高的市场中，为降低估值不确定性，需进行更多核验（如查看历史记录），导致搜索成本 C_search 与 σ_us

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N7

## Claim

噪声对买家搜索成本的传导：买家在 σ_used 较高的市场中，为降低估值不确定性，需进行更多核验（如查看历史记录），导致搜索成本 C_search 与 σ_used² 成正比（C_search = β * σ_used² [待核验]）；高噪声迫使买家更依赖平台信号而非价格本身，间接支持了高挂价策略的可行性。

## Corrected Claim

噪声对买家搜索成本的传导：买家在 σ_used 较高的市场中，为降低估值不确定性，需进行更多核验（如查看历史记录），导致搜索成本 C_search 随 σ_used 的增加而上升（具体函数形式取决于模型假设，如线性或二次关系）；高噪声可能促使买家更依赖平台信号而非价格本身，间接支持了高挂价策略的可行性。

## Evidence

[质询]将搜索成本与噪声方差（σ²）严格成正比（C_search = β * σ_used²）缺乏微观基础支持，通常搜索成本与不确定性（标准差 σ）或信息获取难度相关，而非直接等于方差；且“高噪声迫使买家更依赖平台信号”这一因果链条在缺乏具体平台机制假设下属于推测，可能混淆了相关性与因果性。 | source=knowledge，逻辑上高噪声确实增加估值不确定性从而可能增加搜索/核验成本，但具体函数形式 C_search = β * σ_used² 为特定模型假设而非普适物理/经济定律，且无外部来源支持该具体公式，故降级为定性表述。

## Search Query

search cost information asymmetry variance value assessment
