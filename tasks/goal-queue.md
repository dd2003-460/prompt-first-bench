# origin: ai — Goal 队列（ralph loop 消费）

> 格式：`- [ ] <goal 短名> | <一句话目标> | <产投比依据>`。完成改 `[x]` + 日期。新导出的候选追加到底部。

## 待办

- [ ] R5.2-third-scorer | 第三打分器（不同模型家族）用 packet v2 盲打 r4 三 run，κ 从 2-rater 升到 Fleiss'κ | R5.2 已交付 packet v2（输入对称断言通过），本 goal 直接消费；需 arena 通道或第三个本地模型，产投比中但依赖外部
- [x] T8-matrix-run-r1 (2026-10-30, r101: M8=1.00 团队文件协作/网盘选型域) | 按 tasks/T8-matrix-run-r1.md 任务书执行矩阵 run | 任务书已 push，产投比中

## 已完成

- [x] R5.2-evidence-packet (2026-10-30, r102: baff4b3) — 模板 v2 + packet v2（run1 M2=24/run2 M2=25/run3 null~45；M5 轮数 1/1/2 全带 basis）+ 对称性断言 67/0 exit 0；X2 错配登记（原 packet "run3 任务书25行"张冠李戴）
- [x] R5.2-packet-audit (2026-10-30, r103) — 原 v1 packet 单行摘要 12+1 原子断言全字段审计：8 confirmed / 3 mismatch / 1 unverified；新登记 X4(run1"无降级"vs degraded[3])/X5(14m27s unverified)/X6(step2"49/25/25"双错配，分值结论不变仅理由文本错→APPROVALS 条目 3)/X7("M1-M6定义+"空承诺)；机判脚本 assert-packet-audit.py 16/0/2 exit 0；未改任何冻结分

## 新导出候选

- [ ] R5.2-sourcepath-hardening | assert-packet-symmetry.py 去掉 basename glob 兜底——source_path 强制完整相对路径，消除同名文件误判局限（W1） | 04.5 W1 登记，工作量极小
- [ ] R5.2audit-C12-mechanize | assert-packet-audit.py 把 C12 形式性检查（"M1-M6 定义+"声称 vs 正文缺失的字符串比对）纳入机判，verdict 归类仍留人工 | R5.2-audit 04.5 W1 导出，工作量极小
