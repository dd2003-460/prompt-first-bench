# N116: vLLM 对 Qwen3-27B 的支持版本：vLLM 需在 v0.6.0 或更高版本中才正式支持 Qwen3 系列的架构注册（Model Architectu

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N43

## Claim

vLLM 对 Qwen3-27B 的支持版本：vLLM 需在 v0.6.0 或更高版本中才正式支持 Qwen3 系列的架构注册（Model Architecture: Qwen3ForCausalLM），低于此版本的 vLLM 无法加载 Qwen3-27B 权重，需升级 Python 环境及 pip 包。

## Corrected Claim

vLLM 需在支持 Qwen3 架构注册（Model Architecture: Qwen3ForCausalLM）的版本中才能加载 Qwen3-27B 权重，具体最低版本需查阅官方发布日志，通常高于早期 v0.6.x 版本。

## Evidence

[质询]具体版本号 v0.6.0 可能不准确，Qwen3 系列（特别是 Qwen3-27B 这种较新的模型）通常由更新的 vLLM 版本（如 v0.6.4+ 或 v0.7.x）引入支持，v0.6.0 可能尚未包含该架构注册。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且具体版本号属于经验参数，无法从第一性原理推导）

## Search Query

vLLM supported models list Qwen3 version requirement
