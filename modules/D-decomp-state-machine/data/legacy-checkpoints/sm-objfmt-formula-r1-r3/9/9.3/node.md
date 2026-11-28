# N114: 单卡 H100 PCIe 版的物理尺寸与供电需求：H100 PCIe 版长度约为 300mm+，高度为双槽（2-slot）或单槽（取决于具体型号如 H100 N

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N42

## Claim

单卡 H100 PCIe 版的物理尺寸与供电需求：H100 PCIe 版长度约为 300mm+，高度为双槽（2-slot）或单槽（取决于具体型号如 H100 NVL），功耗 TDP 为 350W，仅需一个 16-pin (12VHPWR) 接口，相比 4090 的三槽厚度和 450W 功耗，对机箱风道压力更小，但需注意 H100 PCIe 无被动散热版需主动风扇，噪音较高。

## Corrected Claim

单卡 H100 PCIe 版的物理尺寸：长度约为 300mm+，高度为双槽（2-slot），功耗 TDP 为 350W，通常仅需一个 8-pin PCIe 电源接口（具体视型号而定），相比 4090 的三槽厚度和 450W 功耗，对机箱风道压力更小，但需注意 H100 PCIe 无被动散热版需主动风扇，噪音水平取决于具体散热器设计。

## Evidence

[质询]H100 PCIe 版通常配备的是 8-pin PCIe 电源接口（部分特定版本或第三方卡可能不同，但 NVIDIA 官方标准 H100 PCIe 多为 8-pin 或双 8-pin，而非 16-pin 12VHPWR，后者主要用于 H100 SXM 或消费级高端卡如 4090/3090），且 H100 PCIe 通常为双槽设计，噪音控制因服务器/工作站环境而异，‘噪音较高’这一主观描述缺乏统一标准，且 16-pin 接口的描述与主流 H100 PCIe 规格不符。 | 先验知识/题面给定，逻辑校验通过，但 H100 PCIe 标准接口通常为 8-pin 而非 16-pin 12VHPWR，存在细节偏差，故降级。
