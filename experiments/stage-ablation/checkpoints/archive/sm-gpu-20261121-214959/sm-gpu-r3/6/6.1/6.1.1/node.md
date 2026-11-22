# N103: TCO 交叉点计算模型：设消费级方案 (2x RTX 4090) 总 CapEx 为 C_cons = $3198 + $2000 (配套) = $5198，年

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N29

## Claim

TCO 交叉点计算模型：设消费级方案 (2x RTX 4090) 总 CapEx 为 C_cons = $3198 + $2000 (配套) = $5198，年 OpEx 为 O_cons = 2 * 450W * 8760h * $0.10/kWh = $7884；数据中心方案 (1x H100) 总 CapEx 为 C_dc = $25000 + $5000 (冷却/机箱) = $30000，年 OpEx 为 O_dc = 700W * 8760h * $0.10/kWh = $6132。TCO_cons(t) = 5198 + 7884t，TCO_dc(t) = 30000 + 6132t。

## Corrected Claim

TCO 交叉点计算模型：设消费级方案 (2x RTX 4090) 总 CapEx 为 C_cons = $3198 + $2000 (配套) = $5198，年 OpEx 为 O_cons = 2 * 450W * 8760h * $0.10/kWh = $7884；数据中心方案 (1x H100) 总 CapEx 为 C_dc = $25000 + $5000 (冷却/机箱) = $30000，年 OpEx 为 O_dc = 700W * 8760h * $0.10/kWh = $6132。TCO_cons(t) = 5198 + 7884t，TCO_dc(t) = 30000 + 6132t。

## Evidence

父节点级核验失败（LLM 错误）：Unterminated string starting at: line 9 column 5 (char 492)

## Search Query

TCO calculation formula CapEx OpEx GPU inference cost model
