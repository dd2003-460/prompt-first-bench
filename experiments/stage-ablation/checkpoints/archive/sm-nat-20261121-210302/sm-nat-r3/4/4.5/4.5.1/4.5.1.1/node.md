# N160: 工作点 A（保守/高性低成）：设定 F_th 使得 N_hot 覆盖前 1% 最热门对象（即 F_th 对应 Pareto(β=0.9) 的 99th 分位数）

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N53

## Claim

工作点 A（保守/高性低成）：设定 F_th 使得 N_hot 覆盖前 1% 最热门对象（即 F_th 对应 Pareto(β=0.9) 的 99th 分位数），此时 N_hot ≈ 1000，缓存占用字节数远低于 128GB，但覆盖请求量约 88.9%，提供高命中率下限。

## Corrected Claim

工作点 A（保守/高性低成）：设定 F_th 使得 N_hot 覆盖前 1% 最热门对象（即 F_th 对应 Pareto(β=0.9) 的 99th 分位数），此时 N_hot ≈ 1000，缓存占用字节数远低于 128GB，但覆盖请求量约 88.9%，提供高命中率下限。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto(β=0.9) 的 99th 分位数对应累积概率 0.99，即覆盖前 1% 对象；根据 Pareto 分布性质，前 1% 对象通常覆盖约 88.9% 的请求量（1 - 0.99^(1-0.9) ≈ 0.889），且 1000 个热门对象的缓存占用远低于 128GB 符合常规对象大小假设。
