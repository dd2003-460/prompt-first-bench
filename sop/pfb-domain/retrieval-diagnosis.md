# 检索通道诊断 SOP

> origin: ai · 2026-11-15 · pfb 领域 SOP
> 触发条件：webllm/research_hook 超时、ERR_ABORTED、verified 率异常低（<5%）、或"调 timeout 没用"时，**第一步不是改参数，是诊断根因**。

## 核心原则：先诊断根因，再改参数

**为什么**：2026-11-15 教训——Perplexity 免费额度用完导致 webllm 超时，我反复调 timeout（90s→25s）没解决问题，因为根因是额度不是速度。ego-browser 手动操控一查才发现"您已达到免费搜索次数上限"。调参数永远修不了根因不对的问题。

**规则**：webllm 通道异常时，禁止直接改 timeout/retry 参数。先走下面的诊断流程，确认根因后再决定修法。

## 诊断流程（按顺序执行）

### Step 1: ego-browser 手动操控目标端点

```bash
ego-browser nodejs -e "
const browser = await globalThis.egoBrowser;
const page = await browser.newPage();
await page.goto('https://perplexity.ai/search?q=测试query', {timeout: 30000});
await new Promise(r => setTimeout(r, 45000));
const text = await page.evaluate(() => document.body.innerText.slice(0, 2000));
console.log(text);
await page.close();
"
```

**看什么**：
- "您已达到免费搜索次数上限" → **额度用完**，等重置或换通道
- "Login to continue" / 登录墙 → **需要登录**，ego-browser 持久会话有登录态，但 headless 实例没有
- 页面正常加载但无答案 → **JS 渲染问题**，检查选择器
- 网络错误 / ERR_ABORTED → **网络层问题**，检查 DNS/代理/防火墙
- 页面 404 / 502 → **端点挂了**，换端点

### Step 2: 区分 ego-browser 通道 vs 无头浏览器

**关键区别**（2026-11-03 诊断确认）：
- **ego-browser 持久会话**（ego-lite）：有登录态，能访问需要认证的页面
- **无头新实例**（Playwright/Chromium headless）：无登录态，遇到登录墙就挂

**判断方法**：ego-browser 手动操控成功但 pipeline 里 webllm 失败 → 检查 pipeline 用的是哪个浏览器实例。`research_hook.py` 的 `_run_ego_browser` 走的是 ego-browser CLI（持久会话），不是 headless。如果 pipeline 里换了 headless 实例，登录态就丢了。

### Step 3: 检查各通道独立状态

| 通道 | 检查方法 | 常见故障 |
|------|---------|---------|
| Perplexity | Step 1 手动操控 | 免费额度用完（几小时重置）、登录墙 |
| DDG lite | `curl -s "https://lite.duckduckgo.com/lite/?q=test" \| head -50` | IP 级 anomaly 封锁、中文 query 质量差 |
| zh-wiki | `curl -s "https://zh.wikipedia.org/api/rest_v1/page/summary/测试" \| head -20` | 零命中（覆盖不足）、条目质量差 |
| arXiv API | `curl -s "http://export.arxiv.org/api/query?search_query=all:test&max_results=3" \| head -30` | 不覆盖非学术域（社会事实/商业数据） |
| bing intl | `curl -s "https://www.bing.com/search?q=test" \| head -50` | 需实现 fallback（当前未接入） |

**规则**：至少 2 个通道独立验证，不能只看一个就下结论。

### Step 4: 检查缓存

```bash
# s5-node 缓存位置
ls -la /Users/a1-6/Desktop/workspace/pfb/experiments/stage-ablation/cache/ 2>/dev/null
# 缓存命中旧垃圾 → 清缓存
# 2026-11-12 教训：drb-2 清缓存前 verified≈0，清后仍≈0——但清缓存是必要步骤，不能跳过
```

**规则**：缓存命中旧数据会跳过真实检索。诊断时先清缓存再跑，排除缓存因素。

## 根因→修法映射

| 根因 | 修法 | 不能做的事 |
|------|------|-----------|
| Perplexity 额度用完 | 等重置（几小时）/ 换通道（bing intl）/ 接其他 LLM API / 升级 Pro（花钱） | ❌ 调 timeout（额度问题不是速度问题） |
| 登录墙（无头实例无登录态） | 用 ego-browser 持久会话 / 配置 API key | ❌ 换 headless 实例（更没登录态） |
| JS 渲染超时 | 加等待时间 / 换更轻量端点 / 用 API 替代页面抓取 | ❌ 只降 timeout（渲染需要时间，降了拿不到内容） |
| DDG IP 封锁 | 换 IP / 换通道 / 用 API | ❌ 加重试（IP 封锁不会因重试解除） |
| zh-wiki 覆盖不足 | 加内容质量过滤 / 接中文百科 API / 走 bing intl | ❌ 加更多 zh-wiki query（覆盖不足不是 query 问题） |
| 缓存中毒 | 清缓存 + 加 cache TTL | ❌ 只改检索逻辑（缓存不命中新逻辑） |

## 什么时候用 ego-browser 手动操控 vs 自动化 pipeline

| 场景 | 用哪个 | 原因 |
|------|--------|------|
| 诊断根因（"为什么超时"） | ego-browser 手动操控 | 交互式，能看页面实际状态（额度提示/登录墙/JS 渲染） |
| 验证端点可用性（"这个 URL 能不能用"） | ego-browser 手动操控 | 需要看渲染后的内容，requests 拿不到 JS-rendered 页面 |
| 批量检索（pipeline 里每节点调一次） | 自动化 pipeline（research_hook） | 手动操控太慢，不能塞进循环 |
| 验证修复是否生效 | 先手动操控确认 → 再跑 pipeline | 手动确认根因修了，pipeline 跑才有意义 |

**架构原则**：ego-browser 手动操控用于诊断和验证，自动化 pipeline 用于执行。验证过的方案再写进 research_hook。

## 已诊断过的案例

| 日期 | 症状 | 根因 | 修法 | 来源 |
|------|------|------|------|------|
| 2026-11-12 | drb-2 verified≈0 | 缓存中毒 + 检索通道对中文 DRB 题全盲 | 清缓存 + junk filter + bing intl fallback | s5-sm-bench-report.md §4 #3 |
| 2026-11-15 | webllm 每节点超时 90s | Perplexity 免费额度用完 | 等重置 / 换通道 / 接 API | s5-sm-bench-report.md §4 #6 |
| 2026-11-15 | webllm timeout 90s→25s 后仍超时 | 同上（额度问题不是速度问题） | 同上（调 timeout 无效） | s5-sm-bench-report.md §4 #5 |

## 禁止行为

1. **禁止在没诊断根因的情况下改 timeout/retry 参数**——这是 2026-11-15 的核心教训。
2. **禁止用 headless 浏览器替代 ego-browser 持久会话**——登录态会丢。
3. **禁止只看一个通道就下结论**——至少 2 个通道独立验证。
4. **禁止跳过缓存检查**——缓存中毒会掩盖真实检索状态。
