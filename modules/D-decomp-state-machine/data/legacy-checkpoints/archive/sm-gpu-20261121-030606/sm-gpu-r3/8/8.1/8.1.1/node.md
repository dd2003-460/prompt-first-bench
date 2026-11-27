# N357: AllReduce通信量修正：Qwen3-27B层数n_layers=28，每层AllReduce数据量=hidden_size(4096)*dtype_siz

- **status**: degraded
- **level**: L4
- **source**: derived
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N152

## Claim

AllReduce通信量修正：Qwen3-27B层数n_layers=28，每层AllReduce数据量=hidden_size(4096)*dtype_size(2 bytes)=8KB。总通信量=28*8KB=224KB/token。此数值基于BF16/FP16精度；若使用INT8/FP8，dtype_size=1 byte，总通信量降至112KB/token，通信瓶颈减半。

## Corrected Claim

若Qwen3-27B的层数为28且hidden_size为4096，则BF16精度下每token的AllReduce通信量为224KB；INT8/FP8精度下为112KB。

## Evidence

[质询]该陈述包含具体的硬件/模型架构参数（Qwen3-27B的层数28、hidden_size 4096），属于经验事实。虽然数学计算（28 * 4096 * 2 = 224KB）在逻辑上自洽，但缺乏外部来源验证这些具体参数是否准确对应Qwen3-27B模型。若模型实际层数或隐藏层维度不同，结论将错误。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法验证Qwen3-27B的具体架构参数）
