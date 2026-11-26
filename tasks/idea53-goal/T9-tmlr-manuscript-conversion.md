# origin: ai
# 任务卡：idea53 TMLR 格式稿生成（11-25 三步第一步）

## 目标
把 `paper-en.md`（markdown 底本）转成 TMLR 格式 LaTeX 并编译出 PDF。纯本地工作，不联网，不改被锁文件。

## 输入（全部已就位，只用这些）
- 底本：`/Users/a1-6/Desktop/workspace/pfb/tasks/idea53-goal/manuscript-scoped/paper-en.md`（116 行，10 节）
- TMLR 模板：`/Users/a1-6/Desktop/workspace/pfb/tasks/idea53-goal/manuscript-scoped/tmlr-style/tmlr-style-file-main/`（tmlr.sty / tmlr.bst / fancyhdr.sty / main.tex 样例 / main.bib）
- 图：`/Users/a1-6/Desktop/workspace/pfb/tasks/idea53-goal/manuscript-scoped/fig1-scoring-protocol.tex`（TikZ 结构图）
- 引用：`/Users/a1-6/Desktop/workspace/pfb/tasks/idea53-goal/submission-staging/references.bib`（15 条已核验）
- LaTeX 环境：`/opt/homebrew/bin/pdflatex`、`/opt/homebrew/bin/xelatex`（本机已有）

## 产出
- `manuscript-scoped/paper-tmlr.tex`（主文件，\usepackage tmlr.sty，bibliography 指向 references.bib）
- `manuscript-scoped/paper-tmlr.pdf`（编译成功，页数合理 8-15 页）
- commit（pfb 仓库）

## 硬性要求
1. **双盲匿名**：不出现作者名/机构/致谢/funding（TMLR double blind）。author 字段留空或用 "Anonymous"。
2. **15 条 bib 全接入**：references.bib 的 15 条 key 全部出现在 bibliography；正文中应有 \cite（底本 md 里如果有引用占位符就接上，没有就在相关工作段按 key 自然引用——不许编造不存在的引用关系，底本 md 没提到的工作不要在正文里硬引）。
3. **fig1 插入**：TikZ 代码 \input 或 \includegraphics 方式嵌入，图注保留。
4. **内容忠实**：paper-en.md 的 10 节结构、scope statement、abstract、数字（43-56% / 0.17-0.23 / 0.71-0.77 bits / 40000 workloads / 24 permutations / 4 platforms）一字不改地搬过去。不新增内容、不删内容、不改数字。
5. **不碰被锁文件**：`submission/paper.tex` 等 SHA256SUMS 锁定的 7 个文件一律不读不写。
6. 编译命令序列：pdflatex → bibtex → pdflatex ×2，直到无 undefined reference。

## 验收标准（Lead 对照检查）
- [ ] paper-tmlr.pdf 存在且可打开（pdfinfo 页数 ≥8）
- [ ] `grep -c "\\\\cite" paper-tmlr.tex` ≥ 5
- [ ] 15 个 bib key 在 tex 的 \bibliography 引用的文件中（直接 grep references.bib）
- [ ] PDF 首页无作者名（grep pdf 文本）
- [ ] commit 存在（git log 可查）
- [ ] 数字抽检：PDF 文本含 "43" "56%" "0.71" "0.77" "40,000"（至少 4/5）

## 边界
- 不联网。不改 references.bib（15 条已核验）。不改 paper-en.md。
- 若 fig1 TikZ 编译报错（缺宏包），允许在 tex 顶部加 \usepackage（tikz 常用包），不改 TikZ 几何。
- 编译 3 次仍不过 → 停下，把完整报错写进 `manuscript-scoped/compile-error-<日期>.log`，不要硬凑。
