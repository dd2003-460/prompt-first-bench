# N135: Apple Mac Studio M3 Ultra (192GB/256GB Unified Memory, ~800GB/s bandwidth, ~$600

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

Apple Mac Studio M3 Ultra (192GB/256GB Unified Memory, ~800GB/s bandwidth, ~$6000-$10000) 作为非典型方案，其统一内存架构允许单设备加载 BF16 权重 (54GB) 并保留大量 KV Cache 空间 (32K ctx BF16 KV Cache ~2GB, 余量巨大)，且无需量化即可保证最高质量 (Quality_Score=1.0)；尽管其单 token 延迟高于 H100，但在'零量化损失 + 单设备部署 + 中等吞吐'场景下，其性价比可能优于多卡消费级方案，需纳入最终条件性推荐对比。

## Corrected Claim

Apple Mac Studio M3 Ultra 作为非典型方案，其统一内存架构允许单设备加载大模型权重并保留KV Cache空间，无需量化即可保证最高质量；尽管单token延迟高于H100，但在特定场景下具有部署优势，需纳入对比。

## Evidence

[质询]来源仅确认了硬件型号（M3 Ultra Mac Studio）的存在，但未提供具体的内存带宽数值（~800GB/s）、精确价格区间（$6000-$10000）或针对特定模型（54GB BF16）的推理性能对比数据，属于缺乏直接证据支持的经验性参数断言。 | 来源[2]和[3]证实了M3 Ultra Mac Studio的存在及硬件配置，但缺乏对内存带宽、具体价格及LLM推理性价比的直接数据支持，逻辑上自洽但属经验事实且缺来源直接支持。

## Retrieval Sources

- {'url': 'https://www.apple.com/mac-studio/&rut=c90237983b6100d24d7951da9a7ef950c681ef8ad0ddf31c2b25ab1001c428e5', 'type': 'ddg', 'title': 'Mac Studio - Apple'}
- {'url': 'https://www.apple.com/shop/product/fu973ll/a/Refurbished-Mac-Studio-Apple-M3-Ultra-chip-with-28%E2%80%91Core-CPU-and-60%E2%80%91Core-GPU&rut=c8c7ce994298a7ac7b71fcc962a3765d9e1c018360a199ff37222138236c1dc9', 'type': 'ddg', 'title': 'Refurbished Mac Studio Apple M3 Ultra chip with 28‑Core CPU and 60‑Core GPU'}
- {'url': 'https://www.bestbuy.com/product/apple-mac-studio-m3-ultra-1tb-ssd-silver/JJGCQXRQKY&rut=39e9b781d1de76cfe3274a89db966a60f156589592b73e8fe09f1c10bd6441b7', 'type': 'ddg', 'title': 'Apple - Mac Studio - M3 Ultra - 1TB SSD - Silver'}
