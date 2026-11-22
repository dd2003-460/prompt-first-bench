# N93: Qwen3-27B 在 W4 (INT4/AWQ/GPTQ) 精度下的权重文件大小为 13.5 GB (27B * 0.5 bytes)，相比 BF16 节省 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N13

## Claim

Qwen3-27B 在 W4 (INT4/AWQ/GPTQ) 精度下的权重文件大小为 13.5 GB (27B * 0.5 bytes)，相比 BF16 节省 75% 权重显存；若 KV Cache 同步量化为 FP8，则总显存占用约为 13.5 GB + (32K * KV_FP8_size)，需计算具体 KV 节省值。

## Corrected Claim

Qwen3-27B 在 W4 (INT4/AWQ/GPTQ) 精度下的权重文件大小为 13.5 GB (27B * 0.5 bytes)，相比 BF16 节省 75% 权重显存；若 KV Cache 同步量化为 FP8，则总显存占用约为 13.5 GB + (32K * KV_FP8_size)，需计算具体 KV 节省值。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点逻辑清晰且正交：节点1负责推导每token KV大小的公式与基准值；节点2基于节点1的结果计算32K上下文下的具体KV总量及节省比例；节点3综合权重与KV数据得出总显存占用并给出硬件适配结论。三者层层递进，无重复或矛盾。虽然节点2中的具体数值（如256KB）依赖于节点1，但这属于正常的计算依赖而非冗余参数，且节点3的结论依赖于前两者的综合，符合分解逻辑。）
