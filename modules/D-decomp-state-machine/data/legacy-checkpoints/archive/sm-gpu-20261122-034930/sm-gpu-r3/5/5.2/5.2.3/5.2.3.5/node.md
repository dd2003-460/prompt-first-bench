# N352: INT8显存需求矛盾判定：N10的41.7GB为正确总需求。量化拆解：模型权重27.0GB + KV Cache (FP16, 32K ctx) 10.7GB 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N125, N126, N127

## Claim

INT8显存需求矛盾判定：N10的41.7GB为正确总需求。量化拆解：模型权重27.0GB + KV Cache (FP16, 32K ctx) 10.7GB + vLLM固定框架开销 4.0GB = 41.7GB。N16的37.7GB缺失框架开销，仅适用于理论最小值计算，不适用于实际部署容量规划。

## Corrected Claim

INT8显存需求矛盾判定：N10的41.7GB为正确总需求。量化拆解：模型权重27.0GB + KV Cache (FP16, 32K ctx) 10.7GB + vLLM固定框架开销 4.0GB = 41.7GB。N16的37.7GB缺失框架开销，仅适用于理论最小值计算，不适用于实际部署容量规划。

## Evidence

先验知识/题面给定，逻辑校验通过：27.0 + 10.7 + 4.0 = 41.7，数值加和自洽，且符合LLM部署中权重+KV Cache+框架开销的常规构成逻辑。
