# N108: 电源转换效率损耗系数 $\eta_{PSU}$：ATX 电源在 50%-60% 负载下效率约为 85%-90%，因此实际从电网取电功率 $P_{grid} = 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N22

## Claim

电源转换效率损耗系数 $\eta_{PSU}$：ATX 电源在 50%-60% 负载下效率约为 85%-90%，因此实际从电网取电功率 $P_{grid} = P_{GPU} / \eta_{PSU}$，需将 GPU 功耗除以 0.85-0.90 以计算真实电费 [knowledge]

## Corrected Claim

电源转换效率损耗系数 $\eta_{PSU}$：ATX 电源在 50%-60% 负载下效率约为 85%-90%，因此实际从电网取电功率 $P_{grid} = P_{GPU} / \eta_{PSU}$，需将 GPU 功耗除以 0.85-0.90 以计算真实电费 [knowledge]

## Evidence

先验知识/题面给定，逻辑校验通过
