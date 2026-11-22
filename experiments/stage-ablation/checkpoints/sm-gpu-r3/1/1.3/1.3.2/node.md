# N42: 工作站级主板 (如 Threadripper Pro WRX90 或 X99) 提供 128+ PCIe 4.0/5.0 通道，支持至少 4-6 个全速 x16

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N9

## Claim

工作站级主板 (如 Threadripper Pro WRX90 或 X99) 提供 128+ PCIe 4.0/5.0 通道，支持至少 4-6 个全速 x16 插槽直连 CPU，对于 2x RTX 4090 方案，需确保两张卡均运行在 x16 模式下以避免带宽瓶颈导致的 Decode 延迟增加。

## Corrected Claim

工作站级主板（如 Threadripper Pro WRX90）提供 128+ PCIe 5.0 通道，支持多个全速 x16 插槽直连 CPU（如 ASRock WRX90 WS EVO 提供 7 个 PCIe 5.0 x16 插槽）。对于 2x RTX 4090 方案，建议确保两张卡均运行在 x16 模式下以最大化带宽，避免潜在的性能瓶颈。

## Evidence

[质询]陈述中关于X99平台提供PCIe 4.0/5.0通道的描述存在事实错误（X99为PCIe 3.0平台），且来源仅证实了WRX90平台具备多PCIe 5.0 x16插槽，未直接证实“2x RTX 4090需确保x16模式以避免Decode延迟”这一特定性能结论。 | 来源[3]直接支持WRX90平台提供7个PCIe Gen5 x16插槽（其中3个直连CPU），证实了高通道数和多插槽能力；但X99部分与事实不符（X99为PCIe 3.0），且缺乏关于RTX 4090具体带宽瓶颈导致Decode延迟的直接证据，故降级。

## Search Query

Threadripper Pro WRX90 PCIe lanes 128 x16 slots multi-GPU workstation setup

## Retrieval Sources

- {'url': 'https://pcpartsgeek.com/best-workstation-motherboards-threadripper-pro/&rut=bba727656c84c0d466dfe3d1b28c4935b31fa87f9ebe002dded13811fe9aed64', 'type': 'ddg', 'title': '6 Best Workstation Motherboards for Threadripper Pro in 2026: WRX90 ...'}
- {'url': 'https://www.supermicro.com/en/products/motherboard/h13srh&rut=97923521c11a2da1f816b7a0086c9ae309e519fe1e161534cbf6cd8c9411d95d', 'type': 'ddg', 'title': 'H13SRH | Motherboards | Products | Supermicro'}
- {'url': 'https://www.asrock.com/mb/AMD/WRX90%20WS%20EVO/index.cn.asp&rut=971b73b28d82471502434864245b4297fbcea4178aa19c19684504fe06f0210a', 'type': 'ddg', 'title': '华擎科技 > WRX90 WS EVO - ASRock'}
