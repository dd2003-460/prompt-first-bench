# N614: AMX 对 INT4 量化的加速比约为 3-5 倍，这一结论基于 AMD 官方文档和第三方测试；具体数值受矩阵尺寸和内存带宽影响，小矩阵（< 64x64）加速比

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N216

## Claim

AMX 对 INT4 量化的加速比约为 3-5 倍，这一结论基于 AMD 官方文档和第三方测试；具体数值受矩阵尺寸和内存带宽影响，小矩阵（< 64x64）加速比可能降至 2 倍，大矩阵（> 512x512）可达 5 倍。

## Corrected Claim

AMX 对 INT4 量化通常具有显著加速效果，具体加速比受矩阵尺寸、内存带宽及硬件代际影响，小矩阵加速比相对较低，大矩阵加速比更高，具体数值需参考特定硬件版本的官方基准测试。

## Evidence

[质询]具体数值（3-5倍、2倍、5倍）及阈值（64x64, 512x512）属于经验事实，缺乏来源支持，且不同硬件代际（如MI250 vs MI300）及具体实现（如使用何种库）下加速比差异巨大，断言固定区间存在风险。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

AMD AMX INT4 acceleration ratio benchmark
