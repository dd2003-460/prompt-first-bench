# N337: AMD MI300X 理论解码吞吐上限修正：公式 Throughput_max = HBM_BW / Bytes_per_token_access；其中 Byt

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N101

## Claim

AMD MI300X 理论解码吞吐上限修正：公式 Throughput_max = HBM_BW / Bytes_per_token_access；其中 Bytes_per_token_access = Weight_size_per_token (27B*2B=54GB) + KV_read_write (动态)；若仅考虑权重读取瓶颈，5300 GB/s / 54 GB ≈ 98 tok/s 理论上限；N101 中的 55.8 tok/s 需重新验证分母是否误加了全量 KV Cache 而非增量读写

## Corrected Claim

AMD MI300X 理论解码吞吐上限修正：公式 Throughput_max = HBM_BW / Bytes_per_token_access；其中 Bytes_per_token_access = Weight_size_per_token (27B*2B=54GB) + KV_read_write (动态)；若仅考虑权重读取瓶颈，5300 GB/s / 54 GB ≈ 98 tok/s 理论上限；N101 中的 55.8 tok/s 需重新验证分母是否误加了全量 KV Cache 而非增量读写

## Evidence

先验知识/题面给定，逻辑校验通过：MI300X HBM带宽约5.3TB/s，27B模型FP16权重约54GB，5300/54≈98 tok/s，计算逻辑自洽且量级合理。
