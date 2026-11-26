# Arena Loop 外包链路（SOP · 唯一入口）

> origin: ai · 2026-10-22 · D指令"链路核查 + arena 首选 + loop 双场景必需 + 精简 SOP + 新 SOP 复制到仓库给 arena 读"
> 本文件是外包 arena 任务的**唯一 SOP 入口**（goal 只索引这一个）。仓库/降级/loop 阶段细节已并入本文件，旧 `sop/arena-outsource.md` 与 `sop/loop-executor.md` 仅作存档指针，不再单独注入 goal。
> **部署**：创建目标仓库后，本文件必须复制进仓库 `sop/arena-loop-pipeline.md` 并 commit+push（与 loop/ 同次 push），arena agent 读仓库内的这份。

## 0. 优先级（硬规则 · D指令）

1. **Arena 外包 = 必须首选通道**：调研/核验/执行类任务，默认走 arena（LMArena agent mode）。不自己 AI 琢磨。
2. **Loop 全程必需 · 双场景**：无论 arena agent 在仓库里执行，**还是** arena 通道失败回退本地 Lead 自答，**loop 6 阶段（01→04.5）一个不少**。
   - 回退降级的是**执行通道**（arena → 本地），不是流程。**默认不降级，穷尽修复手段后才允许本地执行（§3.3 2026-11-06 修订）。**
   - 本地自答时 loop 工件仍落盘 `loop-artifacts/`，conf 标记 0.2。
3. 两者关系：**loop 是流程骨架（永远在），arena 是默认执行通道（首选，可降级）**。

## 1. 链路总览（6 步 + 每步断点 + 验证门禁）

| # | 步骤 | 断点 | 门禁（不过不进下一步） |
|---|------|------|----------------------|
| 1 | AI 启动 | — | goal 按 `sop/goal-template.md` §3 模板创建：含 SOP 索引（**只引用本文件**）+ 验收标准 |
| 2 | 注入 agents 原则 | — | 会话已加载 AGENTS.md/CLAUDE.md；goal 描述引用 goal-template §1 质量原则 |
| 3 | 阅读 arena 外包 SOP | — | 已读本文件；能说出当前任务对应仓库 |
| 4 | 复制 loop + 本 SOP 到目标仓库 + push | **断点 A**：workspace 未 commit/push 时，arena 拉到旧版/缺文件 | push 后在目标仓库验证：`ls loop/prompt-first/*.md` 7 个文件 + `sop/arena-loop-pipeline.md` 存在。**硬门禁：push 后必须在 workspace `projects/AI-计算科学/D1-persona-align/tasks/` 记录 commit hash + `git ls-remote` 输出到验证文件，否则断点 A 未过** |
| 5 | 发任务书 | **断点 B**：任务书未 commit/push 时 arena 读不到 | `git log -1 -- tasks/<id>.md` 有提交；arena 会话 `cat tasks/<id>.md` 成功 |
| 6 | arena agent 读 loop + 执行 | **断点 C**：arena agent 不知道要读 loop / 不知道在哪 | 任务书顶部强制段已写入（§2）；arena 首条消息引用了 loop 阶段路径 |

**回退分支**（步骤 6 故障）：arena 403/沙箱拦截 → 按 §3 降级本地自答，**loop 工件照常落盘**（conf-0.2），故障记 `knowledge/efficiency-bottlenecks.md`。回退不豁免 loop。

## 2. 任务书强制段（防断点 C · 必须写入 tasks/<id>.md 顶部）

```markdown
【执行前必读】
1. 本任务必须走 1-loop：先读 sop/arena-loop-pipeline.md + loop/prompt-first/00-common-review.md + 01..04.5（仓库内）。
2. 每阶段产出落盘 loop-artifacts/stages/<N>/，阶段判定 pass 才进下一阶段。
3. 完成后 commit + push（含全部 loop-artifacts/）。
4. 通道故障（403/沙箱）→ 报告 Lead，由 Lead 降级本地执行，不得静默跳过 loop。
```

## 3. 仓库映射 + 连接 + 失败降级（自 arena-outsource.md 并入）

### 3.1 选仓库（按任务选，不固定连一个）

| 任务类型 | 仓库 | 说明 |
|---------|------|------|
| decomp T4 消融 | `dd2003-460/decomp-bench` | 任务书在 `tasks/T4-arena-batch*.md`。**2026-11-02 r237：GitHub binding 失效（agent 侧 403 "Write access to repository not granted"，T7.2 会话 01a19a08 卡死于此）→ 需D在 arena UI 重绑 decomp-bench；T8 Part B 文献调研任务书已就绪 @ main c358b48（tasks/T8-partB-lit-survey-task.md），重绑后直接派发** |
| prompt-first 流程调研 | `dd2003-460/prompt-first-bench`（2026-10-22 建） | 任务书在 `tasks/` |
| 风格蒸馏 | `dd2003-460/persona-distill`（假设） | 任务书在 `tasks/` |
| 论文校对 | `dd2003-460/academic-AI`（假设） | 任务书在 `tasks/` |
| 媒体 pipeline | `dd2003-460/d1-media-pipeline`（假设） | 任务书在 `tasks/` |
| AI 视频复刻（像素剧/对标 B 站合集） | `dd2003-460/d1-video-recreation`（2026-10-26 确认，实际在用） | 任务卡在 `arena-prompts/batchN/`，SOP 在仓库 `sop/` |

