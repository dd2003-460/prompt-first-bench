# 任务：GPT-Researcher 三题 × 3 rep（官方参数）

## 环境
- 工作目录：/Users/a1-6/Desktop/workspace/pfb/experiments/stage-ablation
- Python：.venv-d1/bin/python（3.12.13，gpt_researcher 0.16.1）
- 模型：qwen3.8-27b @ http://127.0.0.1:8787/v1
- 检索器：arxiv（ddg/mojeek 网络不通）

## 执行命令
```bash
cd /Users/a1-6/Desktop/workspace/pfb/experiments/stage-ablation
.venv-d1/bin/python -u gptr_official_3q.py
```

## 参数（gpt_researcher 0.16.1 官方默认 + 深度研究加宽加深）
| 参数 | 值 | 备注 |
|------|-----|------|
| temperature | 0.4 | 官方默认 |
| max_iterations | 3 | 官方默认 |
| max_search_results_per_query | 5 | 官方默认 |
| total_words | 1200 | 官方默认 |
| max_subtopics | 3 | 官方默认 |
| deep_research_breadth | **6** | 官方默认 3，D 指令加到 6（深度研究最好 baseline） |
| deep_research_depth | **6** | 官方默认 2，D 指令加到 6 |
| deep_research_concurrency | 4 | 官方默认 |
| fast_token_limit | 6000 | 官方默认 |
| smart_token_limit | 12000 | 官方默认 |
| strategic_token_limit | 8000 | 官方默认 |

## 三题
1. **nat**：CDN 缓存命中率（LRU/LFU/Pareto 工作负载）
2. **soc**：二手交易平台均衡分析
3. **gpu**：本地推理 Qwen3-27B 选卡方案

每题 3 次独立重复（共 9 runs），串行执行。

## 输出
- 报告：`runs-gptr-official/{qid}-r{rep}.md`
- 汇总：`runs-gptr-official/summary.json`

## 验收
- 9 份 .md 报告存在且 > 500 chars
- summary.json 含 9 条记录（elapsed_s > 0）
- 无 FAILED 条目（如有 FAILED 记录原因）

## 预计耗时
每 run 约 3-8 分钟（取决于搜索+LLM 响应），9 runs 串行 ≈ 30-70 分钟。
