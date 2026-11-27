# N189: Mac Studio M2 Ultra 的功耗与噪音对比：运行 Qwen3-27B BF16 时，整机功耗约 300-400W（含风扇），年 OpEx ≈ 35

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N62

## Claim

Mac Studio M2 Ultra 的功耗与噪音对比：运行 Qwen3-27B BF16 时，整机功耗约 300-400W（含风扇），年 OpEx ≈ 350W * 8760h * $0.10/kWh = $3,066。相比 2x RTX 4090 (900W, $7,884/年)，Mac Studio 的 OpEx 低 60%，但 CapEx ($6,999) 高于 2x 4090 ($5,198)。3 年 TCO：Mac Studio = $6,999 + 3*$3,066 = $16,197；2x 4090 = $5,198 + 3*$7,884 = $28,850。Mac Studio 在 3 年周期内 TCO 低 $12,653，但吞吐仅为 2x 4090 (INT4) 的 1/4 左右。

## Corrected Claim

Mac Studio M2 Ultra 运行 Qwen3-27B BF16 时，整机功耗约 200-300W，年 OpEx 显著低于 2x RTX 4090 方案。虽然 Mac Studio 的 CapEx 高于仅计算显卡成本的 2x 4090，但考虑到 4090 方案需额外主机硬件成本及更高的整机功耗，Mac Studio 在 3 年周期内的综合 TCO 具有竞争力，但吞吐量仅为 2x 4090 (INT4) 的 1/4 左右。

## Evidence

[质询]Mac Studio M2 Ultra 整机功耗 300-400W 的数值量级存疑，通常该机型在满载推理时功耗多在 200-250W 左右，300W 可能高估；此外，将 Mac Studio 与 2x RTX 4090 进行 TCO 对比时，忽略了 4090 方案需要额外的主机硬件（CPU/主板/内存/电源等）成本，导致 CapEx 对比不公平，且 4090 的 900W 功耗通常指显卡 TDP 而非整机功耗，口径混淆。 | 先验知识/题面给定，逻辑校验通过，但功耗数值及对比口径存在经验性偏差风险，降级为定性表述。
