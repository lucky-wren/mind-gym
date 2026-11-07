# 趣学益智馆 v1 · 静态托管交付包

> 一个 `index.html` 就是整个网站。**不需要构建、不需要后端、不需要数据库、不需要环境变量**，把本目录原样上传到任意静态托管即可访问。
>
> 版本号说明：本次按正式发布节奏重新编号为 **v1**，功能包含此前全部迭代（七个关卡、成语接龙不断链、错题本、徽章、可选免费 AI 等）。页面顶栏与页脚会显示橙色 `v1`。

---

## 一、包里有什么

| 文件 | 必需 | 作用 |
|---|---|---|
| `index.html` | ✅ **唯一必需** | 网站本体。HTML + 内联 CSS/JS，793 条成语、3755 字读音表、七个关卡题库全部内置。单独拿出来双击也能玩 |
| `README.md` | 建议 | 本文件，部署说明 |
| `趣学益智馆使用说明.md` | 建议 | 给最终玩家看的大白话说明书（Markdown 版，记事本 / VS Code / 浏览器都能打开；玩法、AI 要不要开、名词解释、常见问题） |
| `bridge.py` | 可选 | 本机 AI 转发小脚本，仅 Python 标准库、无需 pip。与网页设置页里的「桥代码」逐字一致 |
| `.nojekyll` | 可选 | 空文件，给 GitHub Pages 用，避免 Jekyll 处理目录 |

包内所有文件都是 UTF-8 编码，**不要改动文件名编码**。`index.html` 如需备份留档，复制一份改名即可，不要替换成旧版文件。

---

## 二、通用三步（所有平台都一样）

1. 解压本压缩包，得到 `趣学益智馆_v1_静态托管包/` 目录。
2. 把**整个目录**上传到静态托管，入口设为根目录的 `index.html`。
3. 打开平台给你的网址，拉到页脚看到橙色 **v1** 即部署成功。

关键设置只有三条：**构建命令留空**、**输出目录 / 发布目录 = 根目录**、**索引文档 = index.html**。别的都不用填。

---

## 三、各平台具体步骤（照着点就行）

