# N104: AMD Radeon PRO W7900 在 ROCm 6.0+ 下运行 Qwen3-27B 的兼容性矩阵：需确认 vLLM/TGI 是否原生支持 ROCm 后

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N33

## Claim

AMD Radeon PRO W7900 在 ROCm 6.0+ 下运行 Qwen3-27B 的兼容性矩阵：需确认 vLLM/TGI 是否原生支持 ROCm 后端的 FP8/INT8 量化内核；若不支持，需回退至 BF16 (54GB > 48GB 不可行) 或 INT8 (27GB+16GB=43GB < 48GB 可行)，但 INT8 量化在 ROCm 下的算子覆盖度需验证，[待核验] 具体算子缺失列表。

## Corrected Claim

AMD Radeon PRO W7900 在 ROCm 6.0+ 下运行 Qwen3-27B 的兼容性需进一步确认：需验证 vLLM/TGI 对 ROCm 后端 FP8/INT8 量化内核的支持情况；若不支持，需评估 BF16 或 INT8 量化在 48GB 显存下的可行性及算子覆盖度，具体缺失列表待核验。

## Evidence

[质询]该陈述包含具体的硬件显存规格（48GB）、模型量化后体积估算（BF16 54GB, INT8 43GB）以及软件栈（ROCm 6.0+, vLLM/TGI）的兼容性细节，属于经验事实。由于检索失败，无法验证这些具体数值和兼容性状态是否准确，存在参数过时或估算偏差的风险。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法验证具体显存数值及ROCm算子覆盖度）

## Search Query

ROCm 6.0 vLLM Qwen 27B INT8 FP8 support status
