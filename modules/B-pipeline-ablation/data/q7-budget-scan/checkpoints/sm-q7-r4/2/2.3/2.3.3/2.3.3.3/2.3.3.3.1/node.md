# N597: 小对象合并策略中，将 <128KB 对象合并为 1MB 块，对象数减少比例 R_obj = 1 - (128KB / 1MB) = 87.5%，新对象数 N_o

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N212

## Claim

小对象合并策略中，将 <128KB 对象合并为 1MB 块，对象数减少比例 R_obj = 1 - (128KB / 1MB) = 87.5%，新对象数 N_obj_new = N_obj_old / 8

## Corrected Claim

小对象合并策略中，将 <128KB 对象合并为 1MB 块，对象数减少比例 R_obj = 1 - (128KB / 1MB) = 87.5%，新对象数 N_obj_new = N_obj_old / 8

## Evidence

先验知识/题面给定，逻辑校验通过：128KB/1MB = 0.125，1-0.125=0.875，N_new=N_old*(1-0.875)=N_old/8，计算无误
