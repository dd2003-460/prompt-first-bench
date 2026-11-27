# N87: 吞吐量测试条件标准化定义：输入序列长度 32768 tokens，输出序列长度 1024 tokens，Batch Size 1，Temperature 0，T

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N20

## Claim

吞吐量测试条件标准化定义：输入序列长度 32768 tokens，输出序列长度 1024 tokens，Batch Size 1，Temperature 0，Top-p 1.0，使用 vLLM 或 TGI 框架，记录平均 tokens/s 和首字延迟 (TTFT)。

## Corrected Claim

吞吐量测试条件标准化定义：输入序列长度 32768 tokens，输出序列长度 1024 tokens，Batch Size 1，Temperature 0，Top-p 1.0，使用 vLLM 或 TGI 框架，记录平均 tokens/s 和首字延迟 (TTFT)。

## Evidence

先验知识/题面给定，逻辑校验通过
