# SOP · Arena 轻量审查（review / novelty check）

> 建立 2026-11-25。适用：纯质询/核验/撞车核查/审稿模拟，**不走 6 阶段研发 loop**。
> 与 `template-arena-task-brief.md` 的分工：那个是「派活让它产出工件」，这个是「派问题让它给判断」。

## 触发

用户说"交给 arena 审查/review/查撞车"，且任务不含代码工件产出 → 走本 SOP。

## 步骤

1. **落任务卡**：`tasks/<goal>/arena-review-brief-<date>.md`，四段式 `[任务][背景][必答问题][约束/交付]`。
   - 必答问题编号 Q1..Qn，**Q1 永远是 novelty 或最硬的那问**。
   - 明确要求：中文、每条 conf(0–1)、文献带 arXiv ID/DOI+年份、禁止编造、≤60 行、不复述背景。
2. **登录态门禁**：ego-browser 打开 arena.ai/agent，跑双重信号探针（`inSession && (composerVisible || repoPanel)`）。
   - 在 New Chat 首页发首条消息时 inSession 天然 false，以 composer 可见 + 邮箱已显示为准，记入回执。
   - 未登录 → handOff，不猜凭证、不静默塞字。
3. **派发**：新建 taskSpace → goto → fill composer → 确认落字 >50 → 点 Send。
4. **确认真开工**：snapshot 看 `Stop generating` / `Running commands` / 工具调用文本。**只 push 不发送 = 事故**。
5. **等待**：3 档超时 30s/1min/3min；超 3min 进降级阶梯（arena Battle → ego-browser 直抓 → 本地自答 conf−0.2）。
6. **落回执**：`tasks/<goal>/arena-review-receipt-<date>.md`，含 spaceId、会话 URL、发送时间戳、开工确认信号、回执全文（或全文路径）、 Lead 独立复核结论。
7. **收尾**：`finish({keep:[]})`。

## 纪律

- 不信汇报信证据：novelty 结论必须带可核验文献 ID；Lead 至少抽验 2 条。
- 不派"改稿"任务给 arena——本地做；arena 只做判断类。
- 降级阶梯每一级都要记原因，不得跳过直接本地自答。
