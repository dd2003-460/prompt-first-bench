# PFB 专属 Arena 外包

> origin: ai · 2026-11-07 · pfb 领域 SOP
> 为什么需要这份文件：arena 是 pfb 的主要执行通道（调研、核验、gold 构建都走 arena）。但 arena agent 不知道 pfb 的上下文——它看到的是一个 GitHub 仓库 + 一段任务书。任务书写得不好，arena 就会在错误的方向上忙活半天。这份文件定义"怎么给 arena 写任务书让它一次做对"。

## 通用规则（继承自 sop/arena-loop-pipeline.md）

- 派发前门禁五条：台账 / 远端分支 / 会话绑定 / prompt 仓库声明 / 回执指纹
- 结果核验：不信汇报信 git（fetch → log → show → 独立复算）
- 完整 SOP 见 `sop/arena-loop-pipeline.md`（本文件只补 pfb 特有部分）

## PFB 任务书模板

```markdown
# T<N>: <一句话目标>

## 背景（arena 不知道的部分）
- pfb 是什么：测量 prompt engineering 各臂对 LLM 事实调研质量影响的 benchmark
- 当前状态：<哪个实验跑完了、哪个在等、数字是多少>
- 为什么做这件事：<因果链，不是"因为要推进">

## 具体任务
1. <步骤 1，带预期产出>
2. <步骤 2>
3. ...

## 验收标准（机器可查）
- [ ] <文件路径> 存在且包含 <具体内容>
- [ ] <指标> ≥ <阈值>
- [ ] git log 有新 commit 且 message 含 "T<N>"

## 约束
- 不要修改 <这些文件>（它们是其他实验的数据）
- 新文件放 <目录>
- 格式参照 <已有示例文件路径>

## 降级方案
- 如果 X 不可用 → 用 Y 替代，标注 conf 降为 0.2
- 如果超时 → 落盘已完成部分，commit message 标 "T<N>-partial"
```

**为什么"背景"段最重要**：arena agent 没有我们的对话历史。它不知道 S10 刚跑完、D-face 确认了模型上限、B1 任务卡写了 gold 还没建。不给背景，它会重复做已完成的事或者在错误假设上工作。

## 回执验收

Arena 完成后：
1. `git fetch origin 'refs/heads/arena/<branch>'`
2. `git log origin/arena/<branch> --oneline -5` — 确认有新 commit
3. `git show origin/arena/<branch>:<file>` — 看实际文件内容（不是 commit message）
4. 独立复算数字（如覆盖率、κ）
5. 对照任务书的验收标准逐条过

**常见翻车**：
- Arena 说"完成"但 commit 在错误的 branch 上
- 文件创建了但内容是空模板
- 数字对不上（arena 用了不同的 gold 版本）

## T 编号台账

所有 pfb 相关 arena 任务按 T 编号记录在 `sop/arena-loop-pipeline.md` 的台账表里：

| T | 任务 | 状态 | Branch | Commit |
|---|------|------|--------|--------|
| T29 | R1-R7 独立性检查 | ✅ | arena/... | abc1234 |
| T30 | [待核验] | 🔄 | arena/071ab5cb-... | b08491b (stalled?) |
| T49 | Gold trees merge | ✅ | arena/... | b08491b |

**Stalled 处理**：超过 24h 无新 commit → 标记 stalled，不阻塞其他工作。下次派新任务时顺带问一句。

## 什么该派 arena / 什么自己做

| 工作 | 通道 | 原因 |
|------|------|------|
| Gold tree 构建（调研+整理） | arena | 纯调研+写作，不需要本地工具 |
| 异族 judge battle 投票 | ego-browser 半手动 | 需要登录态+投票交互 |
| 跑 run（本地 vLLM） | 本地 | 需要 GPU + 本地文件 |
| 评分（score.py） | 本地 | 读本地 JSON |
| 竞品调研 / 文献综述 | arena | 多源搜索+综合 |
| Prompt 设计/修改 | 本地（我） | 需要理解实验全貌 |
| Pipeline bug fix | 本地 | 需要 debug 环境 |

**判断原则**：需要本地 GPU/文件/debug 环境的 → 自己；纯信息搜集+综合+写作的 → arena。