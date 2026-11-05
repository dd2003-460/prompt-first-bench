# 03 — 行动分解：RV3G6-o3-claim-list-erratum-27

| # | 动作 | 产出 | 依赖 |
|---|------|------|------|
| A1 | 落盘备料主文档 `bench/rubric-v3/o3-claim-list-erratum-27-materials.md`（六节：溯源/关键发现/三方案对照/推荐/裁定后执行清单/边界声明）——内容 = 02 F1-F5 重组 + X1/X2 修正并入 | materials 文件 | 02+02.5 ✓ |
| A2 | 裁定后执行清单预写三种改法的完整 diff（o3-claim-list.md L137 + assert-hitmatrix-evidence.py L26/L151/L154 三处同步 + revision-log-batch1.md 条目模板 + APPROVALS 登记模板）——**只预写不执行** | materials §5 | A1 |
| A3 | 冻结面零修改验证（git status --porcelain 仅本 goal 新增文件） | 04 日志记录 | A1 |
| A4 | queue 更新：L24 条目 `[ ]` → `[~]`（材料已备，待成璐裁定——同 jaccard-adjudicate L45 惯例，不划掉） | goal-queue.md diff | A1 |
| A5 | 04.5 反方复核（≥6 攻击）→ verdict | 04.5 工件 | A1-A4 |

**不做的**（范围外，显式登记）：不改 o3-claim-list.md（冻结件，等裁定）；不改 assert 脚本（同上）；不动 r142 历史工件（审计链）。