# N145: vLLM/TensorRT-LLM在NVIDIA单卡上的首次编译与依赖安装耗时约为1-2小时，具体取决于Python环境复杂度与PyTorch版本兼容性。

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N48

## Claim

vLLM/TensorRT-LLM在NVIDIA单卡上的首次编译与依赖安装耗时约为1-2小时，具体取决于Python环境复杂度与PyTorch版本兼容性。

## Corrected Claim

vLLM/TensorRT-LLM在NVIDIA单卡上的首次编译与依赖安装耗时约为1-2小时，具体取决于Python环境复杂度与PyTorch版本兼容性。

## Evidence

父节点级核验未通过：不完备（子节点1聚焦于依赖下载耗时，子节点2聚焦于安装/编译总耗时，两者维度不同且无矛盾，正交性良好。但父节点明确提到‘首次编译’耗时约为1-2小时，而子节点2中源码编译仅给出30-60分钟，未涵盖完整的1-2小时范围（可能遗漏了环境配置、依赖解析、CUDA工具链安装等其他关键耗时环节），导致完备性不足。此外，子节点1中的下载耗时包含在子节点2的总耗时中，存在包含关系但非重复，故不判定为冗余。）

## Search Query

vLLM TensorRT-LLM first time setup compilation time
