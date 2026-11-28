# N165: N57中GPU显存带宽竞争的具体量化机制：在TP=4架构下，N个并发请求共享4张V100的HBM2带宽（900GB/s/卡），需推导有效带宽BW_eff(N) 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N57

## Claim

N57中GPU显存带宽竞争的具体量化机制：在TP=4架构下，N个并发请求共享4张V100的HBM2带宽（900GB/s/卡），需推导有效带宽BW_eff(N) = BW_theoretical / (1 + β*(N-1))，其中β为带宽争用系数，需通过NCCL all-reduce基准测试在不同并发度下的实际吞吐下降率确定β值。

## Corrected Claim

N57中GPU显存带宽竞争的具体量化机制：在TP=4架构下，N个并发请求共享4张V100的HBM2带宽（900GB/s/卡），需推导有效带宽BW_eff(N) = BW_theoretical / (1 + β*(N-1))，其中β为带宽争用系数，需通过NCCL all-reduce基准测试在不同并发度下的实际吞吐下降率确定β值。

## Evidence

先验知识/题面给定，逻辑校验通过：V100 HBM2带宽约900GB/s符合硬件规格，带宽争用模型BW_eff(N) = BW_theoretical / (1 + β*(N-1))在逻辑上自洽且量纲正确，β作为经验系数需实测确定符合工程实践。
