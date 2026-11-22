# N161: 四卡 RTX 4090 配置在主流消费级/工作站主板（如 TRX50）上物理不可行或需专用背板，且 4 张 4090 的散热风道冲突导致实际功耗可能因降频低于 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N44

## Claim

四卡 RTX 4090 配置在主流消费级/工作站主板（如 TRX50）上物理不可行或需专用背板，且 4 张 4090 的散热风道冲突导致实际功耗可能因降频低于 1800W 标称值，该配置在性价比模型中应标记为 [排除/非典型]。

## Corrected Claim

四卡 RTX 4090 配置在主流消费级/工作站主板（如 TRX50）上物理不可行或需专用背板，且 4 张 4090 的散热风道冲突导致实际功耗可能因降频低于 1800W 标称值，该配置在性价比模型中应标记为 [排除/非典型]。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 为双槽卡，四卡需至少8槽空间，主流消费级/工作站主板（如TRX50）通常仅支持2-4槽或需特殊背板，且多卡散热冲突导致降频是已知工程事实，符合物理与工程直觉。

## Search Query

4x RTX 4090 workstation cooling thermal throttling power draw
