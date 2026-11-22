# N267: T_throughput 定义的工作点 2 (目标长上下文/中吞吐)：Seq_len = 32K (题目约束)。KV Cache 占用显著增加 (约 10-15

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N81

## Claim

T_throughput 定义的工作点 2 (目标长上下文/中吞吐)：Seq_len = 32K (题目约束)。KV Cache 占用显著增加 (约 10-15GB per layer 累积)，RTX 4090 INT4 的解码速度预计降至 40-60 tokens/s。瓶颈从纯 Memory-Bound 转向 Compute-Bound 与 Memory-Bound 的混合，FlashAttention-2/3 的引入可提升 10-20% 吞吐。

## Corrected Claim

T_throughput 定义的工作点 2 (目标长上下文/中吞吐)：Seq_len = 32K (题目约束)。KV Cache 占用随模型规模显著增加（具体数值取决于模型参数量与隐藏层维度），RTX 4090 INT4 的解码速度预计降至 40-60 tokens/s（视模型大小而定）。瓶颈从纯 Memory-Bound 转向 Compute-Bound 与 Memory-Bound 的混合，FlashAttention-2/3 的引入可提升 10-20% 吞吐。

## Evidence

[质询]KV Cache 占用数值量级存疑：对于主流 LLM（如 7B-13B 参数），32K 上下文下每层 KV Cache 通常仅为数百 MB 至 1-2GB，而非 10-15GB；10-15GB 的每层占用通常对应超大模型（如 70B+）或极宽隐藏层，且未指明具体模型规模，导致该数值缺乏普适性基础。 | 先验知识/题面给定，逻辑校验通过：长上下文确实导致 KV Cache 增加及瓶颈混合化，FlashAttention 提升吞吐符合工程常识；但具体数值（10-15GB/layer, 40-60 tok/s）依赖未指定的模型规模，属于经验事实且缺乏来源支持，故降级。

## Search Query

RTX 4090 32K context length throughput LLM inference
