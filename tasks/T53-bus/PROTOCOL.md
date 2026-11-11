# T53 文件总线协议 (Decision 21)

两个方向，都是追加式（不覆盖），每条带时间戳 + 递增序号：

## lead→teamer.md
Lead 写。用途：方向修正、新指令、上下文补充、对 teamer 问题的回答。
格式：`## L<n> <HH:MM> — <一句话标题>` + 正文。

## teamer→lead.md
Teamer 写。用途：进展汇报（每工作单元）、方向质疑、需要 Lead 判断的决策点、发现的坑。
格式：`## T<n> <HH:MM> — <一句话标题>` + 正文。

## 轮询约定
- Teamer：每完成一个工作单元（一次跑批/一组分析/一段代码）读一遍 `lead→teamer.md` 尾部，有新条目先响应再继续原任务。
- Lead：收到 child 结果或主动检查时读 `teamer→lead.md` 尾部；需要即时纠正时用 delegate_task steer 投递同一内容（steer = 实时通道，bus = 持久记录）。
