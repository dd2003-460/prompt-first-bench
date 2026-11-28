# N11: 32K上下文窗口KV Cache占用的理论上限计算公式：KV_Cache_GB = 2 * num_layers * hidden_dim * seq_len 

- **status**: degraded
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N2

## Claim

32K上下文窗口KV Cache占用的理论上限计算公式：KV_Cache_GB = 2 * num_layers * hidden_dim * seq_len * bytes_per_token / 1e9，需代入Qwen3-27B的具体层数(64?)与隐藏维度(4096?)[待核验]

## Corrected Claim

32K上下文窗口KV Cache占用的理论上限计算公式为：KV_Cache_GB = 2 * num_layers * hidden_dim * seq_len * bytes_per_element / 1e9。其中bytes_per_element取决于数据类型（如BF16为2字节）。Qwen3-27B的具体层数与隐藏维度需查阅官方技术报告确认，常见同参数量级模型可能采用不同配置（如40-50层，8192维），因此不能直接断言为64层和4096维。

## Evidence

[质询]Qwen3-27B的具体架构参数（层数64、隐藏维度4096）属于经验事实，且当前主流大模型（如Llama系列同参数量级）通常采用更宽的隐藏维度（如8192）和更少的层数（如40-50），此处引用的参数值存在不确定性，且公式中bytes_per_token未明确指定数据类型（FP16/BF16通常为2字节，INT8为1字节），导致计算结果依赖未明确的假设。 | 经验事实，逻辑自洽但缺来源支持；公式结构符合KV Cache通用计算原理（Key+Value各一份，乘以层数、序列长度和数据类型大小），但具体参数值（64层/4096维）未经权威来源确认，且不同量化精度下结果差异显著。

## Search Query

Qwen3-27B model architecture num layers hidden size kv cache formula
