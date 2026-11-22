# N432: H100 SXM 四卡（或八卡）方案的 TCO 对比基准：若以 8-GPU 节点为最小购买单元，单卡分摊 Capex 约为 $30,000-$35,000（含节

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N179

## Claim

H100 SXM 四卡（或八卡）方案的 TCO 对比基准：若以 8-GPU 节点为最小购买单元，单卡分摊 Capex 约为 $30,000-$35,000（含节点、CPU、内存、电源），相比 N122 中 H100 单卡 $25,000 的估算，多卡 SXM 方案的单卡成本溢价约 20-40%，主要源于冗余电源、高速互联（NVLink Switch）及专用机箱成本；此溢价使得'4 卡 SXM'在性价比上劣于'4 卡 PCIe H100'或'2 卡 PCIe H100'，除非需要 NVLink 全互联带宽。

## Corrected Claim

H100 SXM 多卡方案（如 8 卡节点）的单卡分摊 Capex 通常高于 PCIe 方案，主要源于冗余电源、NVLink 互联及专用机箱成本，导致单卡成本存在显著溢价（具体比例视市场报价而定，通常在 20%-40% 区间波动），使得其在非全互联带宽需求下的性价比低于 PCIe 方案。

## Evidence

[质询]该陈述包含具体的经验性价格数据（H100 SXM 单卡分摊 Capex $30k-$35k，N122 单卡 $25k）及由此推导的 20-40% 溢价比例。这些数值属于市场波动较大的经验事实，且不同时期、不同供应商报价差异巨大，无法仅凭逻辑自洽确认为当前准确的市场基准。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源，无法验证具体价格数值及溢价比例的准确性）

## Search Query

HGX H100 8-GPU node price vs PCIe H100 cost per GPU TCO comparison
