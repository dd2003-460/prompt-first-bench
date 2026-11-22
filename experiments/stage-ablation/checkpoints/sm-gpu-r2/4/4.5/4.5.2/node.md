# N125: TCO电力成本计算需引入电源效率因子η（通常ATX 80+ Gold为0.85-0.90），实际电网输入功率 P_grid = P_GPU_TDP / η。例如

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N25, N26, N27

## Claim

TCO电力成本计算需引入电源效率因子η（通常ATX 80+ Gold为0.85-0.90），实际电网输入功率 P_grid = P_GPU_TDP / η。例如RTX 4090 TDP 450W，η=0.85时，实际耗电约为529W，年电费按0.1$/kWh计算为 $462/年，而非基于TDP直接计算的$394/年。

## Corrected Claim

TCO电力成本计算需引入电源效率因子η（通常ATX 80+ Gold为0.85-0.90），实际电网输入功率 P_grid = P_GPU_TDP / η。例如RTX 4090 TDP 450W，η=0.85时，实际耗电约为529W，年电费按0.1$/kWh计算为 $462/年，而非基于TDP直接计算的$394/年。

## Evidence

先验知识/题面给定，逻辑校验通过：450W/0.85≈529W，529W*24h*365d/1000*0.1$≈$462，计算无误且符合物理直觉

## Search Query

80 plus gold power supply efficiency factor calculation actual power consumption vs TDP
