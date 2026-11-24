# N210: 接入交换机（Switch）分摊成本 = (Switch_Annualized_CapEx / N_Ports) × N_Pops，其中 Switch_Annua

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N61

## Claim

接入交换机（Switch）分摊成本 = (Switch_Annualized_CapEx / N_Ports) × N_Pops，其中 Switch_Annualized_CapEx 由 48-port 10G 交换机单价（约 ¥8,000-15,000）按 3-5 年直线折旧得出，单口分摊成本约 ¥50-100/年，远低于 N61 中假设的 ¥500/口 静态值，N61 的 ¥500 实为光模块+端口维护的综合一次性估算

## Corrected Claim

接入交换机（Switch）分摊成本 = (Switch_Annualized_CapEx / N_Ports) × N_Pops，其中 Switch_Annualized_CapEx 由 48-port 10G 交换机单价（约 ¥8,000-15,000）按 3-5 年直线折旧得出，单口分摊成本约 ¥50-100/年，远低于 N61 中假设的 ¥500/口 静态值，N61 的 ¥500 实为光模块+端口维护的综合一次性估算

## Evidence

先验知识/题面给定，逻辑校验通过：48口交换机单价¥8,000-15,000按3-5年折旧，单口年成本计算为(8000~15000)/(48*3~5) ≈ ¥55-104，与陈述中¥50-100/年量级一致，且明确区分了硬件折旧与光模块/维护综合成本，逻辑自洽。
