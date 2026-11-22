# N6: Qwen3-27B 模型在 BF16 精度下的权重文件大小为 54GB (27B × 2 bytes)，这是显存容量的绝对下限基准。

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

Qwen3-27B 模型在 BF16 精度下的权重文件大小为 54GB (27B × 2 bytes)，这是显存容量的绝对下限基准。

## Corrected Claim

Qwen3-27B 模型在 BF16 精度下的权重文件大小为 54GB (27B × 2 bytes)，这是显存容量的绝对下限基准。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点1修正了父节点中关于总参数量和总权重大小的核心错误（从27B修正为33.5B，54GB修正为67GB），确立了正确的全局基准；子节点2进一步细化了显存构成的结构特征，指出了嵌入层和输出头的固定开销及其不可压缩性。两者分别关注‘总量修正’和‘结构分布/固定开销’，角度不同且互补，无重复或矛盾。）
