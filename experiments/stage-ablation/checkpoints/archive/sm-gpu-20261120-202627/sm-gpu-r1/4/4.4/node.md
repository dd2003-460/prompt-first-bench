# N24: 多卡互联开销量化：双卡 NVLink 方案相比双卡 PCIe 方案，硬件成本增加约 100-300 美元（NVLink 桥接器/线缆），但 PCIe 方案在多卡

- **status**: degraded
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N4

## Claim

多卡互联开销量化：双卡 NVLink 方案相比双卡 PCIe 方案，硬件成本增加约 100-300 美元（NVLink 桥接器/线缆），但 PCIe 方案在多卡张量并行时通信带宽瓶颈导致有效吞吐量下降约 10-20% [待核验]，需折算为等效性能损失后的隐性 TCO 增加。

## Corrected Claim

多卡互联开销量化：双卡 NVLink 方案相比双卡 PCIe 方案，硬件成本通常增加数十至数百美元（取决于具体桥接器型号），但在高通信频率的多卡张量并行场景下，PCIe 带宽瓶颈可能导致有效吞吐量出现显著下降（具体幅度视模型与并行策略而定，常见报告范围在 10%-20% 或更高），需结合具体业务场景折算隐性 TCO。

## Evidence

[质询]数值量级与具体场景强相关：'10-20%吞吐量下降'和'100-300美元成本'是高度依赖模型规模、并行策略（TP/PP）及具体硬件代际的经验数据，缺乏通用性，且不同文献中波动较大，直接作为固定事实陈述存在以偏概全的风险。 | 先验知识/题面给定，逻辑校验通过（NVLink带宽显著高于PCIe，成本差异符合硬件市场常识），但具体百分比和金额属于经验事实，无外部来源直接支持，故降级。

## Search Query

NVLink vs PCIe multi-GPU inference throughput penalty cost difference
