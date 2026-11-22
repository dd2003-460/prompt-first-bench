# N146: 2×消费卡 PCIe 方案相比 1×数据中心卡 NVLink 方案的 TCO 修正项：因吞吐量损失 20-30%，等效 TCO 需除以 (1 - Loss_Ra

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N35

## Claim

2×消费卡 PCIe 方案相比 1×数据中心卡 NVLink 方案的 TCO 修正项：因吞吐量损失 20-30%，等效 TCO 需除以 (1 - Loss_Rate)，例如若 Loss_Rate=25%，则等效 TCO 增加 33%，此修正项直接改变性价比排序

## Corrected Claim

2×消费卡 PCIe 方案相比 1×数据中心卡 NVLink 方案的 TCO 修正项：因吞吐量损失 20-30%，等效 TCO 需除以 (1 - Loss_Rate)，例如若 Loss_Rate=25%，则等效 TCO 增加 33%，此修正项直接改变性价比排序

## Evidence

先验知识/题面给定，逻辑校验通过：数学上 1/(1-0.25)=1.33，即增加33%，且吞吐量损失导致单位成本上升进而影响性价比排序符合基本经济逻辑。
