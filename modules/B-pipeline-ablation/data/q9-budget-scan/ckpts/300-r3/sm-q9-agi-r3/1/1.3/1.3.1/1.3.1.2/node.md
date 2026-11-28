# N146: 工作点 B（平衡/性价比最优）：max_num_seqs=4, max_model_len=65536，KV Cache 需求 = 4 * 65536 * 12

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N41

## Claim

工作点 B（平衡/性价比最优）：max_num_seqs=4, max_model_len=65536，KV Cache 需求 = 4 * 65536 * 128KB = 32GB，每卡 8GB KV + 3.375GB 权重 = 11.375GB，剩余 4.625GB，支持中等长度科研循环（约 65k tokens），平衡并发与上下文长度

## Corrected Claim

工作点 B（平衡/性价比最优）：max_num_seqs=4, max_model_len=65536，KV Cache 需求 = 4 * 65536 * 128KB = 32GB，每卡 8GB KV + 3.375GB 权重 = 11.375GB，剩余 4.625GB，支持中等长度科研循环（约 65k tokens），平衡并发与上下文长度

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算正确（4*65536*128KB=32GB, 32/4=8GB, 8+3.375=11.375GB, 16-11.375=4.625GB），符合显存分配逻辑。
