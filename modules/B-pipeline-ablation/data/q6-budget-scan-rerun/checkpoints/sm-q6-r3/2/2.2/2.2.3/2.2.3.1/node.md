# N193: 跨地域回源比例量化：Cross_Region_Ratio = 1 - P_Origin_Local，其中P_Origin_Local为源站所在区域与用户请求源地

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N62

## Claim

跨地域回源比例量化：Cross_Region_Ratio = 1 - P_Origin_Local，其中P_Origin_Local为源站所在区域与用户请求源地的地理重合度，若源站位于北京且用户Top-3省份（京沪粤）占比60%，且北京源站可无跨域覆盖京沪，则Cross_Region_Ratio ≈ 40%（需基于N137 HHI修正）

## Corrected Claim

跨地域回源比例量化：Cross_Region_Ratio = 1 - P_Origin_Local，其中P_Origin_Local为源站所在区域与用户请求源地的地理重合度，若源站位于北京且用户Top-3省份（京沪粤）占比60%，且北京源站可无跨域覆盖京沪，则Cross_Region_Ratio ≈ 40%（需基于N137 HHI修正）

## Evidence

先验知识/题面给定，逻辑校验通过：基于定义 Cross_Region_Ratio = 1 - P_Origin_Local，若北京源站覆盖京沪（假设覆盖Top-3中的京、沪，即60%中的大部分或全部，题目设定为无跨域覆盖京沪，意味着京沪请求不产生跨域回源，剩余40%为粤及其他，产生跨域回源），则比例为40%，逻辑自洽。
