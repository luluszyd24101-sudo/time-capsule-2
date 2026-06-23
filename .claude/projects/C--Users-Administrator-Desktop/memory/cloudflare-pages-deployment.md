---
name: cloudflare-pages-deployment
description: Cloudflare Pages 部署的恋爱时间胶囊项目配置
metadata:
  type: project
  related: static-site-project
---

项目已部署在 **Cloudflare Pages**，连接 GitHub 仓库 `luluszyd24101-sudo/time-capsule-2`。

- **入口文件**: `time-capsule.html`（非 index.html，通过 `_redirects` 文件将 `/` 重写至此）
- **配置方式**: 在 Cloudflare Dashboard 网页端手动设置 Build command 为空、Output directory 为 `.`
- **GitHub 仓库同时保留 `vercel.json`**（供 Vercel 使用）和 **`_redirects`**（供 Cloudflare Pages 使用）
- **目标受众**: 女朋友在国内使用，需要国内可直连访问
- **更新方式**: 本地修改后 `git push`，Cloudflare Pages 自动部署

**Why:** 用户是开发者，想给女朋友做一个恋爱纪念页面，部署在 Vercel 上国内无法访问，所以迁移到 Cloudflare Pages。

**How to apply:** 如需添加功能或修改内容，修改后 `git add . && git commit -m "说明" && git push` 即可自动部署。
