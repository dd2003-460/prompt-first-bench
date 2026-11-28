# N42: 本地工作站部署 2x RTX 4090 所需的电源额定功率建议值（通常需 1200W-1600W 80+ Gold/Platinum PSU）及机箱风道对双卡散

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

本地工作站部署 2x RTX 4090 所需的电源额定功率建议值（通常需 1200W-1600W 80+ Gold/Platinum PSU）及机箱风道对双卡散热的影响，对比单卡 H100 PCIe 版对机箱空间和供电接口（8-pin vs 12VHPWR）的兼容性要求

## Corrected Claim

本地工作站部署 2x RTX 4090 建议配备 1200W-1600W 80+ Gold/Platinum 电源（如1650W ATX 3.0电源以支持双12VHPWR接口）；单卡 H100 PCIe 版通常占用更多机箱空间且需支持 16-pin (12VHPWR) 供电接口，而非传统的 8-pin 接口。

## Evidence

[质询]陈述中关于单卡H100 PCIe版供电接口为8-pin的描述存在事实错误（H100 PCIe版通常使用2个16-pin/12VHPWR接口或特定转接方案，而非传统8-pin），且参考来源仅覆盖双4090场景，未提供H100对比数据，导致后半部分缺乏外部证据支持。 | 来源[1]直接支持双4090需1650W电源及12VHPWR接口需求，符合1200W-1600W区间；但H100 PCIe版接口描述与主流硬件规格不符（通常为16-pin），且无来源支持H100对比部分，属经验事实缺来源支持。

## Retrieval Sources

- {'url': 'https://www.zhihu.com/tardis/bd/ans/3018354083&rut=b3eab964991252866b07d8ad42d57e3b8d77a2d2db137fbf581a62e903e64558', 'type': 'ddg', 'title': '双4090显卡的工作站最少得上多少w的电源? - 知乎'}
