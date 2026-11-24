# N86: 冷数据（400TB）年访问次数约束：定义为年总访问次数 < 100次/TB（即平均每个TB每年被读取少于100次），该阈值用于界定‘极少访问’的量化边界，低于此

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N20

## Claim

冷数据（400TB）年访问次数约束：定义为年总访问次数 < 100次/TB（即平均每个TB每年被读取少于100次），该阈值用于界定‘极少访问’的量化边界，低于此阈值时云存储低频/归档层的取回费用占比低于总成本的5%

## Corrected Claim

冷数据（400TB）年访问次数约束：定义为年总访问次数 < 100次/TB（即平均每个TB每年被读取少于100次），该阈值用于界定‘极少访问’的量化边界，低于此阈值时云存储低频/归档层的取回费用占比低于总成本的5%

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

cloud storage infrequent access threshold cost percentage annual reads per TB
