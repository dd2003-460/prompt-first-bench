# N515: RX 7900 XT 在 INT4 量化下，权重占用 13.5GB，扣除框架开销 2GB 后，剩余显存仅 4.5GB，而 32K 上下文 BF16 KV Cac

- **status**: verified
- **level**: L5
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N180

## Claim

RX 7900 XT 在 INT4 量化下，权重占用 13.5GB，扣除框架开销 2GB 后，剩余显存仅 4.5GB，而 32K 上下文 BF16 KV Cache 需 8GB，显存缺口 3.5GB，单卡无法支持 32K 上下文。

## Corrected Claim

RX 7900 XT 在 INT4 量化下，权重占用 13.5GB，扣除框架开销 2GB 后，剩余显存仅 4.5GB，而 32K 上下文 BF16 KV Cache 需 8GB，显存缺口 3.5GB，单卡无法支持 32K 上下文。

## Evidence

先验知识/题面给定，逻辑校验通过：RX 7900 XT 显存为 20GB，13.5GB(权重) + 2GB(开销) + 8GB(KV Cache) = 23.5GB > 20GB，缺口 3.5GB，计算自洽。
