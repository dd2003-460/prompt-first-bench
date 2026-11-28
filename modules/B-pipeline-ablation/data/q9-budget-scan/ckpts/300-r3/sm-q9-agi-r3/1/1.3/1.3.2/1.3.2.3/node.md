# N150: 工作点 C（中并发中长上下文）：设置 max_model_len=32768, max_num_seqs=4。单序列 KV Cache 占用为 32768 * 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N42

## Claim

工作点 C（中并发中长上下文）：设置 max_model_len=32768, max_num_seqs=4。单序列 KV Cache 占用为 32768 * 128KB = 4GB，总需求 16GB，低于 48.5GB 可用内存，留有 32.5GB 余量用于激活值缓冲和碎片开销。此配置平衡了并发数与上下文长度，适合中等复杂度的实验设计环节。

## Corrected Claim

工作点 C（中并发中长上下文）：设置 max_model_len=32768, max_num_seqs=4。单序列 KV Cache 占用为 32768 * 128KB = 4GB，总需求 16GB，低于 48.5GB 可用内存，留有 32.5GB 余量用于激活值缓冲和碎片开销。此配置平衡了并发数与上下文长度，适合中等复杂度的实验设计环节。

## Evidence

先验知识/题面给定，逻辑校验通过：32768 * 128KB = 4GB，4 * 4GB = 16GB，16GB < 48.5GB，余量计算正确，符合内存管理基本逻辑。
