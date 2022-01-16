# Vercel Serverless Function - Python

参考：

Vercel官方Python教程：
https://vercel.com/docs/runtimes#official-runtimes/python

https://sspai.com/post/63028

https://towardsdatascience.com/how-to-deploy-a-python-serverless-function-to-vercel-f43c8ca393a0


部署到 vercel 时：

- Framework Preset 选 other
- Build and Output Settings 和 Environment Vaiables 都不用填
- 直接点部署 Deploy

特别注意：

部署完成后，如果 versel 给的地址是 https://xxx.xxx.vercel.app/ ，直接访问这个地址会失败！
应当在网址后加上 /api/index，也就是 https://xxx.xxx.vercel.app/api/index ，这样才能访问成功。