**会话台账（一仓一会话 · r80 + D 2026-11-01 硬约束）**：外包调研允许用各种 AI（arena agent/Battle、网页 LLM），但**固定会话，不能乱开**——派发前必须先查此表复用该仓库的既有会话；仅当该仓库确无会话时才允许新开，且开完立即登记进本表。同一仓库出现两个活跃 arena 会话 = 违规（历史上下文分裂，任务书版本漂移）。

**judge 选择条款（pfb G2 F2(a)，2026-11-02 升格）**：多 judge 交叉打分必须异族隔离——同底座模型的两遍判定只算"上下文独立"不算"家族独立"，同源共享偏差无法靠加 judge 消除。κ 回执中 judge 族必须显式标注（如 "qwen3.8-27b ×2, non-IRR"）；宣称真 IRR 需 ≥2 不同底座。

| 仓库 | 当前 arena 会话 | 备注 |
|------|----------------|------|
| **（活跃表已拆出）** | `sop/arena/active-sessions.md` + `sop/arena/sessions.json` | 派发前查这两处；历史详情 `sop/arena/session-history.md`（2026-11-20 拆出，防台账膨胀） |

**原则**：每个项目有自己的仓库，arena 连接对应仓库，读仓库内的任务书执行。不跨仓库混用。

### 3.2 连接仓库（新会话直接选仓库 · 2026-10-26 修正）

> **修正**：arena.ai/agent **新会话可以直接切换/选择仓库**（用户实证：新开会话 easily 切到 d1-video-recreation，会话 01a17723）。旧认知"账号级 OAuth 绑定 pfb、UI 无切换入口"已作废。

1. **★ 选对仓库是第一原则**：开新 arena 会话时，按 §3.1 映射表选目标仓库直连，不走 pfb 中转。
2. GitHub App 授权保持 "All repositories"（含私有），保证所有仓库可访问
3. pfb 中转仅用于历史遗留（batch-11 及之前的分支产出需提取清扫）

**验证**：`git ls-remote https://github.com/dd2003-460/<repo>.git HEAD` 返回 hash = 可达（权限本身在 arena 会话内验证）。

### 3.3 失败降级

| 故障 | 诊断 | 降级方案 |
|------|------|---------|
| git clone 403 | `curl -s -o /dev/null -w '%{http_code}' https://github.com` 测网络 | ① 用 GitHub REST API（Contents API）读写文件 ② 上传任务书到对话本机执行 ③ Lead 本地自答（conf-0.2，loop 工件照常落盘） |
| token 过期 | `git ls-remote` 测权限 | 重新 OAuth 授权 / 用 `gh auth token` 生成新 token |
| arena 沙箱拦截 git | `curl https://api.github.com` 通但 `git clone` 不通 | 用 GitHub REST API（不走 git） |

**降级原则（2026-11-06 D修订）**：

1. **默认不降级**。arena 是首选通道，故障时必须先穷尽修复手段再考虑本地执行。
2. **修复清单**（按顺序尝试，全部失败才允许降级）：
   - ⓪ **登录态探针**（必跑第一步）：ego-browser 打开目标会话页，跑 arena-outsource skill「登录态判定门禁」的标准探针脚本。`inSession && (composerVisible || repoPanel)` 不满足 = 未登录/会话不存在 → 停止派发，报告"arena 无有效登录态，需人工登录"，禁止把营销页/登录墙当可用状态
   - ① `curl -I https://arena.ai` 确认网络通
   - ② ego-browser 重新 goto arena.ai/agent（会话页面可能过期）
   - ③ 查 ego-lite 进程是否活着（`ps aux | grep -i ego`），死了就重启
   - ④ 换 taskSpace 名开新会话（旧 space 可能僵尸）
   - ⑤ 检查 GitHub App token 权限（`git ls-remote` 测写权限）
   - ⑥ 若沙箱拦截 git → 用 GitHub REST API（Contents API）替代
   - ⑦ 仍失败 → 记录具体报错（哪条链路 + 什么错误码），等下一个 keepalive 周期重试
3. **降级条件**：以上 7 步全部失败 + 连续 2 个 keepalive 周期重试无效 → 才允许 Lead 本地自答（conf-0.2，loop 工件照常落盘）。
4. **降级后必须修复**：降级不是终点。每次降级后立即在 `knowledge/efficiency-bottlenecks.md` 记录故障根因 + 修复计划，下一个可用周期优先尝试恢复 arena 通道。
5. **禁止静默降级**：不得因为"本地也能跑"就直接跳过 arena。只有确认所有方法都试过且不可修复时，才允许本地跑。

## 4. loop 阶段速览（自 loop-executor.md 并入 · 逐段定义见仓库内 loop/prompt-first/）

6 阶段，每阶段读对应 `loop/prompt-first/<阶段>.md` → 产出落盘 `loop-artifacts/stages/<N>/` → 判定 pass/revise：

