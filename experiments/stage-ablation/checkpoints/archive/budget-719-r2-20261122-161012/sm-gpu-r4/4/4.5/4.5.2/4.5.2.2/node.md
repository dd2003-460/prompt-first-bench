# N235: H100 80GB 在 BF16 下剩余 25GB 显存，最大支持 Batch Size = 25 / 1.2 ≈ 20 个并发请求，与 A100 相同，但 H

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N109

## Claim

H100 80GB 在 BF16 下剩余 25GB 显存，最大支持 Batch Size = 25 / 1.2 ≈ 20 个并发请求，与 A100 相同，但 H100 的更高带宽使其在相同 Batch 下吞吐更高。

## Corrected Claim

H100 80GB 在 BF16 下若剩余 25GB 显存，且单请求显存占用约为 1.2GB（取决于序列长度和模型大小），则最大支持 Batch Size 约为 20 个并发请求；H100 相比 A100 具有更高带宽，在相同 Batch Size 下通常能提供更低的延迟或更高的吞吐。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点1针对BF16精度下的KV Cache占用进行详细计算，证明原假设在长上下文下失效；子节点2引入FP8量化作为变量，展示精度降低后的不同结果。两者分别对应不同的技术路径（精度选择），逻辑上正交且互补，共同覆盖了父节点中关于'Batch Size计算错误'的核心反驳点，且未出现重复或矛盾。）
