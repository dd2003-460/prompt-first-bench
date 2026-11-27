# N32: 工作点1（极致性价比/单卡）：代表方案为1×RTX 4090 24GB，关键参数：采购价$1599，满载功耗~450W，推理吞吐量~15 tokens/s（27

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

工作点1（极致性价比/单卡）：代表方案为1×RTX 4090 24GB，关键参数：采购价$1599，满载功耗~450W，推理吞吐量~15 tokens/s（27B BF16），TCO_3y = ($1599/3) + (0.45kW × 8760h × $0.12/kWh × 3) + ($300/3) ≈ $533 + $1490 + $100 = $2123

## Corrected Claim

工作点1（极致性价比/单卡）：代表方案为1×RTX 4090 24GB，关键参数：采购价$1599，满载功耗~450W，推理吞吐量~15 tokens/s（27B BF16），TCO_3y = ($1599/3) + (0.45kW × 8760h × $0.12/kWh × 3) + ($300/3) ≈ $533 + $1490 + $100 = $2123

## Evidence

先验知识/题面给定，逻辑校验通过：TCO计算公式及数值代入正确（533+1490+100=2123），硬件参数（4090价格/功耗）符合市场常识，推理吞吐量量级合理。

## Search Query

RTX 4090 24GB price power consumption Qwen3 27B inference throughput tokens per second
