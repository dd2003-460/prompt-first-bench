# Goal: RV3B1-prompt-side-freeze — D2 边界类型声明段写入 prompt + V3 sham 化联动（batch2 R-09 前置）

> 创建：2026-10-30 · ralph loop runner（queue 队首未完成项，纯仓库内无外部依赖）
> 依据：`tasks/goal-queue.md` 候选条目「RV3B1-prompt-side-freeze (batch2 R-09 前置)」+ batch1 revision-log 诚实保留 #5 + DRAFT-rubric-v3-v2.md L154-161（D2 冻结 diff 段）/ §3.2 变体矩阵 / §4.3 sham 先例
> 状态：阶段 01-03 工件已存在（loop-artifacts/stages/{01,02,02.5,03}/RV3B1psf-*，02.5 verdict pass），本轮从 04 执行续跑

## 【目标】
V3-noboundary 消融开跑前的流程动作落地：
1. **A1**：D2 段正文 6 行（DRAFT v2 L155-L160）逐字写入 `loop/prompt-first/02.5-cross-check.md` 文末附录区（标题显式声明「非本 loop 规则」，防 A1 攻击的误读风险）
2. **A2**：DRAFT v2 §4.3 之后新建 §4.4 V3-sham 替换段——引用/脚注格式规范主题，代码块内 6 行正文，总字符数与 D2 正文偏差 ≤10%，不含边界类型三类语义 token
3. **A3**：§3.2 变体矩阵 V-sham 行后插入 V3-sham 行；既有六行零改动
4. **A4**：L164 `[batch2: R-09]` 占位符更新为「部分落地」状态
5. **A5**：新建 `bench/rubric-v3/ablation/scripts/assert-psf-freeze.py`（byte-exact + 定点断言 + 等长机判 + 黑名单），exit 0 + 变异测试
6. **A6**：revision-log 登记 R-09 部分落地
7. **A7**：04 执行日志 + 04.5 反方复核 + per-goal web-llm 回执（已存在，沿用）

## 【阶段】
rubric-v3 正式实验开跑前置环。纯仓库内文本工作，不改任何冻结数据（prior-estimates.json / judge-blindtest-r1.json / hit-matrix.json / stats-* 只读）。工作量小。

## 【SOP 索引】
- `sop/arena-loop-pipeline.md`（唯一 SOP 入口）
- `loop/prompt-first/00..04.5`（六阶段定义）
- `bench/rubric-v3/DRAFT-rubric-v3-v2.md`（修订对象：§3.2 / §4.3-4.4 / L164 占位符 / revision-log）
- `loop/prompt-first/02.5-cross-check.md`（A1 落点）
- 既有 01-03 工件（判断 J1-J4 已预注册，04 按 03 行动表执行不重新决策）

## 【验收标准】
- [ ] 02.5 附录段与 DRAFT v2 L155-L160 byte-exact（assert 检查①）
- [ ] §3.2 含 V3-sham 行且既有六变体行文本不变（assert 检查②）
- [ ] §4.4 存在 + 行数 = 6 + 字符偏差 ≤10% + 黑名单 token 零命中（assert 检查③）
- [ ] assert-psf-freeze.py exit 0 + 变异测试确认实义生效
- [ ] L164 占位符更新（grep 定点）
- [ ] revision-log 登记 R-09 部分落地
- [ ] 定性结论零改动：V3-noboundary 定义本身不动；冻结数据零修改（git status 验证）
- [ ] 04.5 反方复核 verdict pass

## 【失败降级】
- §4.4 凑等长反复失败 → 放宽到「行数 ±1 + 字符偏差 ≤15%」并同步改 assert 阈值 + 04.5 登记（不静默改）
- 发现 DRAFT v2 实际行号与 02 工件盘点不符 → 以文件实际内容为准重定位，04 日志记录差异
- web-llm 三 provider 登录态失效 → 沿用 unverified 降级（本 goal 证据链仓库内闭合，边际贡献 ≈ 0）
- claude max-turns 耗尽未收口 → 留断点工件，runner 下轮从断点续跑（同 RV3B1psf 当前状态模式）