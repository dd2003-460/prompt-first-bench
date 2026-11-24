# N212: 工作点B（中性价比/标准密度）：采用双路 32核 CPU + 256GB RAM + 2TB NVMe 配置，初始硬件成本 C_init = ¥25,000；5

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N67

## Claim

工作点B（中性价比/标准密度）：采用双路 32核 CPU + 256GB RAM + 2TB NVMe 配置，初始硬件成本 C_init = ¥25,000；5年直线折旧后 C_hardware_depreciation = ¥416.67/月；功耗 P_avg = 450W，电价 ¥0.8/kWh，PUE 1.4，C_power = 450/1000 * 24 * 30 * 0.8 * 1.4 = ¥453.60/月；二线城市机柜分摊租金 C_colocation = ¥800/月；总 C_server = ¥1,670.27/月。

## Corrected Claim

工作点B（中性价比/标准密度）：采用双路 32核 CPU + 256GB RAM + 2TB NVMe 配置，初始硬件成本 C_init = ¥25,000；5年直线折旧后 C_hardware_depreciation = ¥416.67/月；功耗 P_avg = 450W，电价 ¥0.8/kWh，PUE 1.4，C_power = 450/1000 * 24 * 30 * 0.8 * 1.4 = ¥453.60/月；二线城市机柜分摊租金 C_colocation = ¥800/月；总 C_server = ¥1,670.27/月。

## Evidence

父节点级核验未通过：不完备（子节点在主题上正交（分别关注性能/单位成本、电力敏感性、租金逻辑），无重复或矛盾。但完备性不足：父节点明确包含‘初始硬件成本’及‘折旧’（C_hardware_depreciation），这是总成本的重要组成部分，但三个子节点均未涉及硬件折旧或初始投资的摊销逻辑，导致对父节点成本构成的覆盖不全。）

## Search Query

mid-range server cost 32 core 256GB RAM price
