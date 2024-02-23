# 面试题

后端 serve 启动方法：

1. 修改 `backend/app/__init__.py` 中的数据库链接

2. 运行 `init.sql` 生成数据库表

3. 运行 `backend/run.py` 文件启动服务

前端 web 启动方法

1. （按需）修改 `frontend/src/lib/user/index.ts` 中的 `baseURL`

2. 进入 frontend 文件夹，运行 `yarn & yarn dev` 命令
