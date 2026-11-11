# T53 文件总线（CC 实验员 → Lead）

两个方向，都是追加式（不覆盖），每条带时间戳 + 递增序号：

## lead-to-teamer.md / teamer-to-lead.md（Teamer 线）
Lead ↔ Teamer。格式 `## L<n>/<T<n> <HH:MM> — 标题`。

## cc-to-lead.md（CC 实验员 → Lead）
CC 写。用途：困惑/方向质疑、工作单元完成汇报、**idea 记录**、需要 Lead 判断的决策点。
格式：`## C<n> <HH:MM> — <一句话标题>` + 正文。
Lead 扫描频率：cron 每 30 分钟；检测到 CC 进程消失或 transcript 停更 >1h 时立即重启并读 bus。

### Idea 记录规范（CC 与 Lead 共同遵守）
CC 与 Lead 在讨论/工作中产生的 idea，写入 `pfb/lit-survey/IDEA-INDEX.md`（追加），必须带：
- **来源标注**：`[CC-Lead 讨论]` / `[CC 自主]` / `[Lead 自主]` —— 标明是"我们俩"的产物，不是用户的原始意图
- **taste 三问**（过不了就别记，记了也是噪音）：
  1. **general?** 换一个问题域还成立吗？还是只对当前 gpu/nat/soc 特化？
  2. **structured?** 能用 ≤3 句话写成可执行的机制描述吗？写不成 = 只是感觉
  3. **Levin 方向?** 它是在往"用更短的程序生成更多正确行为"上凑（压缩律），还是在加复杂度？前者记，后者要能说明为什么值得
- 状态：`[候选]`（刚产生）→ `[已验证方向]`（有数据支撑）→ `[已落盘]`（进了 decomposition/代码）