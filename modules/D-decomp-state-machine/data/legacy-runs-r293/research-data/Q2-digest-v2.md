# Q2 研究数据摘要 — LLM 选型成本分析

## 候选模型规格（来源标注）

### Qwen3-32B-Instruct
- 参数: 32B dense [来源: Qwen3 blog, qwenlm.github.io/blog/qwen3]
- Context: 32K native (40K with RoPE scaling) [来源: HF model card]
- 量化: FP8/INT8/INT4 均支持 [来源: Qwen3 blog]
- VRAM: ~64GB(FP16) / ~35GB(INT8) / ~18GB(INT4) [来源: 社区实测, artificialanalysis.ai]
- Benchmark (Qwen3 blog 报告): MMLU ≈ 78-82%, HumanEval Pass@1 ≈ 75-85% (依 prompt 格式) [conf: 0.7, 官方博客数字]
- 推理速度: RTX 4090 INT4 ≈ 25-35 tok/s; A100 FP16 ≈ 40-50 tok/s [来源: 社区基准测试, conf 0.6]

### Mistral-Small-3.1-24B-Instruct
- 参数: 24B dense [来源: mistralai HF org]
- Context: 32K [来源: model card]
- VRAM: ~48GB(FP16) / ~24GB(INT4) [来源: 计算推导]
- Benchmark: HumanEval ≈ 70-80%, MMLU ≈ 72-78% [来源: Mistral tech report, conf 0.7]
- 推理速度: RTX 4090 INT4 ≈ 35-45 tok/s (比 32B 快 ~30%) [来源: 社区, conf 0.6]

### DeepSeek-Coder-V2-Lite (16B)
- 参数: 16B MoE (2.8B active) [来源: DeepSeek blog]
- Context: 128K [来源: model card]
- VRAM: ~32GB(FP16) / ~10GB(INT4) [来源: 计算]
- Benchmark: HumanEval ≈ 75-85%, MBPP ≈ 70-80% [来源: DeepSeek tech report, conf 0.7]
- 推理速度: 极快（active params 少），RTX 4090 ≈ 60-80 tok/s [来源: 社区, conf 0.7]

### GLM-4-Air (9B)
- 参数: 9B dense [来源: THUDM]
- Context: 128K [来源: model card]
- VRAM: ~18GB(FP16) / ~6GB(INT4) [来源: 计算]
- Benchmark: HumanEval ≈ 60-70%, MMLU ≈ 65-72% [来源: GLM-4 tech report, conf 0.6]
- 推理速度: RTX 4090 ≈ 80-100 tok/s [来源: 社区, conf 0.7]

## 硬件成本参考
- RTX 4090 (24GB): 购买 $1,599; 云租赁 ~$0.8-1.2/hr (RunPod/Vast.ai) [来源: 2026 市场价格, conf 0.8]
- A100 80GB: 购买 ~$8,000-15,000; 云租赁 ~$2-4/hr [来源: 同上]
- 电力: 4090 TDP=450W → ~$0.05/kWh 时 ≈ $0.23/hr 满负载 [来源: 计算]
- 双卡 48GB 配置: 2×4090 ≈ $3,200 或 1×A100-80G ≈ $10,000+

## API 定价参考 (2026)
- GPT-4o: $2.5/1M input, $10/1M output [来源: OpenAI pricing page]
- Claude Sonnet: $3/1M input, $15/1M output [来源: Anthropic pricing]
- Qwen-Max (DashScope): ~$0.4/1M input, $1.2/1M output [来源: Alibaba Cloud, conf 0.7]
- DeepSeek-V3: ~$0.28/1M input, $0.42/1M output [来源: DeepSeek API, conf 0.8]

## 关键洞察
1. **质量-成本 tradeoff 的拐点**: 对于"函数级补全正确"任务，16B MoE (DeepSeek-Coder) 在代码任务上接近 32B dense 的水平，但速度快 2-3x
2. **本地 vs API 的 break-even**: 月调用量 > ~50M tokens 时，本地 4090 通常比 API 便宜
3. **合格率 P_valid 是最大变量**: 同样硬件，模型从 70%→90% 合格率，有效成本降 28%
