# T8-matrix-run-r1（新域首跑）— 阶段 00 前置检查

> 创建：2026-10-30 · 阶段：00（common-review 前置检查）· 依据：`loop/prompt-first/00-common-review.md` + `tasks/T8-matrix-run-r1.md`
> 执行通道：**Lead 本地自答**（arena 通道未接入本 runner；同 T7.1 先例，conf-0.2 标注）。ralph web-llm 三 provider 登录态失效（回执见 §4），降级公开检索。

## 1. 目标可分解性

任务 = "选一个与机械键盘/会议室预约系统/GPU 硬件选型不同的新域，走完整 01→04.5（V-full），产出六阶段工件 + M8 计分表"。
- 交付物明确（六阶段工件 + m8-scorecard.md + design.md 回填）✅
- 验收标准逐条可判（current-goal.md §验收标准 9 条）✅
- 域选择本身是本 run 的一部分（任务书只约束"不复用三域"，未指定域）→ 域选择在 01 内完成并冻结 ✅

**判定：可分解。**

## 2. 域边界

| 项 | 内容 |
|----|------|
| 选定域 | **团队文件协作/网盘选型**（30 人研发团队，预算 ≤¥30,000/年，需 Web+macOS+Windows 客户端、版本管理、权限控制） |
| 排除域 | 机械键盘选购（T6 r1）、会议室预约系统（T7.1）、GPU 硬件选型（27b-hw-costperf） |
| 出域声明 | 不覆盖：办公套件整体迁移（Word/Excel 替代）、代码托管（GitHub/GitLab 属开发工具链，非文档协作）、IM 工具选型（飞书/钉钉整体平台作为候选类别出现，但其 IM 功能不在评估范围） |
| 与前两域的差异 | T6=硬件消费级、T7.1=SaaS 服务级、本域=**自托管 vs SaaS 混合决策**（开源 self-hosted 是真实候选类别，前两域无此结构）→ 对 V-full prompt 的"候选集冻结 + 未核验降级"机制是新压力测试 |

## 3. 环境降级登记

| # | 项 | 状态 | 处理 |
|---|-----|------|------|
| E1 | arena 通道 | 本 runner 未接入 arena.ai | Lead 本地自答，全程 conf-0.2 标注（同 T7.1） |
| E2 | ralph web-llm | 三 provider 全部 error（§4 回执） | 按 02 §2 记录失败后继续公开检索；02.5 "网页 LLM 结论是否被独立来源支持"一项不适用（无产物） |
| E3 | ego-browser | 可用（binary 存在）但依赖用户已登录浏览器会话；本 headless 环境无可见浏览器 | 不使用；动态页面改 curl/API |
| E4 | 出站网络 | github.com / api.github.com = 200；reddit = 403（bot-wall）；厂商官网可达性逐个实测（02 记录） | GitHub API 作一手源主力；官网直连受限时标 lead-unverifiable（F1 规则） |

## 4. ralph web-llm 失败回执（原样引用）

命令：`ralph prompt-first web-llm . "<域选择线索问题>" --context "阶段 02；只要求可复核来源线索"`
结果：`ok: true`，`successful_provider_ids: []`，`failed_provider_ids: [perplexity-review, chatgpt-review, gemini-review]`
错误详情（`loop-artifacts/prompt-first/02-web-llm-cross-check.md`，2026-10-29T20:18Z 生成——注意该回执为上一轮 runner 遗留，本轮沿用同一故障模式，02 阶段将重新调用并留新回执）：
- perplexity-review: "Perplexity prompt box is unavailable; login or UI changed"
- chatgpt-review: "ChatGPT prompt box is unavailable; sign in manually in the visible browser first"
- gemini-review: "Gemini prompt box is unavailable; sign in manually in the visible browser first"

**处置**：快速失败、未重试、未等待（符合 02 §2）。本 run 无任何"网页 LLM 线索"证据。

## 5. 阶段推进判定

00 pass → 进入 01。
