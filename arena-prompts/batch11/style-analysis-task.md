# Arena 任务卡: Opus 5.5 对标逐元素解析 + 工具调研

你是视频风格分析任务。产出落盘到本仓库，不讨论、不渲染视频。全程中文。

## 执行步骤
1. `git clone https://github.com/dd2003-460/prompt-first-bench`（main 分支）。
2. 读 `docs/refs/opus55/opus55-inventory.md`（合集元数据+规格）和 `docs/refs/opus55/sheets/sheet_suosuo.jpg`、`sheet_ziyou.jpg`、`sheet_jidian.jpg`（3 集抽帧 contact sheet，每格 1 帧，顺序=时间顺序）；需要细节再读 `docs/refs/opus55/frames/<集>/<帧>.jpg` 单帧（1280×720）。
3. 写 `docs/style-analysis.md`（UTF-8，markdown），必须包含以下 7 节，全部基于你实际看到的帧，禁止编造：
   - `## 0 总览`：3 集一句话风格定位 + 与"像素终端+绿色等宽字+黑底"风格（对照 d1-video-recreation E01-E24）的核心差异。
   - `## 1 像素/绘制单元`：最小绘制单元尺寸（px）、角色/物体的构造方式（矩形块？圆形？矢量？）、线条与描边。
   - `## 2 配色`：主色/背景渐变/卡片色/气泡色的 hex 估计（写近似值+来源帧）、整体色温（暖/冷）、每集是否有差异。
   - `## 3 字体与文字`：中文/英文字体风格（无衬线？像素？手写？）、字号层级、字幕/气泡/代码三种文字形态、HUD 文字的等宽特征。
   - `## 4 角色（Clawd/叙）`：形象构成（几块矩形/什么颜色/眼睛）、姿态变化、与 d1 的 Clawd 40×17 的差异点。
   - `## 5 镜头/节奏/转场`：单机位还是多机位？帧率感（30fps 实感）、每集节奏（静/动占比）、转场方式（硬切/淡入淡出/黑场）、HUD 黑条（顶部"上下文 x%"进度条/底部"Context left..."）的出现规律。
   - `## 6 声音`：从帧内无法直接判断的部分明确标"unverified"；若 inventory 有线索（BGM 风格等）列出。
   - `## 7 复刻要点（给 E25-E28 渲染任务卡的输入）`：10 条以内可执行规格（px 级），按产投比排序——先做能立竿见影还原风格的 3 条。
4. 另写 `## 8 网络类似工具/skill 调研`（同文件内）：用你已有的 web 能力（或明确说明不可用）调研"代码逐帧生成动画短片"的成熟工具/项目/skill，至少 3 个候选，表格：名称 | 一句话定位 | 链接 | 与 d1 需求（1280×720 60fps 1800帧 像素风 自动渲染+音频 mux）的匹配度 | 产投比排序 | conf（0-1，标 unverified 的来源不得 >0.7）。若网络不可用，此节写"网络不可用"并列出 3 个基于知识的候选标 conf≤0.5。
5. 验证：`test -s docs/style-analysis.md && wc -l docs/style-analysis.md` ≥ 80 行。
6. `git checkout -b arena/style-analysis` → `git add docs/style-analysis.md` → `git commit -m "docs: Opus 5.5 逐元素风格解析 + 工具调研（batch-11 对标）"` → `git push origin arena/style-analysis` → 向 main 开 PR 并给出 PR 链接。

## 验收（Lead 侧机器检查）
- pfb 存在分支 arena/style-analysis，含 docs/style-analysis.md，第 0-8 节齐全，第 7 节 ≥10 条可执行规格。
- 第 1 节必须给出具体 px 数值（不是"小方块"这类模糊描述）。
- 任何无法从帧确认的结论必须标 unverified。

## 边界
- 只新建 docs/style-analysis.md，不改其他文件。
- 不渲染视频、不生成 mp4。
- 参考图在仓库内（docs/refs/opus55/），不要从外网下载 B 站内容。
