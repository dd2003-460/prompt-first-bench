# N71: 计算 Qwen3-27B 在 W4 (INT4) 量化下的精确权重体积：使用 N6 中确认的 27.2B 参数量，计算 4-bit 量化后的权重大小（27.2e

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N25

## Claim

计算 Qwen3-27B 在 W4 (INT4) 量化下的精确权重体积：使用 N6 中确认的 27.2B 参数量，计算 4-bit 量化后的权重大小（27.2e9 * 0.5 bytes / 1024^3 ≈ 12.7 GB），并加上 Scale 因子（通常增加 5-10% 开销），得出实际占用约 13.5-14.0 GB，验证 N25 中 ~14GB 的估计

## Corrected Claim

计算 Qwen3-27B 在 W4 (INT4) 量化下的精确权重体积：使用 N6 中确认的 27.2B 参数量，计算 4-bit 量化后的权重大小（27.2e9 * 0.5 bytes / 1024^3 ≈ 12.7 GB），并加上 Scale 因子（通常增加 5-10% 开销），得出实际占用约 13.5-14.0 GB，验证 N25 中 ~14GB 的估计

## Evidence

父节点级核验未通过：非正交, 不完备（1. 正交性违背：子节点1计算出的纯权重体积（~12.8GB）与父节点声称的‘13.5-14.0GB’直接矛盾，且子节点1的结论（Scale开销极小）在逻辑上削弱了父节点中‘Scale增加5-10%’的前提，导致分解内部逻辑冲突。2. 完备性违背：父节点核心任务是‘计算并验证N25的~14GB估计’，但子节点3讨论的是KV Cache，这属于推理时的动态显存占用，与父节点关注的‘静态权重体积’无关，属于偏离主题。）

## Search Query

Qwen 27B INT4 quantized model size GB GGUF AWQ
