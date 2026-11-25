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

## 追加：10:20 逐通道探活（pilot 结束后、队列 STEP1 进行中）

逐通道直连测试（纯 HTTP，不碰 vLLM）：

| 通道 | 状态 | 证据 |
|---|---|---|
| wikipedia API | **429 Too Many Requests** | `curl https://en.wikipedia.org` = 301（首页可达）但 API 查询 429（换 UA 也 429）→ 本机 IP 被 API 级限流，疑似 pilot 整夜高频查询触发 |
| arXiv API | **429** | http/https 均 429 |
| DuckDuckGo | **SSL EOF** | `URLError: EOF occurred in violation of protocol` |
| webllm（perplexity/chatgpt-web 等） | **全挂** | 队列 STEP1 开头 `[WEBLLM-BROKEN] all endpoints failed` |
| bing.com / cn.bing.com | **HTTP 200 但区域化垃圾** | 直连返回 ~10-20 结果但全是日本区推广（google.co.jp/adwords）；`_bing_search` 解析正常（n=3）但内容无用 |

**根因分层**：
1. `_probe_network` 探针本身**通过**（wikipedia 首页 301 → healthy=True）——所以不是探针短路问题，10:20 一度怀疑的"探针挡 bing"排除。
2. 真根因 = **本机出口 IP 被 wikipedia/arxiv API 限流（429）+ ddg 连接层封锁 + webllm 端点全挂**，与 05:27 记录的"本机网络层封锁"同源且加重（新增 API 级 429 限流）。
3. bing 是唯一 HTTP 层存活通道，但地域化为日本区 → 对英文技术查询无有效结果。

**对队列 4 步的影响**：
- STEP1 L4-disambig：主判读（4 卡是否出现）**不依赖搜索**——预注册设计把候选固定为 5 类正是消歧的一部分；搜索降级只伤 verify 取证（corrected_claim 预期=0，同 pilot）。实验有效，结论带"无 live search"caveat。
- STEP2 gptr / STEP3 J4 / STEP4 ArmC：取证质量同样受限；gptr 有 pfb_retriever 多通道但底层同受 429/EOF 影响。
- **决策：不中途改 research_hook.py**（队列在跑，改了会造成 STEP1 无搜索 vs STEP2-4 有搜索的队列内口径不一致 = 新 confound）。修复（bing 区域化/429 退避/换端点）等队列 DONE 后统一做。

**修复方向（队列 DONE 后）**：
- ~~bing 通道加 `&setmkt=en-US&mkt=en-US` 强制美国区~~ **已测无效（10:40）**：`mkt=en-US&setmkt=en-US` 下 bing 返回美国公寓网站广告（Summer Place Apartments），`setlang=en` 下返回日本 Google 地图——**两种参数都是无关垃圾**。结论：不是参数问题，是 **IP 级质量降级**（本机出口 IP 被所有搜索后端喂垃圾/广告），mkt 参数救不了。
- 429 通道加指数退避 + 请求间隔（pilot 连续查询无节流是限流诱因）；
- 考虑把 `_probe_network` 探针从 wikipedia 换成 bing（当前探针端点和被限流的 API 端点是同一个域，首页可达≠API 可用，探针语义已失真）。
- **根本出路**：~~换出口（代理/服务器端）~~ **已排除（11:00 实测）**：LAN 服务器 10.20.33.188 出口更差（wiki API 000 连接失败、ipify 空），无干净出口可用。**最终决定：接受"无 live search"为实验条件**——当前 4 个排队实验（队列 STEP1-4 + T-REPAIR-1 4 臂）都按此条件跑，判读时统一带 caveat；臂间对比不受影响（同条件），跨批对比（vs 11-23 前的 K7/Q6 基线）需注意搜索质量漂移。

**核验命令（可复现）**：
```
curl -s -m 8 -o /dev/null -w "%{http_code}" https://en.wikipedia.org          # 301（首页 OK）
curl -s -m 8 -o /dev/null -w "%{http_code}" "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=test&format=json"  # 429（API 限流）
curl -s -m 8 -o /dev/null -w "%{http_code}" https://www.bing.com              # 200
python3 -c "import sys; sys.path.insert(0,'.'); import research_hook as RH; print(RH._bing_search('RTX 3090 memory bandwidth', 3))"  # n=3 但日本区垃圾
```
