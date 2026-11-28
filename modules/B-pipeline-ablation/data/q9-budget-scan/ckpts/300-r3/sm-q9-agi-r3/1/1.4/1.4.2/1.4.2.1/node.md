# N156: V100 (CC 7.0) 缺乏原生 FP8 张量核心支持，vLLM 在 CC 7.0 上启用 FP8 配置时的行为是：若检测到硬件不支持，则回退至 FP16 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N45

## Claim

V100 (CC 7.0) 缺乏原生 FP8 张量核心支持，vLLM 在 CC 7.0 上启用 FP8 配置时的行为是：若检测到硬件不支持，则回退至 FP16 路径，或在某些版本中抛出 RuntimeError 拒绝启动；不存在'强制转换为 FP16/INT8 以保持运行'的静默降级机制，需查阅 vLLM 源码中 `model_runner.py` 或 `quantization/` 模块的 `check_supported` 逻辑以确认具体报错或回退行为。

## Corrected Claim

V100 (CC 7.0) 缺乏原生 FP8 张量核心计算单元。在标准 vLLM 版本中，启用 FP8 量化通常会导致启动失败或回退至 FP16/BF16，因为硬件不支持 FP8 GEMM。然而，特定优化分支（如 1Cat-vLLM）可能允许在 KV Cache 等特定环节使用 FP8 存储格式（如 E4M3），但这不等于拥有原生 FP8 计算加速。具体行为需查阅对应版本的源码。

## Evidence

[质询]参考来源 [1] 显示存在针对 V100/SM70 的特定 vLLM 分支（1Cat-vLLM），其摘要明确提到将 `--kv-cache-dtype fp8` 解析为 E4M3 并选择 `fp8_e4m3` 配置，这暗示在该特定工程分支中可能存在某种形式的 FP8 支持或模拟，从而挑战了原陈述中关于“缺乏原生支持”及“必然回退/报错”的绝对性描述，尽管主分支 vLLM 确实如此，但原陈述未区分官方主分支与特定 Fork 的行为差异。 | 逻辑上 V100 (CC 7.0) 确实缺乏硬件 FP8 Tensor Core，主流 vLLM 行为符合描述；但来源 [1] 提供了间接证据表明存在针对 SM70 的特定实现路径（如 KV Cache 使用 FP8 格式），使得“不存在任何 FP8 配置行为”的断言过于绝对，故降级。

## Search Query

vLLM V100 compute capability 7.0 FP8 support fallback behavior source code

## Retrieval Sources

- {'url': 'https://github.com/1CatAI/1Cat-vLLM&rut=e21f452280349e4ca8214b0017ee74bc012180a2a1b0964fdcc6381b4b2a0ab7', 'type': 'ddg', 'title': 'GitHub - 1CatAI/1Cat-vLLM: V100 / SM70-focused vLLM engineering fork ...'}
