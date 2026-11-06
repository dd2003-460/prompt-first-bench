# 检索数据摘要（Q2: LLM 选型成本分析）

## Qwen3-32B (来源: Qwen3 官方博客)
- Context: 32,768 tokens (native), max_position_embeddings=40,960
- Parameters: 32B dense
- Quantization: supports FP8, INT8, INT4 (GPTQ/AWQ)
- VRAM requirement: ~64GB FP16, ~32GB INT8, ~16GB INT4

### Benchmark scores (from blog):
- Introduction Today, we are excited to announce the release of Qwen3, the latest addition to the Qwen family of large language models. Our flagship model, Qwen3-235B-A22B, achieves competitive results 
- document.addEventListener("DOMContentLoaded",function(){renderMathInElement(document.body,{delimiters:[{left:"$$",right:"$$",display:!0},{left:"$",right:"$",display:!1},{left:"\\(",right:"\\)",display
- Introduction Today, we are excited to announce the release of Qwen3, the latest addition to the Qwen family of large language models. Our flagship model, Qwen3-235B-A22B, achieves competitive results 
- Introduction Today, we are excited to announce the release of Qwen3, the latest addition to the Qwen family of large language models. Our flagship model, Qwen3-235B-A22B, achieves competitive results 
- DISCORDIntroduction#Today, we are excited to announce the release of Qwen3, the latest addition to the Qwen family of large language models. Our flagship model, Qwen3-235B-A22B, achieves competitive r

## Mistral-Small-3.1-24B (来源: HF Model Card)

## 通用参考
- API pricing (2026 typical): $0.3-3/1M input tokens, $0.6-15/1M output tokens (varies by provider/model)
- Local inference: RTX 4090 (24GB) can run 24B INT4 at ~30-50 tok/s; A100 (80GB) runs 32B FP16
- Power: 4090 TDP=450W, A100 TDP=400W; cloud GPU rental ~$0.5-2/hr
