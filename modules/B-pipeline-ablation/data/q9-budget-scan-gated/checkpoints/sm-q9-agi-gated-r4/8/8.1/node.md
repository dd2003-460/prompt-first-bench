# N71: 修正N34/N22的KV Cache计算错误：Qwen3.8-27B (GQA, 8 kv_heads, 128 dim) 每Token KV占用应为 2*8*

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N34

## Claim

修正N34/N22的KV Cache计算错误：Qwen3.8-27B (GQA, 8 kv_heads, 128 dim) 每Token KV占用应为 2*8*128*1byte(FP8) = 2KB/token，而非N22声称的64KB/token（后者误用了32 layers或未除以GQA分组数）。因此单序列262144 tokens的KV占用为 262144 * 2KB = 512 MB，而非4.19 GB。

## Corrected Claim

修正N34/N22的KV Cache计算错误：Qwen3.8-27B (GQA, 8 kv_heads, 128 dim) 每Token KV占用应为 2*8*128*1byte(FP8) = 2KB/token，而非N22声称的64KB/token（后者误用了32 layers或未除以GQA分组数）。因此单序列262144 tokens的KV占用为 262144 * 2KB = 512 MB，而非4.19 GB。

## Evidence

父节点级核验未通过：非正交, 不完备, 有冗余（子节点之间存在严重逻辑矛盾和事实错误。1. 矛盾性：子节点1和3声称正确值是64KB/token和16GB，而父节点声称正确值是2KB/token和512MB。子节点实际上是在反驳父节点的结论，而非分解父节点，导致父子节点逻辑冲突。2. 事实错误：Qwen3.8-27B通常有48层左右（具体视版本而定，但绝非32层），且即使按32层计算，FP8下每token占用确实远大于2KB（2*32*8*128/1024=64KB），父节点的“2KB”结论本身可能是错误的（除非它指的是单层或误解了单位），但作为检查员，主要问题是子节点试图“修正”父节点而不是分解它，且子节点内部对于‘谁错了’的判断与父节点预设相反。3. 冗余：子节点1和3都在重复计算总占用，且都基于同一个（被父节点否定的）64KB数值。）
