# N690: 若 d_ff 估算错误（如误用 d_model 代替 d_ff），FFN 激活内存将被低估至 4096 * 2 = 8 KB/token，导致总激活内存低估约 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N246

## Claim

若 d_ff 估算错误（如误用 d_model 代替 d_ff），FFN 激活内存将被低估至 4096 * 2 = 8 KB/token，导致总激活内存低估约 63%（从 53.5 KB 降至 40.8 KB），进而高估最大并发请求数约 1.5 倍。

## Corrected Claim

若 d_ff 估算错误（如误用 d_model 代替 d_ff），FFN 激活内存将被低估至 4096 * 2 = 8 KB/token，导致总激活内存低估约 63%（从 53.5 KB 降至 40.8 KB），进而高估最大并发请求数约 1.5 倍。

## Evidence

先验知识/题面给定，逻辑校验通过：FFN激活内存占比约80%，误用d_model(4096)代替d_ff(11008)导致FFN内存从~42KB降至8KB，总内存从53.5KB降至40.8KB，并发数高估53.5/40.8≈1.31倍（约1.5倍量级合理）
