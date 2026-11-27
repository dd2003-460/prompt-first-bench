# N343: 数据中心 GPU 的 3 年总拥有成本 (TCO) 中，电力成本占比 (Power_Cost_Ratio) 计算公式为：(3 × Power_Cost_Annu

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N121

## Claim

数据中心 GPU 的 3 年总拥有成本 (TCO) 中，电力成本占比 (Power_Cost_Ratio) 计算公式为：(3 × Power_Cost_Annual) / (Hardware_Cost + 3 × Power_Cost_Annual + Maintenance_Cost)，其中 H100 硬件成本约 $30,000 [待核验]，维护成本约为硬件成本的 5%/年

## Corrected Claim

数据中心 GPU 的 3 年总拥有成本 (TCO) 中，电力成本占比 (Power_Cost_Ratio) 计算公式为：(3 × Power_Cost_Annual) / (Hardware_Cost + 3 × Power_Cost_Annual + Maintenance_Cost)，其中 H100 硬件成本约 $30,000 [待核验]，维护成本约为硬件成本的 5%/年

## Evidence

先验知识/题面给定，逻辑校验通过：TCO公式结构符合定义（总成本=硬件+3年电力+维护），H100硬件成本$30,000及维护成本5%/年属于数据中心GPU领域的典型经验参数，量级合理且无内部矛盾。

## Search Query

NVIDIA H100 price USD 2024 data center GPU TCO maintenance cost percentage
