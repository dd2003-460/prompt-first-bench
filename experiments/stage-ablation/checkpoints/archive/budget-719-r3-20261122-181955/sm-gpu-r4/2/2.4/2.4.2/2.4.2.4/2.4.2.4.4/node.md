# N732: 若框架不支持 FP8 KV Cache，KV Cache 将回退至 BF16，导致内存占用从 4.0 GB 翻倍至 8.0 GB，总内存需求从 33.5 GB 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N258

## Claim

若框架不支持 FP8 KV Cache，KV Cache 将回退至 BF16，导致内存占用从 4.0 GB 翻倍至 8.0 GB，总内存需求从 33.5 GB 升至 37.5 GB，仍适配 48GB 卡但超出 24GB 卡容量上限。

## Corrected Claim

若框架不支持 FP8 KV Cache，KV Cache 将回退至 BF16，导致内存占用从 4.0 GB 翻倍至 8.0 GB，总内存需求从 33.5 GB 升至 37.5 GB，仍适配 48GB 卡但超出 24GB 卡容量上限。

## Evidence

先验知识/题面给定，逻辑校验通过：FP8为8位，BF16为16位，内存占用翻倍符合位宽比例；33.5GB中KV Cache占4.0GB，回退后增加4.0GB变为37.5GB，算术正确；37.5GB < 48GB且 > 24GB，适配性判断符合逻辑。
