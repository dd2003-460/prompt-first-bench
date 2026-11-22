# N521: 标准化基准测试的输出长度固定为1024 tokens，需指定采样策略（如Greedy Decoding或固定Temperature=0.7的Top-K采样），以

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N162

## Claim

标准化基准测试的输出长度固定为1024 tokens，需指定采样策略（如Greedy Decoding或固定Temperature=0.7的Top-K采样），以消除随机性对吞吐量测量的影响

## Corrected Claim

标准化基准测试的输出长度固定为1024 tokens，需指定采样策略（如Greedy Decoding或固定Temperature=0.7的Top-K采样），以消除随机性对吞吐量测量的影响

## Evidence

先验知识/题面给定，逻辑校验通过：标准化基准测试（如MLPerf Inference）确实通过固定输出长度（如1024 tokens）和确定性采样策略（如Greedy或固定种子/温度）来消除随机性，确保吞吐量测量的可复现性和公平性。
