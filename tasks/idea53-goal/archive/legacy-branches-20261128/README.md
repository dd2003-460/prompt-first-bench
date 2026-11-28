# idea53 旧分支归档（legacy-branches-20261128）

2026-11-28 从 6 个已落后的 idea53 旧分叉中提取的**独有内容**存档。
这些分支各自只有 1–2 个独有 commit，且落后 main 约 2028 个 commit；
main 已用最新 TMLR 稿（`manuscript-scoped/paper-tmlr.tex`）取代了早期的 submission 打包。
本目录保留的是 main 上**没有**的历史产物，便于日后追溯。

## 来源分支

| 子目录 | 来源分支 | 内容 |
|---|---|---|
| `preprint-submission-v4/` | `idea53-preprint-ts-v4` | 11/24 时间戳锁定的 preprint 打包（paper.tex/pdf + formalism-skeleton + recompute 脚本 + SHA256SUMS） |
| `additive-tree-20261125/` | `idea53-additive-tree` | additive-tree 扰动版整包：草稿 + 投稿决策 + recompute 脚本 + arena 评审 |
| `round6/` | `idea53-round6` | round6 终审任务书（collision + venue match） |
| `planning-docs/` | `idea53-preprint-ts` | 早期规划文档历史快照（GOAL/outline/paper/decomposition*/metacog-skeleton） |

## 提取方式

逐文件 `git show <branch>:<path>` 取出，仅取「分支上有、main 上没有」的 idea53 路径。
非 idea53 内容（T53-bus / XREF / 10-decomposition / gpu-gold-tree 等）不在此归档——
那些是分支从旧 main 带出的别的项目状态，main 已有现行版本。

## 备注

- 各 preprint 分支（ts/v2/v3/v4）的 submission 打包内容基本相同，此处只保留最完整的 v4（含 recompute 脚本）。
- 归档后这些旧分支可安全删除（commit 仍在 git 历史中，必要时可 `git checkout <sha>` 找回）。
