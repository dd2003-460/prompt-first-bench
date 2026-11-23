# N194: Apple M2 Ultra 192GB 运行 Qwen3-27B BF16 时的实际功耗约为 100W-150W (GPU+CPU)，远低于 2x RTX 4

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N60

## Claim

Apple M2 Ultra 192GB 运行 Qwen3-27B BF16 时的实际功耗约为 100W-150W (GPU+CPU)，远低于 2x RTX 4090 的 900W，其每 token 电力成本仅为 NVIDIA 方案的 1/10，但由于吞吐量低 5-10 倍，每 token 总成本 (含硬件折旧) 在高频使用场景下仍高于 RTX 4090 方案。

## Corrected Claim

Apple M2 Ultra 192GB 运行 Qwen3-27B BF16 时的实际功耗约为 100W-150W (GPU+CPU)，远低于 2x RTX 4090 的 900W。虽然其每 token 电力成本显著低于 NVIDIA 方案（约为 1/9 至 1/45），但由于吞吐量低 5-10 倍，在考虑硬件折旧后，每 token 总成本在高频使用场景下可能接近或略高于 RTX 4090 方案，具体取决于硬件购置成本与使用寿命假设。

## Evidence

[质询]数值量级与成本比例存在逻辑矛盾：若吞吐量低5-10倍，且功耗仅为1/9（100-150W vs 900W），则每token电力成本应约为NVIDIA方案的1/45至1/9，而非1/10；此外，'每token总成本仍高于RTX 4090'的结论依赖于硬件折旧分摊，但M2 Ultra与2x 4090的硬件初始成本差异巨大（通常M2 Ultra整机成本远低于2x 4090显卡），在高频使用下折旧占比降低，电力成本优势可能抵消折旧劣势，该结论缺乏具体折旧模型支持，属于过度推断。 | 先验知识/题面给定，逻辑校验发现内部数值矛盾（电力成本比例与吞吐量/功耗比例不匹配）及结论推导缺乏必要前提（硬件折旧具体数值），故降级。
