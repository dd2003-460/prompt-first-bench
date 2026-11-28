# N71: GPU满载推理时的稳态功耗基准值：RTX 4090 TDP为450W，RTX 5090 TDP预计为575W [时效待核]，H100 PCIe TDP为700W

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N14

## Claim

GPU满载推理时的稳态功耗基准值：RTX 4090 TDP为450W，RTX 5090 TDP预计为575W [时效待核]，H100 PCIe TDP为700W，H200 PCIe TDP为700W，Mac Studio M3 Ultra整机峰值功耗约1200W [待核验H100/H200具体SKU功耗及Mac Studio实测数据]

## Corrected Claim

GPU满载推理时的稳态功耗基准值：RTX 4090 TDP为450W，RTX 5090 TDP预计为575W（待官方确认），H100 SXM TDP为700W（PCIe版通常为350W-500W，需指定SKU），H200 SXM TDP为700W（PCIe版类似），Mac Studio M3 Ultra整机峰值功耗约1200W（稳态功耗较低，需区分峰值与稳态）

## Evidence

[质询]RTX 5090 TDP 575W 为预测值而非官方确认值，且 H100/H200 PCIe 版本 TDP 通常标注为 350W 或 700W（取决于具体 SKU 和散热设计，SXM 版为 700W，PCIe 版常为 350W 或 500W+），此处笼统标为 700W 可能存在口径混淆；Mac Studio M3 Ultra 峰值功耗 1200W 亦需区分整机峰值与持续稳态功耗。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且部分数值如 RTX 5090 为预测值，H100/H200 PCIe TDP 存在 SKU 差异风险）

## Search Query

RTX 4090 5090 H100 H200 TDP watts Mac Studio M3 Ultra power consumption