| 阶段 | 产出 |
|------|------|
| 01 目标分解 | decomposition.md（正交+覆盖+边界+已知vs空缺+递归到原子） |
| 02 信息调研 | research.md（GitHub→arXiv→ego-browser→自答；每条 claim 带来源+conf） |
| 02.5 交叉验证 | crosscheck.md（关键结论 ≥2 LLM；矛盾记录） |
| 03 行动分解 | actions.md（依赖+并行标注+执行级原子化） |
| 04 执行验证 | execution-log.md（per-step 备份→执行→review→提交） |
| 04.5 反方复核 | review.md（找矛盾+验证假设） |

**约束**：每阶段产出必须落盘；判定基于工件内容不是感觉；任务卡 ≤50 行；每读 N 个文件先写 checkpoint。

### 4.1 复制 + push 命令模板（断点 A）

目标仓库是独立 git 仓库（含 `loop/ sop/ tasks/ rubric/`），workspace 是源。已验证先例：`dd2003-460/prompt-first-bench`。

```bash
# 本地浅克隆目标仓库（已存在则 git -C <dir> pull）
git clone --depth 1 https://github.com/dd2003-460/<repo>.git /tmp/<repo>
# 同步 workspace 的 1-loop 阶段文件 + SOP（只同步 prompt-first/，workspace loop/ 其他子目录不属于仓库）
rsync -av --delete /Users/a1-6/Desktop/workspace/loop/prompt-first/ /tmp/<repo>/loop/prompt-first/
cp /Users/a1-6/Desktop/workspace/sop/arena-loop-pipeline.md /tmp/<repo>/sop/
# 记录验证证据 + commit + push
git -C /tmp/<repo> add -A && git -C /tmp/<repo> commit -m "sync: loop/prompt-first + sop (workspace $(date +%Y%m%d))"
git -C /tmp/<repo> push && git ls-remote https://github.com/dd2003-460/<repo>.git HEAD
```

说明：rsync `--delete` 保证仓库 `loop/prompt-first/` 与 workspace 完全一致（6 个阶段文件 + examples/ 示例子目录，2026-10-26 外移）；**不要 rsync 整个 workspace `loop/`**（含 archived 等与 arena 无关的内容）。sop 只复制本文件。push 后把 commit hash + ls-remote 输出写进 tasks/ 验证文件（§1 断点 A 硬门禁）。

## 5. goal 模板引用

所有外包 arena 的 goal，目标描述包含：
```
按 `sop/arena-loop-pipeline.md`（仓库内）/ `sop/arena-loop-pipeline.md`（workspace）流程执行：
1. 选仓库：<repo>
2. 复制 loop/ + 本 SOP 到仓库 + push（断点 A 门禁）
3. 发任务书（含强制段）+ push（断点 B/C 门禁）
4. arena 执行 + 评分 + push
5. 失败降级：按 §3.3（loop 不豁免）
```

## Battle 投票 = 免费的多模型打分器

R5.2-third-scorer / RV3G4-kappa-gate-execution 类"需要不同模型家族独立打分"的阻塞项，可用 battle 通道解：

1. ego-browser 打开 lmarena.ai（已登录态），新建 chat
2. 把同一份盲打材料（如 packet v2 三 run 评分任务书）发给 battle
3. 两个匿名模型各自独立作答（上下文天然隔离，互不可见）
4. **必须投票**（选 A 好/B 好/平局均可）→ 页面揭晓双方真实模型名
5. 记录：模型名 + 完整回答文本 → 落盘 `bench/rubric-v3/scorers/<date>-battle-<id>.json`
6. 每轮新会话（不污染上下文）；N 轮得 N×2 个模型家族的独立分数
7. 收齐 ≥3 个不同家族后算 Fleiss'κ（消费 assert-kappa-receipt.py schema）

### 硬约束

- 投票是揭晓模型名的唯一途径，不投票 = 白跑
- 记录时必须存原始回答全文（不是摘要），后续复算要用
- 同一份材料发多次 = 多个独立样本，但同一模型家族只取一次（防重复计数）
- 自动化限制：battle 页面的发送/投票按钮用 ego-browser JS 事件派发（同 GPT 侧套路）；若菜单/按钮触发失败，降级为半手动（我准备好材料，D点两下）

## 结果核验

- agent mode：不信汇报信 git（fetch 显式 refspec → log → show 文件 → 独立复算数字）
- battle mode：核对揭晓的模型名与记录一致；回答文本 sha256 入库；分数复算和原文对账

## 7. 维护补充（2026-10-30）

- 新增 battle 通道实操细节（ego-browser 选择器、投票按钮定位、揭晓页解析）→ 补进本文件 §Battle 节 + skill `arena-outsource` references
- 每次 battle 打分轮次 → 台账登记（日期/模型对/材料 hash/落盘路径）

## 8. 维护

- 新增仓库 → 更新 §3.1 映射表
- 新增链路断点（实际断裂案例）→ 更新 §1 表格 + 记 qanda-ledger
- 故障修复 → 更新 §3.3
- 本文件变更 → commit + push（workspace + 已部署的目标仓库同步）
