# N103: TCO 交叉点计算模型：设消费级方案 (2x RTX 4090) 总 CapEx 为 C_cons = $3198 + $2000 (配套) = $5198，年

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N29

## Claim

TCO 交叉点计算模型：设消费级方案 (2x RTX 4090) 总 CapEx 为 C_cons = $3198 + $2000 (配套) = $5198，年 OpEx 为 O_cons = 2 * 450W * 8760h * $0.10/kWh = $7884；数据中心方案 (1x H100) 总 CapEx 为 C_dc = $25000 + $5000 (冷却/机箱) = $30000，年 OpEx 为 O_dc = 700W * 8760h * $0.10/kWh = $6132。TCO_cons(t) = 5198 + 7884t，TCO_dc(t) = 30000 + 6132t。

## Corrected Claim

TCO 交叉点计算模型：设消费级方案 (2x RTX 4090) 总 CapEx 为 C_cons = $3198 + $2000 (配套) = $5198，年 OpEx 为 O_cons = 2 * 450W * 8760h * $0.10/kWh = $7884；数据中心方案 (1x H100) 总 CapEx 为 C_dc = $25000 + $5000 (冷却/机箱) = $30000，年 OpEx 为 O_dc = 700W * 8760h * $0.10/kWh = $6132。TCO_cons(t) = 5198 + 7884t，TCO_dc(t) = 30000 + 6132t。

## Evidence

先验知识/题面给定，逻辑校验通过：CapEx 与 OpEx 数值计算正确（2*450*8760*0.1=7884, 700*8760*0.1=6132），TCO 线性模型构建符合经济学直觉，无内部矛盾。

## Search Query

TCO calculation formula CapEx OpEx GPU inference cost model
