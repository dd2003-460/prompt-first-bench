# N368: Intel Gaudi 3 在 vLLM 框架中的官方支持状态为 'Experimental'，需使用特定版本的 vLLM 分支（如 intel/vllm-ga

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N130

## Claim

Intel Gaudi 3 在 vLLM 框架中的官方支持状态为 'Experimental'，需使用特定版本的 vLLM 分支（如 intel/vllm-gaudi），且针对 Qwen3-27B 的 FP8 量化内核需手动编译，该部署复杂度导致初始调试时间成本约 2-4 周，需查阅 Intel Gaudi 3 官方文档或 vLLM GitHub issues 确认最新兼容性列表。

## Corrected Claim

Intel Gaudi 3 在 vLLM 框架中的官方支持状态通常为 'Experimental'，需使用 Intel 维护的特定 vLLM 分支（如 intel/vllm-gaudi）。针对特定模型（如 Qwen3-27B）的 FP8 量化支持可能需手动编译或特定配置，部署复杂度较高，具体调试时间因环境而异，建议查阅 Intel Gaudi 3 官方文档或 vLLM GitHub issues 确认最新兼容性列表。

## Evidence

[质询]具体调试时间成本（2-4周）属于高度依赖团队技能和具体场景的经验性估计，缺乏通用标准，且‘需手动编译FP8内核’这一技术细节可能随vLLM版本更新而改变，存在时效性和主观性风险。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法验证具体版本分支名称及调试时长）

## Search Query

Intel Gaudi 3 vLLM Qwen3 FP8 support status experimental
