# N188: 数据可用性判定的二元逻辑函数 Avail(Data) = 1 if (HTTP_Status == 200 AND Record_Count > 0 AND S

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N55

## Claim

数据可用性判定的二元逻辑函数 Avail(Data) = 1 if (HTTP_Status == 200 AND Record_Count > 0 AND Schema_Match == True) else 0；其中 Schema_Match 通过 JSON Schema Validator 校验字段类型与必填项，校验耗时 < 5ms（CPU侧），若任一条件为 False，标记为不可用

## Corrected Claim

数据可用性判定的二元逻辑函数 Avail(Data) = 1 if (HTTP_Status == 200 AND Record_Count > 0 AND Schema_Match == True) else 0；其中 Schema_Match 通过 JSON Schema Validator 校验字段类型与必填项，校验耗时 < 5ms（CPU侧），若任一条件为 False，标记为不可用

## Evidence

先验知识/题面给定，逻辑校验通过
