# N272: Qwen3.8-27B 在 TP=4 切分下，单个 GPU 参与 AllReduce 的张量大小并非固定的 30MB，而是随序列长度动态变化：对于 LLM 解码

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N86

## Claim

Qwen3.8-27B 在 TP=4 切分下，单个 GPU 参与 AllReduce 的张量大小并非固定的 30MB，而是随序列长度动态变化：对于 LLM 解码阶段，AllReduce 主要同步 Attention Output 和 FFN Output，大小约为 2 * hidden_dim * batch_size * seq_len * dtype_size；在 max_num_seqs=8 且平均生成长度受限时，需计算具体张量尺寸以确定通信基数。

## Corrected Claim

Qwen3.8-27B 在 TP=4 切分下，单个 GPU 参与 AllReduce 的张量大小并非固定的 30MB，而是随序列长度动态变化：对于 LLM 解码阶段，AllReduce 主要同步 Attention Output 和 FFN Output，大小约为 2 * hidden_dim * batch_size * seq_len * dtype_size；在 max_num_seqs=8 且平均生成长度受限时，需计算具体张量尺寸以确定通信基数。

## Evidence

先验知识/题面给定，逻辑校验通过：LLM解码阶段AllReduce同步Attention和FFN输出，张量大小随seq_len动态变化符合分布式推理基本原理

## Search Query

vLLM tensor parallelism allreduce tensor size calculation hidden dim
