# 面试题

后端 serve 启动方法：

1. 进入 backend 目录

2. 安装依赖 `pip install -r requirements.txt`

3. 修改 `backend/app/__init__.py` 中的数据库链接

4. 运行 `init.sql` 生成数据库表

5. 运行 `python -m flask run` 文件启动服务

前端 web 启动方法

1. 进入 frontend 目录

2. （按需）修改 `frontend/src/lib/user/index.ts` 中的 `baseURL`

3. 进入 frontend 文件夹，运行 `yarn & yarn dev` 命令
