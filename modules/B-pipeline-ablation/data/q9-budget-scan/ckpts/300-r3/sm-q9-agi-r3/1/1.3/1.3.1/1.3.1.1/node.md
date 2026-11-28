# N145: 工作点 A（高吞吐/低延迟）：max_num_seqs=2, max_model_len=32768，KV Cache 需求 = 2 * 32768 * 128

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N41

## Claim

工作点 A（高吞吐/低延迟）：max_num_seqs=2, max_model_len=32768，KV Cache 需求 = 2 * 32768 * 128KB = 8GB，每卡 2GB KV + 3.375GB 权重 = 5.375GB，剩余 10.625GB 可用于扩展批处理或更长上下文，适合短推理链快速迭代

## Corrected Claim

工作点 A（高吞吐/低延迟）：max_num_seqs=2, max_model_len=32768，KV Cache 需求 = 2 * 32768 * 128KB = 8GB，每卡 2GB KV + 3.375GB 权重 = 5.375GB，剩余 10.625GB 可用于扩展批处理或更长上下文，适合短推理链快速迭代

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算正确（2*32768*128KB=8GB，8/2+3.375=5.375GB，16-5.375=10.625GB），符合显存分配逻辑。
