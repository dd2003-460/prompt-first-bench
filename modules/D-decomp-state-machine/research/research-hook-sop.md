# SOP: S5 多通道检索基础设施（research_hook v3）

> origin: ai（2026-11-16 D 指令落盘：搜索基础设施的 SOP 和 skill 缺失，补上）
> 状态：现行。代码 `s5_pipeline.py` + `research_hook.py`（pfb/experiments/stage-ablation/）。
> 本文件是**操作手册**：改检索行为前先读这里，改完回来更新。

## 1. 架构总览

```
search_node(node, qid)            s5_pipeline.py L349
  ├─ source ∈ {given, knowledge} → 不检索，直接返回 []（P3 走逻辑核验）
  └─ source == search → research_hook("s5-node", query, ...)
        │
        ▼
research_hook(qid, question)      research_hook.py L913
  cache-first (.research-cache/)
  通道按序填充，总数 ≤ max_results：
   1. local_corpus   本地语料 grep（仅 gpu 题；nat/soc 禁用防污染）
   2. wikipedia      公网 API ~1.5s
   3. ddg            DDG lite 中文/英文搜索 ~2-4s
   4. web_llm        Perplexity via ego-browser ~15-25s（前 3 通道 <3 条才触发）
   5. arxiv          学术 API（s5-node 级跳过；题级用 ARXIV_QUERIES）
   6. webfetch       纯 HTTP 抓 KNOWN_SITES 已知站点
   7. direct_site    ego-browser 深抓 JS 渲染页（最后兜底）
  过滤：_BAD_ANCHOR 跳转链接 + _JUNK_PATTERNS 垃圾源 + 白名单域名匹配
  全空 → raise ResearchHookUnavailable
```

**关键设计决策（为什么这样）**：
- given/knowledge 节点**不走检索**：题面给定和模型先验知识只需逻辑自洽核验，硬要搜只会引入噪声（soc r1 膨胀事故就是反例——r1 那轮把 search 节点也判成 knowledge 式"逻辑过"，verified 虚高到 174）。
- nat/soc 禁用 local_corpus：语料库只有 D1-gpu-research，grep 命中全是无关 GPU 文档，会污染 P3 核验（nat 100 reps evidence 里大量出现"来源与节点无关"）。
- s5-node 级跳过 arXiv：节点 query 是 L2/L3 子维度（如 "GPU depreciation rate"），查 arXiv 只捞回无关论文。

## 2. 中文 query 策略（2026-11-15 修，soc 106 节点全空的根因修复）

claim 含中文 → **先用中文 claim 查**（DDG 对中文有真实召回：搜狐/今日头条/知乎/央行数据）；中文全空才用英文 search_query 兜底。
反面教训：英文 query 查 wiki 返回英文条目，与中文 claim 完全无关 = 假来源。

## 3. 白名单与垃圾过滤

- `_SOURCE_WHITELIST`（L37）：可信域名列表。2026-11-16 扩了 18 个中文域（知乎/搜狐/新浪/北大等）。
- `_JUNK_PATTERNS`：drb-1 诊断后加的垃圾模式（色情视频/游戏/翻译工具/股票行情）。
- **已知局限（实测 2026-11-16）**：长尾中文 query（如"二手平台 挂价 高于成交价 15% 成交周期 变短"）DDG/Bing 都 0 召回——搜索引擎对这种具体数值型 claim 没有索引，不是白名单问题。这类节点的 verify_node 判 degraded 是**正确行为**，不要为了凑 cov 放宽白名单或造证据。

## 4. 缓存纪律

`.research-cache/` 按 (qid, question) 稳定键存结果。**改了白名单/垃圾过滤/通道逻辑后必须清缓存重跑**——否则新逻辑读的是旧结果（"同一结果反复出现 → 可能在读缓存"，执行纪律第 7 条）。
清法：`rm -rf .research-cache/`（run 前做，留痕在 run 日志第一行）。

## 5. 失败降级链（每个环节的行为）

| 环节 | 失败表现 | 下游行为 |
|------|---------|---------|
| 单通道异常 | 该通道静默跳过（try/except pass） | 其余通道继续填 |
| 全部通道空 | raise ResearchHookUnavailable | search_node 返回 ([], err) → sources_block 显示"(本轮检索无可用来源)" |
| P3 收到空来源 | LLM 只能凭逻辑判 | status ∈ {verified(逻辑自洽), degraded, failed}；evidence 里应写明"无外部来源" |
| P3 解析失败 | status 不在三值内 | 强制 degraded（保守档） |

**红线**：degraded 不许被脚本批量翻成 verified。cov 数字只能来自真实的 P3 判定输出。

## 6. 运维检查清单（run 前 30 秒）

1. `ls -la .research-cache/ | head` — 确认是否要清（改了检索代码就必须清）
2. `curl -s 'https://lite.duckduckgo.com/lite/?q=test' | head -c 200` — DDG 通不通
3. `python3 -c "import research_hook as rh; print(len(rh._SOURCE_WHITELIST))"` — 白名单加载正常
4. 起 run 用 `setsid nohup python3 ... > log 2>&1 &`，PID 写进 goal state（长跑进程纪律）
5. run 中盯 `[RESEARCH-GAP]` / `[WEBLLM-SKIP]` stderr 行 — 出现密度高 = 通道大面积失效

## 7. 已知边界（别当 bug 修）

- **数值型 claim 无公开来源**：二手平台微观数据、损失厌恶系数统计值这类，全网就没有公开发布的具体数字。verify 判 degraded 是对的。bench report 里如实写"领域证据稀薄"，这是 bench 的真实发现，不是管线缺陷。
- **web_llm 通道依赖 ego-browser 登录态**：ego-lite 会话掉线时该通道静默失败（[WEBLLM-SKIP]）。恢复 = 桌面端重新登录 ego lite，不改代码。
- **cov 上限由题目决定**：nat 0.651 / soc 0.898 gate 里，knowledge/given 类节点占大头，search 通道贡献是边际的（nat 176/181 verified 里 search 只 5 个）。想提 cov 的正确路径是把 pending 核完，不是堆搜索通道。

## 8. 改动记录

| 日期 | 改动 | 原因 |
|------|------|------|
| 2026-11-09 | nat/soc 禁 local_corpus；s5-node 跳 arXiv | 无关语料污染 P3 |
| 2026-11-12 | _JUNK_PATTERNS 垃圾过滤 | drb-1：75% 节点 degraded 源于垃圾源 |
| 2026-11-15 | 中文 claim 优先中文 query | soc 106 节点 retrieval_sources 全空 |
| 2026-11-16 | 白名单 +18 中文域 | 中文来源被过滤丢弃 |
| 2026-11-16 | 本 SOP 落盘 | D 指令：搜索基础设施缺 SOP/skill |