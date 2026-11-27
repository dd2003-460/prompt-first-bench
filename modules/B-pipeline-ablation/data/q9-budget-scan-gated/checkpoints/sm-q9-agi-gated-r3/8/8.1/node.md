# N71: 修正N34/N22的KV Cache计算错误：Qwen3.8-27B (GQA, 8 kv_heads, 128 dim) 每Token KV占用应为 2*8*

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N34

## Claim

修正N34/N22的KV Cache计算错误：Qwen3.8-27B (GQA, 8 kv_heads, 128 dim) 每Token KV占用应为 2*8*128*1byte(FP8) = 2KB/token，而非N22声称的64KB/token（后者误用了32 layers或未除以GQA分组数）。因此单序列262144 tokens的KV占用为 262144 * 2KB = 512 MB，而非4.19 GB。

## Corrected Claim

修正N34/N22的KV Cache计算错误：Qwen3.8-27B (GQA, 8 kv_heads, 128 dim) 每Token KV占用应为 2*8*128*1byte(FP8) = 2KB/token，而非N22声称的64KB/token（后者误用了32 layers或未除以GQA分组数）。因此单序列262144 tokens的KV占用为 262144 * 2KB = 512 MB，而非4.19 GB。

## Evidence

先验知识/题面给定，逻辑校验通过：KV Cache计算公式为 2(K+V) * num_kv_heads * head_dim * bytes_per_element。代入参数 2 * 8 * 128 * 1 = 2048 bytes = 2KB/token。总大小 262144 * 2KB = 512MB。计算无误，且符合GQA架构下KV头数少于Query头数的常识。
