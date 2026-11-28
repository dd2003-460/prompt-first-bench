# N68: 双卡系统 (2x RTX 4090) 需要支持 2 个 PCIe x16 插槽的主板，消费级主板 (如 Z790/X670E) 通常仅提供 1 个全速 x16 

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N21

## Claim

双卡系统 (2x RTX 4090) 需要支持 2 个 PCIe x16 插槽的主板，消费级主板 (如 Z790/X670E) 通常仅提供 1 个全速 x16 插槽，第二插槽可能降速至 x8，导致 PCIe 互联带宽减半 (16 GB/s)，进一步加剧 N27 中提到的通信开销，使多卡方案的理论吞吐量损失从 30% 上升至 40-50%。

## Corrected Claim

双卡系统 (2x RTX 4090) 在消费级主板上常受限于第二插槽降速（如 x8），导致 PCIe 互联带宽受限（Gen4 x8 双向约 32 GB/s），这可能增加通信开销，但具体吞吐量损失取决于工作负载，并非固定从 30% 升至 40-50%。

## Evidence

[质询]数值量级与逻辑推导存在严重错误：PCIe 4.0 x8 的双向带宽约为 32 GB/s（单向 16 GB/s），并非陈述中的 16 GB/s；且将插槽降速直接等同于‘理论吞吐量损失从 30% 上升至 40-50%’缺乏严谨的基准测试支持，属于过度推断，不同工作负载下通信开销占比差异巨大。 | 来源 [1] 仅讨论单卡识别问题，与双卡带宽及吞吐量损失无关；陈述中 PCIe 带宽数值（16 GB/s 对应 x8 双向）存在量级错误（实际 x8 Gen4 双向约 32 GB/s），且吞吐量损失比例缺乏通用性，属经验事实但逻辑推导不严谨。

## Search Query

consumer motherboard dual PCIe x16 slot speed downgrade x8

## Retrieval Sources

- {'url': 'https://www.techpowerup.com/forums/threads/how-to-switch-x8-to-x16.318031/&rut=899f6d6b2f57aed00a3c062f289c38bdf6c8ae0438fd0d9a8dea0819a7c393a9', 'type': 'ddg', 'title': 'how to switch x8 to x16 | TechPowerUp Forums'}
