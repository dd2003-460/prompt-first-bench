# N117: NVIDIA L4 (24GB) 数据中心卡 TDP 仅 72W，无风扇设计，3年电力成本 ($0.1/kWh, 24/7) 约为 $1,900，远低于 RTX

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

NVIDIA L4 (24GB) 数据中心卡 TDP 仅 72W，无风扇设计，3年电力成本 ($0.1/kWh, 24/7) 约为 $1,900，远低于 RTX 4090 的 ~$3,500；虽然其带宽 (300GB/s) 导致 W4 推理吞吐仅 ~10-15 tok/s，但在高电价或静音敏感场景下，其 TCO 可能优于 4090。

## Corrected Claim

NVIDIA L4 (24GB) 数据中心卡 TDP 为 72W，采用无风扇被动散热设计，在 $0.1/kWh 电价下 3 年 24/7 运行电力成本约为 $1,900。虽然其 300GB/s 带宽限制了 W4 推理吞吐（约 10-15 tok/s），但在高电价或静音敏感场景下，其低功耗特性可能带来优于高功耗消费级显卡（如 RTX 4090）的 TCO 优势。

## Evidence

[质询]陈述中关于 RTX 4090 的 TDP 隐含值（约 450W）及由此推导的电力成本对比（$3,500 vs $1,900）属于经验事实，且参考来源仅覆盖 NVIDIA L4 的规格，未提供 RTX 4090 的功耗数据或两者 TCO 对比的直接证据，无法排除因电价波动或具体负载差异导致的成本估算偏差。 | 来源 [1] 直接支持 L4 的 24GB 显存、72W TDP 及无风扇（被动散热）设计；L4 电力成本计算逻辑自洽（72W * 24h * 365d * 3y * $0.1/kWh ≈ $1,892），但 RTX 4090 的对比数据缺乏来源支持，属经验事实，故降级。

## Retrieval Sources

- {'url': 'https://www.nvidia.com/content/dam/en-zz/Solutions/Data-Center/l4/PB-11316-001_v01.pdf&rut=07404245c598604bbd5abd30eb2bb6336c1de6481826b659cd6f65dd71018969', 'type': 'ddg', 'title': 'PDF NVIDIA L4 GPU Accelerator'}
