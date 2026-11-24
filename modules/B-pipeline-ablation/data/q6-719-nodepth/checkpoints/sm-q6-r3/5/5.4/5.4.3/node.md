# N115: 5k元/月/POP 的风险溢价估算隐含假设：单POP故障或政策限制导致的月均业务损失为50k元（即 P_pop_shutdown × 50k = 5k，若 P=

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N30, N31, N32

## Claim

5k元/月/POP 的风险溢价估算隐含假设：单POP故障或政策限制导致的月均业务损失为50k元（即 P_pop_shutdown × 50k = 5k，若 P=10% 则单POP月损失50k；若 P=1% 则单POP月损失500k），需验证该损失值是否与平台实际营收匹配

## Corrected Claim

5k元/月/POP 的风险溢价估算隐含假设：单POP故障或政策限制导致的月均业务损失为50k元（即 P_pop_shutdown × 50k = 5k，若 P=10% 则单POP月损失50k；若 P=1% 则单POP月损失500k），需验证该损失值是否与平台实际营收匹配

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点1负责确定基准营收参数（ARPU及单POP营收），子节点2负责基于该参数进行匹配度逻辑检验和场景分类。两者分别处理‘数据基础’和‘逻辑验证’，职责清晰，无重复或矛盾。）

## Search Query

edge node failure business loss estimation methodology
