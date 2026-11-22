# N195: 内存功耗具体值：64GB DDR5-6000在LLM推理负载下平均功耗约30-40W（双通道），96GB DDR5-5600约35-45W，内存容量和频率对功耗

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N63

## Claim

内存功耗具体值：64GB DDR5-6000在LLM推理负载下平均功耗约30-40W（双通道），96GB DDR5-5600约35-45W，内存容量和频率对功耗影响约±5W，需根据具体内存配置确定

## Corrected Claim

64GB DDR5-6000在LLM推理负载下平均功耗通常在数十瓦量级（具体数值依配置而异），96GB DDR5-5600功耗略高，内存容量和频率对功耗有显著影响，需根据具体内存配置和实测数据确定。

## Evidence

[质询]具体功耗数值（30-40W/35-45W）属于经验事实，受内存颗粒品牌、电压设置（VDD/VDDQ）、主板供电效率及具体负载模式影响极大，缺乏统一标准，且无来源支持具体数值区间。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

DDR5 64GB 96GB power consumption LLM inference workload measured watts
