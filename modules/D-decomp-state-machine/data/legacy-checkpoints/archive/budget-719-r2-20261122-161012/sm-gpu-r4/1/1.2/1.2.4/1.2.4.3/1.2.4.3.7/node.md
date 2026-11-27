# N368: 高端消费级主板 (如 Z790 旗舰) 的双 x16 插槽通常由 CPU 直接提供 (PCIe 5.0 x16 + x16)；需查阅具体主板手册 (Manual

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N151, N152, N153

## Claim

高端消费级主板 (如 Z790 旗舰) 的双 x16 插槽通常由 CPU 直接提供 (PCIe 5.0 x16 + x16)；需查阅具体主板手册 (Manual) 确认 'Dual x16' 模式下的实际电气规格：部分主板在插入两张卡时，会将第二张卡降为 x8 或 x4，即使物理插槽为 x16；例如 ASUS ROG STRIX Z790-E 在双卡模式下可能仅提供 x16 + x4，需通过 AIDA64 或 GPU-Z 实测链路宽度以确认是否真正支持双 x16 推理。

## Corrected Claim

高端消费级主板 (如 Z790 旗舰) 的双 x16 物理插槽通常由 CPU 直接提供 PCIe 通道；受限于 CPU 总 PCIe 通道数量，在插入两张卡时，第二张卡的电气带宽往往会降级（例如从 x16 降为 x8 或 x4）。具体降级比例（如 x16+x4 或 x16+x8）因主板设计和 CPU 型号而异，需查阅具体主板手册或通过 AIDA64/GPU-Z 实测链路宽度以确认实际可用带宽。

## Evidence

[质询]具体型号（ASUS ROG STRIX Z790-E）的双卡模式电气规格（x16+x4 vs x16+x8）属于特定硬件产品的经验事实，不同批次或BIOS版本可能存在差异，且该具体数值无法从第一性原理推导，若缺乏官方手册直接佐证，存在以偏概全或数据过时的风险。 | 逻辑自洽：高端Z790主板通常由CPU提供PCIe通道，受限于CPU总通道数（如Intel 13/14代通常提供20条PCIe 5.0通道），双x16物理插槽在双卡模式下确实常因通道不足而降级（如x16+x4或x16+x8），建议查阅手册或使用工具实测是正确且必要的工程实践。但参考来源为空，且具体型号的具体降级规格属于经验事实，无来源直接支持，故降级。

## Search Query

Z790 motherboard dual GPU PCIe lane configuration x16 x4 manual
