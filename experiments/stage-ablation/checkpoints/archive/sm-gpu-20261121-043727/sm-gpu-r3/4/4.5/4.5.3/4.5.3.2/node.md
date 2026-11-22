# N201: AMD MI300X 单卡 3 年 TCO 计算：硬件成本 $15,000 [待核验] + 电力成本 (750W * 0.8 load factor * 876

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N76

## Claim

AMD MI300X 单卡 3 年 TCO 计算：硬件成本 $15,000 [待核验] + 电力成本 (750W * 0.8 load factor * 8760h * $0.1/kWh * 3 years = $1,576.8) + 维护成本 ($1,500/年 * 3 = $4,500) = 总 TCO $21,076.8，需与 2x RTX 4090 方案 TCO 对比

## Corrected Claim

AMD MI300X 单卡 3 年 TCO 估算：硬件成本约 $15,000 [需进一步核实具体采购渠道价格] + 电力成本 (750W * 0.8 load factor * 8760h * $0.1/kWh * 3 years = $1,576.8，未含 PUE) + 维护成本 ($1,500/年 * 3 = $4,500) ≈ 总 TCO $21,076.8

## Evidence

[质询]硬件成本 $15,000 为经验事实，参考来源仅提供了云租赁价格（$1.99-$3.45/GPU-hour）和二手市场链接，未提供明确的单卡硬件采购价格，无法直接验证该数值；此外，电力成本计算中未包含 PUE（电源使用效率）系数，实际数据中心电力成本通常更高。 | 逻辑推导成立（750*0.8*8760*0.1*3=1576.8），但硬件成本 $15,000 属于经验事实，来源 [2] 仅提及云租赁价格，未直接支持硬件采购价，且来源 [1][3] 为二手市场无具体价格，故降级。

## Search Query

AMD MI300X street price 2024 2025 TCO calculation data center GPU

## Retrieval Sources

- {'url': 'https://www.ebay.com/sch/i.html?_nkw=amd+instinct+mi300x&_sop=12&rut=2d01eb37c2f6ad1e3e64a79434b3721cbf71e7532156fc3456be82fa01e5e167', 'type': 'ddg', 'title': 'Amd Instinct Mi300x for sale | eBay'}
- {'url': 'https://deploybase.ai/articles/amd-mi300x-price&rut=2b8b778c2191b693eee84c29ba0348c93b5ac25b1854c1a819b9299be98c4b1d', 'type': 'ddg', 'title': 'AMD MI300X Price: Cost Guide & Availability as of March 2026'}
- {'url': 'https://www.ebay.com/sch/i.html?_nkw=mi300x+gpu&_sop=12&rut=cf219779183e11fc6ec619c7aa8b2717db3db214f75ff68353039a6859d0fb12', 'type': 'ddg', 'title': 'Mi300x GPU for sale - eBay'}
