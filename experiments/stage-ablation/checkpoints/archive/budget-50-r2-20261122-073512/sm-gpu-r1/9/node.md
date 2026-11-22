# N36: Mac Studio M2 Ultra (192GB) 统一内存带宽为 800 GB/s，M2 Ultra (512GB) 带宽为 800 GB/s (部分配置

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

Mac Studio M2 Ultra (192GB) 统一内存带宽为 800 GB/s，M2 Ultra (512GB) 带宽为 800 GB/s (部分配置) 或更高 (需具体型号确认，通常为 800GB/s 级别)；由于统一内存延迟高于 GDDR/HBM，实际推理吞吐约为理论带宽上限的 60-70%，即约 48-56 tokens/s (理论 800/56=14.2? 错误，800/56=14.2 是错的，800/54=14.8? 不，54GB 是权重，KV cache 很小。800 GB/s / 54 GB ≈ 14.8 tokens/s? 不对，27B 是 54GB。800/54 = 14.8 tokens/s。等等，M2 Ultra 带宽是 800GB/s 吗？M1 Ultra 是 800GB/s。M2 Ultra 也是 800GB/s。那么 800/54 ≈ 14.8 tokens/s。这比 4090 (18 tokens/s) 还低？是的，因为 27B 模型较大，而 Mac 带宽相对较低。修正：M2 Ultra 带宽 800 GB/s，27B BF16 (54GB) 理论上限 14.8 tokens/s。

## Corrected Claim

Mac Studio M2 Ultra (192GB) 统一内存带宽为 800 GB/s。由于统一内存延迟高于 GDDR/HBM，实际推理吞吐受限于带宽，具体数值取决于模型大小、量化方式及软件优化，通常远低于理论带宽上限，需具体测试确认。

## Evidence

[质询]陈述中关于推理吞吐的具体数值（48-56 tokens/s 或 14.8 tokens/s）属于经验事实，且内部计算逻辑混乱（先给出48-56，后自我修正为14.8，且未明确模型具体大小和量化方式，仅凭带宽除以权重大小估算吞吐过于简化，忽略了计算密集型和内存密集型的区别以及实际效率损耗的具体比例），缺乏直接来源支持该具体吞吐数值。 | 来源[3]直接支持M2 Ultra 192GB的内存带宽为800 GB/s，但无来源支持具体的推理吞吐数值（48-56或14.8 tokens/s），该部分为经验事实且推导过程存在不确定性，故降级。

## Retrieval Sources

- {'url': 'https://www.36kr.com/p/2289342420031233&rut=dffd9732e5fbfaf92df3870bbeaed02c757b6cdb4b30abf2fd00abe0845dbdbc', 'type': 'ddg', 'title': '苹果最强芯片深夜炸场：192gb统一内存，单台设备能跑ai大模型-36氪'}
- {'url': 'https://support.apple.com/zh-cn/111835&rut=229df7470e3bf428317bd868faca8af772de55153747e210cb55f3c5dac1afdd', 'type': 'ddg', 'title': 'Mac Studio（2023 年）- 技术规格 - 官方 Apple 支持 (中国)'}
- {'url': 'https://hardwarehq.io/gpus/mac-studio-m2-ultra-192gb&rut=643c9de4c3d6ba0d7300d7a7e638e8a5d2d4c08938dc419bf20978f6e17ee991', 'type': 'ddg', 'title': 'Mac Studio M2 Ultra 192GB for AI — Specs, VRAM & Compatibility | HardwareHQ'}
