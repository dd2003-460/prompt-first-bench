# T-soc-arena-20261116 — SOC 缺口归因调研（arena 外包）

**origin: ai** · 派发: zero (Hermes) · 2026-11-16 · 目标仓库: dd2003-460/prompt-first-bench (main)

## 背景（最小必要）
pfb 的 S5 状态机跑中文社考（social-exam）消融臂，gate 要求 soc cov ≥ 0.898。
当前 checkpoint `experiments/stage-ablation/checkpoints/sm-soc-r1.json`：
verified=174, pending=77, degraded=31, total=283 → cov=0.615。
本地估算现实上限约 230/283=0.813（pending 77 中约 46 个 knowledge/given 类可翻 verified，degraded 31 中约 10 个可救回）。
卡死原因之一：webllm 检索通道（Perplexity/ChatGPT）全挂，search 类节点拿不到来源。

## 任务（回答三个具体问题，不开放式）
1. **来源类型**：中文社考量化断言（如"2020年中国人口14.1亿""GDP增速5.2%"这类）有哪些**可公开溯源**的数值来源？按可靠度排序列出类型（例：国家统计局公报、统计年鉴、教育部文件、权威媒体、教材），每类给 1 个具体可访问的 URL 示例。
2. **免费检索通道**：不用 API key、不用付费，哪些网页检索通道可程序化访问？逐个测可达性（curl 能拿到 HTML/JSON 就算通）：DDG html 端点、Bing、Wikipedia API、国家统计局网站、arXiv API。输出"通道 → 状态(通/断) → 证据(状态码或报错)"。
3. **上限交叉验证**：基于任务 1 的来源类型，判断"0.813 现实上限"这个估算合理吗？哪类节点（pending 77 / degraded 31）最可能有公开来源、哪类基本没有？给 conf。

## 约束
- 中文回答；每条结论标 conf(0-1)；给来源 URL；查不到的标"未验证"，禁止编造数字。
- 交付物格式：markdown，结构 = 三节对应三任务 + 末尾"核心发现 ≤10 行"。
- 长度 ≤80 行（过程论证删掉，只留结论+证据）。

## 交付（硬约束）
把结果写入本仓库 `experiments/stage-ablation/loop-artifacts/stages/arena-outsource/soc-gap-20261116.md` 并 push 到 main。
**文件不存在 = 任务未完成，Lead 不验收。**