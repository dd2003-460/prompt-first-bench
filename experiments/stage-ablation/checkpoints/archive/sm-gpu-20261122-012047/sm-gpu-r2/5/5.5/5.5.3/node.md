# N151: AMD 数据中心级显卡（MI300X）的驱动支持周期约为 3-5 年，MI300X 预计支持至 2027-2029 年，ROCm 软件栈的向后兼容性比 CUDA

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N40

## Claim

AMD 数据中心级显卡（MI300X）的驱动支持周期约为 3-5 年，MI300X 预计支持至 2027-2029 年，ROCm 软件栈的向后兼容性比 CUDA 弱，长期持有需预留软件栈迁移成本（约 $500-$2000/次）。

## Corrected Claim

AMD 数据中心级显卡（MI300X）的驱动支持周期通常较长，ROCm 软件栈的向后兼容性相比 CUDA 可能存在差异，长期持有需预留软件栈迁移成本。

## Evidence

[质询]陈述中包含具体的驱动支持周期（3-5年）、具体截止日期（2027-2029）以及具体的迁移成本数值（$500-$2000/次），这些属于经验事实且缺乏公开权威来源的直接支持，尤其是迁移成本的具体金额区间缺乏依据。 | 参考来源仅确认MI300X为数据中心级GPU，未提供驱动支持周期、具体截止日期或迁移成本数据；逻辑上长期持有需考虑软件栈兼容性风险是合理的，但具体数值无法从现有来源验证。

## Search Query

AMD MI300X driver support lifecycle ROCm backward compatibility

## Retrieval Sources

- {'url': 'https://instinct.docs.amd.com/projects/amdgpu-docs/en/latest/gpu-partitioning/mi300x/index.html&rut=6e40cef19d998593958f52d9202409bb024ec786edc040356a3a2b87b29d5944', 'type': 'ddg', 'title': 'AMD Instinct MI300X GPU — AMD GPU Driver (amdgpu) 31.60.0'}
- {'url': 'https://www.amd.com/en/products/accelerators/instinct/mi300/mi300x.html&rut=a7616f60f54071936540a6fb9e37b79094f7ed96f1e90a385e5b54e51730a348', 'type': 'ddg', 'title': 'AMD Instinct™ MI300X Accelerators'}
- {'url': 'https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/data-sheets/amd-instinct-mi300x-data-sheet.pdf&rut=0e33306caf8ed99b2b60ea4114a803736d028db358b7d573e97cc4b8dbdbdaa1', 'type': 'ddg', 'title': 'PDF AMD Instinct MI300X Accelerator'}