> **动手前先做两件小事**
> 1. 解压 `趣学益智馆_v1_静态托管包.zip`，确认根目录里能看到 `index.html`、`README.md`、`.nojekyll`。**不要把外层文件夹再套一层**上传：要传的是「文件夹里面的文件」，不是「装着文件夹的文件夹」。
> 2. 先跑一次 [3.8 本机预览](#38-本机先预览推荐部署前做一次)，确认 `http://` 环境下页面正常。这一步能提前排掉 90% 的「上传后白屏」。
>
> **三条通用设置，任何平台都一样**：构建命令留空、发布目录 = 根目录、索引文档 = `index.html`。

### 3.0 先选平台：一张表看懂

| 平台 | 适合谁 | 要不要账号 | 大概耗时 | 国内访问 | 自定义域名 |
|---|---|---|---|---|---|
| **本机预览** | 只是自己先看看 | 不要 | 1 分钟 | 最快 | 不需要 |
| **Netlify 拖拽** | 想最快给别人一个网址 | 要（可邮箱注册） | 2 分钟 | 一般 | 免费支持 |
| **GitHub Pages** | 已有 GitHub、想长期放着 | 要 | 5 分钟 | 一般 | 免费支持 |
| **Vercel** | 已有 Git 仓库、想要自动部署 | 要 | 5 分钟 | 一般 | 免费支持 |
| **Cloudflare Pages** | 想要 CDN 快、已用 CF | 要 | 5 分钟 | 一般 | 免费支持 |
| **腾讯云 COS** | 国内访问优先 / 已有云账号 | 要 + 实名 | 10 分钟 | **快** | 免费支持（需备案） |
| **Gitee Pages** | 国内、不想绑信用卡 | 要 + 实名 | 10 分钟 | **快** | 需实名审核 |
| **Nginx / VPS** | 自己有服务器、要完全掌控 | 服务器 | 15 分钟 | 看你服务器 | 自己配 |

**只想最快看到效果** → Netlify 拖拽。**想国内打开快** → 腾讯云 COS 或 Gitee Pages。**已经有 GitHub** → GitHub Pages。

---

### 3.1 GitHub Pages

**适用场景**：长期放着一个公开小站，改文件推上去就自动更新。免费，仓库需公开（私有仓库要用付费版才能开 Pages）。

#### A. 用网页上传（不用装 Git）

1. 登录 GitHub → 右上角 `+` → **New repository**。
2. 填仓库名（如 `quiz`），**Public**，勾选 **Add a README** 可勾可不勾，点 **Create repository**。
3. 进入仓库页 → 点 **Add file** → **Upload files**。
4. 把解压目录里的**全部文件**（含 `.nojekyll`，它是隐藏文件，Windows 需要在资源管理器勾「显示隐藏的项目」）一起拖进上传区。
5. 下方 Commit message 随便填（如 `init`），点 **Commit changes**。
6. 仓库 → **Settings** → 左侧 **Pages**。
7. **Build and deployment** → **Source** 选 `Deploy from a branch`；**Branch** 选 `main`、右边目录选 `/ (root)` → 点 **Save**。
8. 等 30 秒～2 分钟，刷新 Pages 页面，顶部会出现 `Your site is live at https://用户名.github.io/仓库名/`。
9. 点开网址，拉到页脚看橙色 **v1**。

#### B. 用命令行（已有 Git 习惯）

```bash
cd 趣学益智馆_v1_静态托管包
git init
git add -A                 # -A 会把 .nojekyll 一起加进去
git commit -m "init quiz"
git branch -M main
git remote add origin https://github.com/用户名/仓库名.git
git push -u origin main
```
然后照样走上面第 6～8 步开 Pages。

**子路径部署**：访问地址是 `https://用户名.github.io/仓库名/`，页面没有任何绝对路径引用，**不用改代码、不用加 `<base>`**。若用自定义域名映射到根路径，也照常能跑。

**常见坑**

- **404**：Pages 还没开、分支选错（有的默认 `main`、有的 `master`）、或目录选成了 `/docs`。回到 Settings → Pages 核对。
- **页面样式全丢 / 一片白**：多半是把外层文件夹也传上去了，实际入口变成 `/仓库名/趣学益智馆_v1_静态托管包/index.html`。根目录必须直接能看到 `index.html`。
- **改了文件但线上没变**：GitHub Pages 有构建延迟，等 1 分钟；再不行给网址加 `?v=2` 绕开浏览器缓存，或在 Settings → Pages 里关掉再开一次。
- **`.nojekyll` 没传**：GitHub Pages 默认用 Jekyll 处理，会忽略下划线开头的文件；本包没有这类文件，但建议还是传上，避免平台做多余处理。

---

### 3.2 Netlify（最快）

#### A. 拖拽部署（推荐，连 Git 都不用）

1. 打开 [app.netlify.com](https://app.netlify.com) 注册登录（邮箱或 GitHub 都行）。
2. 进入 **Sites** → 右侧 **Add new site** → 选 **Deploy manually**。
3. 页面中间出现一个虚线拖拽区，把**解压后的整个目录**拖进去（拖目录本身即可，Netlify 会以目录内文件为站点根）。
4. 稍等几秒，状态变 **Published**，平台会给一个 `https://随机名字.netlify.app` 的网址。
5. 打开网址 → 页脚看 **v1**。
6. 想换名字：**Site configuration → Site details → Change site name**，改成好记的即可。

> 拖拽部署不经过 Git，**以后改文件要重新拖一次**。想「推代码就自动更新」用下面 B。

#### B. 连 Git 仓库（自动部署）

1. **Add new site** → **Import an existing project** → 选 GitHub / GitLab / Bitbucket 并授权。
2. 选中你的仓库。
3. **Build settings** 里这样填：
   - **Branch to deploy**：`main`
   - **Build command**：**留空**（不要填 `npm run build`，本包没有构建步骤）
   - **Publish directory**：填 `.` （一个点，代表根目录）
4. 点 **Deploy site**。之后每次 `git push` 都会自动重新发布。
5. **Site configuration → Build & deploy → Post processing** 里可以关掉「Bundle / minify」之类优化（可选，页面本来就单文件）。

**常见坑**

- **Publish directory 填错**：填成 `dist`、`build`、`public` 都会导致 404。本包没有输出目录，就是 `.` 或留空。
- **Build command 被自动填了**：有些模板会自动带 `npm run build`，务必清空，否则报「No package.json」。
- **拖拽时拖错层级**：拖的是外层空壳目录，导致入口多一层。上传后到 **Deploys → 点本次部署 → 看文件列表**，根目录应直接有 `index.html`。
- **自定义域名**：**Domain management → Add custom domain**，按提示加 CNAME；Netlify 会免费签 Let's Encrypt 证书。

---

### 3.3 Vercel

1. 打开 [vercel.com](https://vercel.com) 用 GitHub / GitLab / 邮箱登录。
2. 控制台点 **Add New… → Project**，或 **Import Git Repository** 选中仓库 → **Import**。
3. **Configure Project** 页面：
   - **Framework Preset**：选 **Other**（千万别让 Vercel 自己猜成 Next.js / Vite）。
   - **Root Directory**：留默认 `./`。
   - **Build Command**：**清空 / 留空**。Vercel 有时会预填，点右边齿轮 → Override → 清空。
   - **Output Directory**：**留空**或填 `.`。
   - **Install Command**：留空。
4. 点 **Deploy**，等 20～60 秒，出现 `https://项目名.vercel.app`。
5. 打开 → 页脚 **v1**。
6. 自定义域名：**Project → Settings → Domains** → Add → 按提示加解析，证书自动签。

**常见坑**

- **选错 Framework**：Vercel 会试图跑 `npm install` / `next build`，报「No package.json」或「No framework detected」。回到 Settings → Build & Development Settings，把 Framework 改 **Other**、三个命令全清空后 Redeploy。
- **Output Directory 填了 `public`**：会 404。本包就在根目录。
- **不需要 `vercel.json`**：单页无路由、无服务端函数，加了反而可能引入重写规则。
- 免费 Hobby 计划对个人站够用；**不要**把它配置成需要服务端渲染的项目。

---

### 3.4 Cloudflare Pages

1. 登录 [dash.cloudflare.com](https://dash.cloudflare.com) → 左侧 **Workers & Pages** → **Create application** → **Pages** → **Connect to Git**（或 **Upload assets** 直接拖目录）。
2. 授权并选中仓库 → **Begin setup**。
3. **Set up builds and deployments**：
   - **Production branch**：`main`
   - **Framework preset**：**None**
   - **Build command**：**留空**
   - **Build output directory**：留空或填 `/`
   - **Root directory**：留空
4. 点 **Save and Deploy**，得到 `https://项目名.pages.dev`。
5. 打开 → 页脚 **v1**。
6. 自定义域名：**Custom domains** → Set up a custom domain（域名在 CF 托管时最省事，自动加解析和证书）。

**常见坑**：CF 有时会自动补一个 `npm run build`，务必在 Build command 里清空；**Direct Upload**（拖目录）时同样选 None preset。Cloudflare Pages 与 **Quick Tunnel 是两回事**——前者是静态托管，后者只是把本机端口临时映射成公网地址，见第六节。

---

### 3.5 腾讯云 COS / 国内对象存储静态网站

**适用场景**：国内打开要快、已有腾讯云账号。需要实名认证；绑定自定义域名在大陆需备案。

1. 登录 [腾讯云控制台](https://console.cloud.tencent.com/cos) → **对象存储 COS → 存储桶列表 → 创建存储桶**。
2. 填写：名称（如 `quiz-你的标识`）、**地域**选离访客近的（如 `ap-shanghai`）、**访问权限**选 **公有读私有写**（最省事；选私有读则后面每个文件都要单独授权，容易 403）。其余默认 → 创建。
3. 进入桶 → **文件列表** → **上传文件**，把解压目录里的**全部文件**上传到**桶根目录**（不要新建子文件夹再传进去；`.nojekyll` 在 COS 上用不到，传不传都行）。
4. 左侧 **基础配置 → 静态网站** → 点 **编辑**，开启「静态网站」：
   - **索引文档**：`index.html`
   - **错误文档**：也填 `index.html`（可选，单页无路由，填了更保险）
   - 其余（重定向规则、错误码）不用动 → 保存。
5. 回到静态网站页，复制平台给的**静态网站访问域名**（形如 `quiz-xxx.cos-website.ap-shanghai.myqcloud.com`），浏览器打开 → 页脚 **v1**。
6. **（可选）自定义域名 + CDN**：**域名与传输管理 → 自定义 CDN 加速域名** 或 **自定义源站域名**，按提示加 CNAME，并在 **SSL 证书管理** 申请/上传免费证书，开启 HTTPS。大陆域名需先完成 ICP 备案。
7. **（可选）刷新缓存**：改完 `index.html` 后，到 **CDN → 刷新预热** 提交 URL 刷新，否则可能还是旧页面。

**常见坑**

- **403 AccessDenied**：桶是「私有读」。改成公有读私有写，或给 `index.html` 单独设公有读。
- **404 / 直接下载文件而不是打开网页**：没开「静态网站」，或索引文档没填 `index.html`。注意 COS 有「默认域名」和「静态网站域名」两个地址，**要用静态网站那个**。
- **上传到了子目录**：根目录必须直接是 `index.html`，否则索引文档找不到。
- **用 COS 默认域名访问会强制下载**：这是 COS 的行为，务必走静态网站域名或自定义域名。
- **阿里云 OSS / 华为云 OBS** 流程几乎一样：建桶 → 公有读 → 传根目录 → 静态页面/静态网站托管 → 索引文档 `index.html` → 用平台给的静态网站域名访问。

---

### 3.6 Gitee Pages（国内备选）

1. 登录 [gitee.com](https://gitee.com)，完成**实名认证**（Gitee Pages 要求实名）。
2. 新建**公开**仓库，把目录内文件推上去（方式同 3.1 的 B，把 remote 换成 Gitee 地址）。
3. 仓库页 → 顶部 **服务** → **Gitee Pages**。
4. 部署分支选 `master` / `main`，**部署目录留空**（根目录）→ 点 **启动/更新**。
5. 得到 `https://用户名.gitee.io/仓库名`，打开验证页脚 **v1**。

**常见坑**：Gitee Pages **不会自动更新**，每次推完代码都要回到 Pages 页手动点「更新」；仓库必须公开；首次需实名审核；自定义域名需另外申请。

---

### 3.7 Nginx / 任意 VPS（自己有服务器）

#### A. 放文件

```bash
sudo mkdir -p /var/www/quiz
sudo cp -r 趣学益智馆_v1_静态托管包/* /var/www/quiz/
sudo chown -R www-data:www-data /var/www/quiz   # Debian/Ubuntu；CentOS 用 nginx:nginx
sudo chmod -R 755 /var/www/quiz
sudo ls /var/www/quiz                           # 应直接看到 index.html
```

#### B. 配置站点

新建 `/etc/nginx/sites-available/quiz`（CentOS 放 `/etc/nginx/conf.d/quiz.conf`）：

```nginx
server {
    listen 80;
    server_name your.domain.com;      # 没域名就写 _ 或服务器 IP

    root /var/www/quiz;
    index index.html;

    # 单页无路由；这行只是保险，删掉也能跑
    location / {
        try_files $uri $uri/ /index.html;
    }

    # index.html 不缓存，避免升级后用户拿到旧版
    location = /index.html {
        add_header Cache-Control "no-cache, no-store, must-revalidate";
    }

    # 说明书 / README 纯文本，顺手声明 UTF-8
    location ~* \.(md|txt)$ {
        default_type text/plain;
        charset utf-8;
    }
}
```

#### C. 启用并重载

```bash
sudo ln -s /etc/nginx/sites-available/quiz /etc/nginx/sites-enabled/   # 仅 Debian/Ubuntu 需要
sudo nginx -t                # 必须显示 syntax is ok / test is successful
sudo nginx -s reload         # 或 sudo systemctl reload nginx
```

浏览器打开 `http://服务器IP/` 或你的域名，验证页脚 **v1**。

#### D. 上 HTTPS（推荐）

```bash
sudo apt install certbot python3-certbot-nginx -y   # Debian/Ubuntu
sudo certbot --nginx -d your.domain.com
```
certbot 会自动改配置并配好自动续期。**建议一定上 HTTPS**：一是浏览器对 `http://` 页面会标「不安全」，二是若以后要开 AI，https 页面不能去连 `http://localhost` 的本地桥（见第六节）。

**常见坑**

- **`nginx -t` 不过**：多半是 `location ~*` 里的反斜杠被 shell 吞了，用上面的配置文件原样写入、别在命令行里手敲。
- **403 Forbidden**：目录权限或 SELinux。先 `chmod -R 755`，CentOS 再试 `sudo setenforce 0` 验证是不是 SELinux。
- **改了文件没生效**：Nginx 不缓存，但浏览器会。Ctrl+F5 或加 `?v=2`。
- **防火墙**：云服务器安全组要放行 80 / 443。

---

### 3.8 本机先预览（推荐部署前做一次）

```bash
cd 趣学益智馆_v1_静态托管包
python3 -m http.server 8080
```

浏览器打开 `http://localhost:8080/`，按 Ctrl+F5 强刷，确认页脚 **v1**、七张卡片、随便答一题有反馈。

没有 Python 也能用：

```bash
npx serve .            # 需要 Node.js
```

或用 VS Code 装 **Live Server** 插件，右键 `index.html` → **Open with Live Server**。

**为什么值得做**：`file://` 双击和 `http(s)://` 是两种环境。http 下能提前验证 localStorage 写入、相对路径、内联脚本是否被 CSP 拦住、页面是否真的零外部请求——这些都和真实托管一致。Ctrl+C 可停掉服务。

> 部署完成后，按 [第五节「部署后验证清单」](#五部署后验证清单) 逐项打勾。若页脚不是 v1，按 [第七节「缓存与版本」](#七缓存与版本) 处理。

---

## 四、为什么它能直接丢上去（技术事实）

- **零外部依赖**：没有 CDN、没有字体、没有图片、没有音频文件；CSS 与 JS 全部内联。连 favicon 都是内联 SVG，托管时不会额外请求 `/favicon.ico` 产生 404。
- **无构建、无路由**：单页、单文件，不依赖服务端重写规则（Nginx 的 `try_files` 只是保险，不是必须）。
- **全相对路径**：放在域名根目录或任意子目录都能正常工作。
- **默认零联网**：不开启 AI 时，页面一个外部网络请求都不发；开启后也只在你主动点「让 AI 帮我想一个」时才请求一次。
- **状态存本机**：积分、错题、设置、AI 配置都写在浏览器 `localStorage`，不需要后端接口。

> ⚠️ 若托管平台设置了严格的 **Content-Security-Policy**，请确认允许内联脚本与内联样式（`'unsafe-inline'`），否则页面脚本会被拦住。绝大多数静态托管默认不设 CSP，无需处理。

---

## 五、部署后验证清单

打开网址，逐项确认：

- [ ] 页脚显示橙色 **v1**（不是旧版本号）
- [ ] AI 设置页「⭐ 推荐模型」有 5 个按钮，默认模型名为 `Qwen/Qwen3.8-27B`
- [ ] 首页有 **7 张**关卡卡片，点「开始挑战」能进入答题
- [ ] 随便答一题，绿色/红色反馈出现在题卡内部，能点「继续」到下一题
- [ ] 成语接龙里输入「穷则思变」接「…力大无穷」能判对，且成语链不会从头开始
- [ ] 顶栏 🌙 深色模式、🔊 音效开关可用
- [ ] 「我的战绩」有 7 行排行榜，「影视台词小抄」有 28 句
- [ ] 浏览器开发者工具 Network 面板：**默认状态下无外部请求**

---

## 六、AI 与 HTTPS（部署后唯一需要留意的地方）

### 6.0 零基础：本地桥到底怎么用（不想看代码版）

**先判断要不要用**：不开 AI → 不需要；开了 AI 且「测试连接 ✅ 通了」→ 也不需要。**只有**「跨域被拦」或「https 网站想用本机桥」才需要它。

**它是什么**：一个住在你自己电脑里的「传话员」。浏览器只跟本机的传话员说话（浏览器允许），传话员再替你去问魔搭（服务器之间不受跨域限制），把答案带回来。好处是令牌只交给传话员，不进浏览器。

**那一大段 Python 代码一个字都不用看懂，也不用改**，只要下载下来跑起来：

| 步骤 | 做什么 |
|---|---|
| 1 | 网页设置页点「⬇️ 下载 bridge.py」，或直接用包内自带的 `bridge.py`。不用打开、不用编辑 |
| 2 | 电脑装了 Python（Windows 可在微软商店搜「Python」安装，Mac 一般自带）。打开命令行，进入文件所在目录，运行：`MODELSCOPE_TOKEN=ms-你的令牌 python3 bridge.py`（Windows PowerShell 用 `$env:MODELSCOPE_TOKEN="ms-你的令牌"; python bridge.py`） |
| 3 | 看到 `bridge -> http://localhost:8787/v1/chat/completions` 即成功，**命令行窗口别关**。回到设置页选「本地桥」通道 → 勾开启 → 保存 → 测试连接 → ✅ 通了 |

小提醒：窗口关掉 / 电脑重启后要重跑第 2 步；https 部署时还要再跑一条 `cloudflared tunnel --url http://localhost:8787`，把打印出的 https 地址加上 `/v1/chat/completions` 填进「接口地址」。不想碰命令行就改用 Puter.js 零配置通道或直接填魔搭令牌。

---

### 6.1 推荐模型（页面里可一键填入）

交付包 v1 的魔搭默认模型为 **`Qwen/Qwen3.8-27B`**。它出现在魔搭公开 `/v1/models` 清单与官方 curl 示例里，也有第三方实测可用，是当前证据最硬的一个。上一版曾推荐 `Qwen/Qwen3.5-27B`，但它只见于第三方清单、缺少官方示例佐证，已降级为备选（若报 400/404「模型不存在」就换掉）。AI 设置页「模型名」下方新增 **⭐ 推荐模型** 一排按钮，点一下自动填入完整 id 并切回魔搭通道，模型下架时换一个点即可，不用手抄。

| 模型 id（必须带组织前缀） | 定位 | 依据 / 为什么适合 |
|---|---|---|
| **`Qwen/Qwen3.8-27B`** ⭐ | 默认 | 公开 `/v1/models` 清单 + 官方 curl 示例里都出现，第三方实测也可用 |
| `Qwen/Qwen3.5-35B-A3B` | 官方示例 | 魔搭《API推理介绍》示例代码用的 id；MoE 35B 总参只激活约 3B，中文强 |
| `deepseek-ai/DeepSeek-V4-Flash-0731` | 备选 | 在公开 `/v1/models` 清单里，第三方实测「综合向底仓、能跑通」 |
| `Qwen/Qwen3.8-Flash-Next` | 极速档 | 上一版默认，第三方实测可用 |
| `Qwen/Qwen3.5-27B` | 上一轮推荐 · 备选 | 仅见于第三方清单；若报 400/404，换上面几个或点「查当前可用模型」 |

**为什么挑这几个**：页面拿到回答后是「抓前 4 个汉字」当成语用的。模型若回「好的，给你一个成语：穷则思变」，抓到的是「好的我给」→ 判失败回退本地；带思考过程的模型更糟，思考块里的汉字会被先抓走。所以要选**听话的 instruct / Flash 类**，旗舰 `Qwen3.5-397B-A17B` 能用但 2 魔粒/次、慢、爱啰嗦，属于杀鸡用牛刀。

**别踩坑**：2026-09 有第三方对 37 个 API-Inference 模型逐个实测，只有 15 个真返回内容，22 个是 HTTP 200 但 `choices` 为空的「挂牌模型」，**而空响应照样扣魔粒**。返回空的有 `DeepSeek-V4-Pro`（含 `-0813`）、`GLM-5.2`、`Step-3.7-Flash`、`MiniMax-M3` 等。官方也说明支持清单会随新模型发布持续迭代、早期模型逐渐下架。所以**别挨个试**，换完模型点一次「🧪 测试连接」即可（这也是「先测再接」的探针）。

**额度口径**：现在按魔粒算，每天登录 200 + 绑定阿里云 50 = 250 魔粒/天、当日有效不结转；轻量 0.5 / 主流 1 / 旗舰 2 魔粒一次，约合 500 / 250 / 125 次。网传「2000 次/天」是旧规则。官方明确这是体验性质服务，不保证并发与 SLA。

> 资料核对：2026-11-07，综合魔搭官方文档、2026-09 第三方逐个实测与 2026-10 社区清单。免费池动态轮换，最终以「测试连接」结果为准。

---

### 6.2 「测试连接」没通？先确认地址，再按状态码定位

**先回答最常见的疑问：接口地址填得对吗？—— 对的。**

魔搭官方文档写的 `https://api-inference.modelscope.cn/v1` 是给 **SDK** 用的：SDK 会自动在后面拼 `/chat/completions`。
本页不用 SDK、直接 `fetch`，所以必须填**完整路径** `https://api-inference.modelscope.cn/v1/chat/completions`
（页面自动填的就是这个）。**不要**改成不带 `/v1` 的 Anthropic 端点，也别用网上流传的 `/compatible-mode/v1/`（实测 404）。
若用 Dify / 客户端类工具，那里反而只填 `.../v1`，两者别混。

**三步把「地址 / 网络」「Token / 账号」「模型名」彻底分开：**

1. 看 **API Key 输入框旁边的格式自检**：不是 `ms-` 开头或长度偏短会直接红字提示（只检查格式，不显示内容）。
2. 点 **「🔎 查当前可用模型」**：它请求公开的 `/v1/models`，**不需要 Token**。能拉到清单 → 地址和浏览器跨域都是通的，问题只在 Token/账号/模型名；拉不到 → 是网络或跨域被拦，走本地桥。清单里点任意一行即可填入模型名。
3. 点 **「🧪 测试连接」**：现在会直接显示 **HTTP 状态码 + 服务端原文 + 一句该做什么**，不再是一句笼统的「没通」。

| 看到 | 意思 | 怎么办 |
|---|---|---|
| `401` + `bind your Alibaba Cloud account` | 没绑定阿里云 / 未实名 | 去 modelscope.cn 账号设置绑定并实名，等 1~3 分钟，必要时重新生成 Token |
| `401` 其它 / `Invalid token` | Token 复制不全、过期或权限没勾 | 回 `modelscope.cn/my/myaccesstoken` 重复制完整 `ms-` 串 |
| **`403` + `email verification` / `Magicubes`** | **邮箱没验证（最常见）** | 魔搭官方规定「邮箱验证通过」才开放魔粒 / API-Inference → 去 `modelscope.cn/my/settings/account` 点「验证邮箱」，到邮箱（含垃圾箱）点链接，回来确认已验证；顺手把「身份」下拉也选一下并保存。一般不用换 Token |
| `403` + `real name verified` | 阿里云账号未完成实名认证 | 完成实名后等几分钟，用同一个 Token 重试 |
| `400` / `404` `ModelNotFound` | 模型 id 不在当前清单 | 点「查当前可用模型」从官方清单挑一个，或点「⭐ 推荐模型」换 |
| `429` | 限流或当天魔粒用完 | 等一会儿 / 明天再试，换轻量模型 |
| 网络错误 / 无状态码 | 浏览器跨域预检被拦、网络不通 | 先按第 2 步判定；不通就走本地桥（https 站点再加 Quick Tunnel） |
| `HTTP 200 但无内容` | 挂牌模型或思考型模型 | 换一个 id 再测 |
| `5xx` | 魔搭服务端临时故障 | 稍后重试，不是你的配置问题 |

**账号三道关，别混淆**：① 绑定阿里云账号　② 阿里云实名认证　③ **邮箱验证通过**。前两关过了也可能卡在第 ③ 关——
魔搭官方《Magicube Rewards Program》明确写着「使用魔粒的前置条件：完善个人信息并通过邮箱验证」，
而 API-Inference 是用魔粒结算的，所以邮箱没验证会直接 403 。
账号设置页里邮箱右边还显示「验证邮箱」几个字，就说明没验证完；**已实名 ≠ 已验证邮箱**，两者是独立的关卡。

> 页面还兼容了 `reasoning_content`（思考型模型把正文放在这里）、数组型 content 等返回形状；
> 若链路通了但模型没按指令回「OK」，会提示「链路是通的，只是这次没按指令回」，不会误报失败。

---

AI **默认关闭**，游戏功能完全不依赖它。开启后，托管在 `https://` 上的页面会受浏览器两条规则影响：

| 通道 | https 托管下 | 说明 |
|---|---|---|
| 不开 AI（默认） | ✅ 完全正常 | 零外部请求，最省心 |
| 魔搭 ModelScope（默认推荐） | ⚠️ 看跨域 | 端点本身是 https。若对方允许 CORS 即可直连；若浏览器跨域预检被拦，走下面的「桥 + Quick Tunnel」 |
| Puter.js（零配置） | ✅ 可用 | 脚本是 https，按需加载；费用记在使用者自己的 Puter 账户，可能需要登录 |
| 智谱 GLM / Gemini / Pollinations | ⚠️ 视网络 | 都是 https；Gemini 国内多半不可达，Pollinations 匿名限流约 30 秒一次 |
| `bridge.py` 的 `http://localhost:8787` | ❌ 会被拦 | **https 页面不能请求 http 地址**（混合内容 / Mixed Content） |
| `bridge.py` + Quick Tunnel | ✅ 可用 | 用 `cloudflared tunnel --url http://localhost:8787` 拿到 `https://xxx.trycloudflare.com`，把地址加上 `/v1/chat/completions` 填进设置页 |

**结论**：本机双击预览时可以直接填 `localhost:8787`；一旦部署到 https 网址，本地桥就必须配 Quick Tunnel 换成 https 地址。Quick Tunnel 只是把本机端口临时映射成公网 https 网址的「管子」，**本身不提供任何 AI 能力**，推理仍来自桥后面的魔搭或本机 Ollama。

详细的大白话解释见包内 `趣学益智馆使用说明.md` 第 6 节；平台部署的逐步操作见本文件第三节。

---

## 七、缓存与版本

- 页面已带禁用缓存的 meta（`Cache-Control: no-cache`、`Pragma: no-cache`）。
- 平台 CDN 仍可能缓存旧文件：发布后在控制台 **Purge / 刷新 CDN 缓存**，或给用户网址加一个查询参数如 `?v=1` 绕开。
- 升级时**只替换 `index.html` 一个文件**即可，其它文件不需要动。
- 若页脚不是 `v1`，说明浏览器或 CDN 拿到的还是旧文件。

---

## 八、数据与隐私

- 成绩、错题、徽章、深色模式、音效、AI 配置都只存在**访问者本机浏览器**的 `localStorage`，不同域名之间互相隔离（本机双击一份、托管网址另一份，不互通）。
- 页面不含任何密钥；若用户填写了 API Key，它只保存在该用户自己的浏览器里，不会上传。
- 使用 `bridge.py` 时，令牌放在本机环境变量，连浏览器都不进。
- 免费 AI 通道均为第三方公共服务，条款、模型名与限流随时可能调整，以其官网最新说明为准。资料核对时间：2026-11-07。

---

## 九、常见问题

**Q：上传后打开是空白 / 一片乱？**
A：多半是 `index.html` 没放在发布目录根部，或平台设了严格 CSP 拦住内联脚本。按第四节检查。

**Q：子目录部署（如 `/quiz/`）能用吗？**
A：能，页面无绝对路径，也不需要改 `<base>`。

**Q：需要配 404 页面吗？**
A：不需要。单页无路由；若平台要求填错误文档，指向 `index.html` 即可。

**Q：能不能只上传 `index.html` 一个文件？**
A：可以，其余都是说明与可选工具。但建议把 `README.md` 和使用说明一起留着，方便交接。

**Q：AI 没配通，网站会坏吗？**
A：不会。请求失败会静默回退本地，判对错始终由页面本地规则完成，七个关卡照常可玩。

---

## 十、目录结构

```
趣学益智馆_v1_静态托管包/
├── index.html                  ← 网站本体（唯一必需）
├── README.md                   ← 本文件
├── 趣学益智馆使用说明.md        ← 给玩家看的大白话说明书（Markdown 版）
├── bridge.py                   ← 可选：本机 AI 转发桥
└── .nojekyll                   ← 可选：GitHub Pages 空文件
```
