# 04 — 执行验证：RV3G6-o3-claim-list-erratum-27

## A1 — 材料落盘 ✓

`bench/rubric-v3/o3-claim-list-erratum-27-materials.md`（六节齐，9.6KB）：溯源 byte-exact / 关键发现（三口径表+双源验证+下游消费者）/ 三方案对照表 / 推荐 A + 折中出口 / 裁定后执行清单（A/B/C 三序列 + APPROVALS 模板 + revision-log 模板）/ 边界声明。

## A2 — 数字复算断言 ✓（机判，非目视）

| 检查 | 结果 |
|------|------|
| V1 L137 引用 byte-exact（materials §1 引文 == o3-claim-list.md L137 strip） | True |
| V2 三口径数字 **13**/**34**/**35** 均在材料中 | True ×3 |
| V3 diff 预览含旧片段「27 个」+ 新片段「13 个」 | True ×2 |
| V4 六节标题齐 | True ×6 |
| V5 assert 脚本 3 同步点（L26/L151/L154）均列入执行清单 | True ×3 |

## A3 — 冻结面零修改 ✓

`git status --porcelain` 无 modified 行（仅本 goal 新增 untracked 文件）。o3-claim-list.md / hit-matrix.json / gold-tree.md / runs-C0-* / assert-hitmatrix-evidence.py / revision-log-batch1.md / APPROVALS.md 全部零触碰。

## A4 — queue 更新 ✓

L24 `[ ]` → `[~]`（材料已备待成璐裁定，同 jaccard-adjudicate L45 惯例不划掉），结果注记指向 materials 文件路径。

## 回归基线（未触碰脚本，预期不变）

assert-hitmatrix-evidence.py 常态输出维持「V1 计数 = 13/98 vs 声明值 = 27（MISMATCH——…勘误候选已导出）」——这是信号源职责的预期行为，不因备料收口而改变（X4 已声明）。