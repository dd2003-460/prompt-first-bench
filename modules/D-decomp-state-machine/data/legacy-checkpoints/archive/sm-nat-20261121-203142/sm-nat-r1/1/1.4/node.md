# N9: 128GB 缓存容量相对于 10 万对象总数据量（N_total × E[S]）的缓存覆盖率 C = 128GB / (N_total × E[S])，该比值决

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

128GB 缓存容量相对于 10 万对象总数据量（N_total × E[S]）的缓存覆盖率 C = 128GB / (N_total × E[S])，该比值决定缓存可容纳的对象数量上限及工作集大小

## Corrected Claim

128GB 缓存容量相对于 10 万对象总数据量（N_total × E[S]）的缓存覆盖率 C = 128GB / (N_total × E[S])，该比值决定缓存可容纳的对象数量上限及工作集大小

## Evidence

先验知识/题面给定，逻辑校验通过：缓存覆盖率定义为缓存容量与总数据量之比，量纲一致（GB/GB），逻辑自洽。
