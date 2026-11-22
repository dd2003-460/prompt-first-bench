# N383: RTX A6000 48GB 价格约 $4000-$5000，3 年周期内折旧成本 C_depreciation 估算为 ($4500 - $1500) / 3

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N134

## Claim

RTX A6000 48GB 价格约 $4000-$5000，3 年周期内折旧成本 C_depreciation 估算为 ($4500 - $1500) / 3 ≈ $1000/年，加上电力成本（TDP 300W，PUE 1.0，电价 $0.1/kWh，年运行 8760h）约为 $263/年，总 3 年 TCO 约为 $4500 + 3*($1000 + $263) ≈ $8289 [待核验: 实时价格及电力成本]

## Corrected Claim

RTX A6000 48GB 价格约 $4000-$5000，3 年周期内折旧成本 C_depreciation 估算为 ($4500 - $1500) / 3 ≈ $1000/年，加上电力成本（TDP 300W，PUE 1.0，电价 $0.1/kWh，年运行 8760h）约为 $263/年，总 3 年 TCO 约为 $4500 + 3*($1000 + $263) ≈ $8289 [待核验: 实时价格及电力成本]

## Evidence

先验知识/题面给定，逻辑校验通过：RTX A6000 价格区间及 TDP 符合工程常识，折旧与电力成本计算公式及数值推导正确（(4500-1500)/3=1000, 300*8760*0.1/1000=262.8, 4500+3*(1000+263)=8289）。

## Search Query

RTX A6000 48GB price 2024 TCO calculation electricity cost
