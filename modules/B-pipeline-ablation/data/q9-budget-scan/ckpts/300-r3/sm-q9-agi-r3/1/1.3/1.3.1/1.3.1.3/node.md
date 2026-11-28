# N147: 工作点 C（长上下文/低并发）：max_num_seqs=1, max_model_len=262144，KV Cache 需求 = 1 * 262144 * 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N41

## Claim

工作点 C（长上下文/低并发）：max_num_seqs=1, max_model_len=262144，KV Cache 需求 = 1 * 262144 * 128KB = 32GB，每卡 8GB KV + 3.375GB 权重 = 11.375GB，支持超长上下文（如整篇论文分析），但并发度为 1，总吞吐量最低

## Corrected Claim

工作点 C（长上下文/低并发）：max_num_seqs=1, max_model_len=262144，KV Cache 需求 = 1 * 262144 * 128KB = 32GB，每卡 8GB KV + 3.375GB 权重 = 11.375GB，支持超长上下文（如整篇论文分析），但并发度为 1，总吞吐量最低

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 1 * 262144 * 128KB = 32GB 正确，单卡负载 8GB + 3.375GB = 11.375GB 符合常规显存分配逻辑，长上下文低并发导致吞吐量低的结论符合推理引擎基本原理。
