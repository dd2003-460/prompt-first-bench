# N582: H100 SXM 单卡边际成本中，SXM 转接/基板费用并非固定 $2k-$5k，而是取决于是否复用现有 HGX 基板；若从零开始构建单卡 SXM 平台，需购买

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N243

## Claim

H100 SXM 单卡边际成本中，SXM 转接/基板费用并非固定 $2k-$5k，而是取决于是否复用现有 HGX 基板；若从零开始构建单卡 SXM 平台，需购买 SXM 转 PCIe 的专用基板或专用 SXM 冷板，成本约为 $3k-$8k（含液冷循环泵和管路），此费用在 N243 中被低估。

## Corrected Claim

H100 SXM 单卡边际成本中，SXM 转接/基板费用并非固定值，而是取决于是否复用现有 HGX 基板；若从零开始构建单卡 SXM 平台，需购买专用基板或液冷组件，成本显著高于复用场景，具体金额需根据实际供应链报价确定，原陈述中的 $3k-$8k 仅为估算区间。

## Evidence

[质询]具体数值区间（$3k-$8k）属于经验事实，缺乏公开市场数据或官方BOM支持，且‘从零构建单卡SXM平台’的定义模糊，可能混淆了标准HGX基板成本与定制液冷集成成本。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）

## Search Query

H100 SXM to PCIe adapter board cost 2024
