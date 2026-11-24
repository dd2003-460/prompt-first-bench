# T-PR-17 pilot 搜索后端降级记录（rep 同质性核验）

# origin: ai · 2026-11-25 05:27 · 确定性日志核验（不碰 vLLM）

## 发现
pilot 全程（11-24 原 run → 11-25 resume）搜索后端持续降级：
- `WEBLLM-BROKEN all endpoints failed` + `DDG-BROKEN consecutive failures` 在三个时段都出现：
  - 11-24 原 pilot 报告（tpr17-pilot-report-20261124-213055.md）L745/746/2165
  - 11-25 resume 日志 r2 段 L753/767
  - 11-25 resume 日志 r3 段 L11600/11601（当前）
- 即 r1（03:15 落盘）/ r2（04:58 落盘）/ r3（在跑）三个 rep 在**相同的搜索降级条件**下运行。

## 判定
- **rep 同质性：OK**——降级对三 rep 一视同仁，不引入 rep 间异质性。
- **实验条件：需在最终分析中标注**——s5 管道的 web 搜索组件在整个 pilot 窗口内失效，节点来源 = LLM 生成 + `.research-cache` 缓存命中（resume 日志 CACHE-HIT=84，r3 段 1）。这是"无 live search"条件下的 4-arm 消融，结论外推到"有 live search"时需另验。
- 与 gpt-researcher 臂 0 结果根因（ddgs→mojeek 被封，commit 4af5aac23）同源：本机网络层对 ddgs/mojeek/perplexity/chatgpt-web 端点封锁。

## 影响面
- canonical/verify-off/null-control 三臂都走同一 s5 管道 → 同条件，arm 间对比有效。
- gpt-researcher 臂（外部参照）已修 bing 后端，跑法不同——本就是独立参照臂，不要求同条件。

## 核验命令（可复现）
```
grep -n 'BROKEN' modules/B-pipeline-ablation/data/tpr17/tpr17-pilot-resume-20261125-033733.log
grep -n 'BROKEN' modules/B-pipeline-ablation/data/tpr17/tpr17-pilot-report-20261124-213055.md
```
