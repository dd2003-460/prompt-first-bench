# N265: Qwen3-27B 模型在 BF16 精度下的权重文件大小为 54GB，计算公式为 27e9 * 2 bytes，此数值是 Decode 阶段每次 token 

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N82

## Claim

Qwen3-27B 模型在 BF16 精度下的权重文件大小为 54GB，计算公式为 27e9 * 2 bytes，此数值是 Decode 阶段每次 token 生成需从显存读取的最小数据量（假设无 KV Cache 读取干扰）

## Corrected Claim

Qwen3-27B 模型在 BF16 精度下的权重文件大小为 54GB，计算公式为 27e9 * 2 bytes，此数值是 Decode 阶段每次 token 生成需从显存读取的最小数据量（假设无 KV Cache 读取干扰）

## Evidence

先验知识/题面给定，逻辑校验通过：27e9参数 * 2字节(BF16) = 54GB，且Decode阶段权重读取量确实等于模型权重大小
