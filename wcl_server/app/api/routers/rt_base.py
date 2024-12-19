# coding=utf8
from fastapi import APIRouter, Request

from app.core.config import settings

# 定义路由
base_rt = APIRouter(prefix='/base', tags=['base'])

# 接受参数
@base_rt.post('/authorize')

async def handleAuthorize(request:Request):

    body = await request.body()
    print(body)