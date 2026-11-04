# Battle 投票通道（免费多模型打分器 · 冻结自 sop/arena-loop-pipeline.md v1）

> 用途：需要「不同模型家族独立打分」时的阻塞项（R5.2-third-scorer / RV3G4-kappa-gate 类）。
> 本文件**不参与注入**，只在决定用 battle 通道时读。主 SOP §5 有 3 行指针。
> R7 冻结日期：2026-11-04。

---

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
- 自动化限制：battle 页面的发送/投票按钮用 ego-browser JS 事件派发（同 GPT 侧套路）；若菜单/按钮触发失败，降级为半手动（我准备好材料，成璐点两下）
