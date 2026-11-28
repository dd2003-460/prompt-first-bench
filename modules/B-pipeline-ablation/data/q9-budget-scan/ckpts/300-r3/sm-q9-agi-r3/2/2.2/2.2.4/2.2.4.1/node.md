# N198: 无效实验定义量化：Invalid_Exp = {e | Data_Unavailable(e) OR FLOPs(e) > 2.3e17 OR Ethics_V

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N58

## Claim

无效实验定义量化：Invalid_Exp = {e | Data_Unavailable(e) OR FLOPs(e) > 2.3e17 OR Ethics_Violation(e)}，拦截率 IR = |Intercepted_Invalid| / |Total_Invalid_Generated| * 100%，目标 IR > 80%

## Corrected Claim

无效实验定义量化：Invalid_Exp = {e | Data_Unavailable(e) OR FLOPs(e) > 2.3e17 OR Ethics_Violation(e)}，拦截率 IR = |Intercepted_Invalid| / |Total_Invalid_Generated| * 100%，目标 IR > 80%

## Evidence

先验知识/题面给定，逻辑校验通过
