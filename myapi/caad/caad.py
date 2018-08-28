# _*_ coding:utf-8 _*_
from __future__ import absolute_import, print_function, division
from ..Model.models import Apiconfig
from Crypto.Cipher import AES
import base64
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from base64 import b64decode
import urllib2
import json
import uuid




def caseid():
    return str(uuid.uuid1()).replace('-', '')


# region Aes加密解密
def AES_encrypt(content, aes_Key):  # 加密
    BS = AES.block_size
    pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
    cipher = AES.new(aes_Key)
    encrypted = cipher.encrypt(pad(content))
    result = base64.b64encode(encrypted)
    return result


def AES_decrypt(content, aes_Key):  # 解密
    unpad = lambda s: s[0:-ord(s[-1])]
    cipher = AES.new(aes_Key)
    result = base64.b64decode(content)
    decrypted = unpad(cipher.decrypt(result))
    return decrypted


# region RSA加签验签
def RSA_sign(data, private_key):
    # print(private_key)
    rsakey = RSA.importKey(b64decode(private_key))
    signer = PKCS1_v1_5.new(rsakey)
    digest = SHA.new(data)
    signature = signer.sign(digest)
    result = base64.b64encode(signature)
    return result


def RSA_verify(data, signature, public_rsa_Key):
    """
          验证函数使用指定的公钥对返回签名结果进行验证
          :param data: 原始数据文件（此处的原始数据并非明文，而是AES加密过后的密文）
          :param signature: RSA加签过后的数据
          :param public_rsa_Key: 用于验证的公钥
          :return: 成功返回True, 失败返回False
          """
    rsakey = RSA.importKey(b64decode(public_rsa_Key))
    verifier = PKCS1_v1_5.new(rsakey)
    digest = SHA.new(data)
    return verifier.verify(digest, base64.b64decode(signature))


# endregion

# region Http请求
def post(url, data):
    header = {'content-type': 'application/json; charset=utf-8'}
    jdata = json.dumps(data)
    req = urllib2.Request(url, jdata, header)
    response = urllib2.urlopen(req)
    return response.read()


def handle(conten):
    content, aes, private_key, public_rsa_Key, url, username, node = data(conten)
    encrypt_content = AES_encrypt(json.dumps(content), aes)
    signature = RSA_sign(encrypt_content, private_key)
    result_data = (post(url, {'Data': encrypt_content + "," + signature}))[1:-1]  # 对返回的结果进行字符串截取（"）, 否则会影响验证结果
    result_encrpyt_content = result_data.split(',')[0]
    result_signature = result_data.split(',')[1]

    if RSA_verify(result_encrpyt_content, result_signature, public_rsa_Key):
        # print(("验签成功").decode("utf-8"))
        result = json.loads(AES_decrypt(result_encrpyt_content, aes))
    else:
        result = json.loads(AES_decrypt(result_encrpyt_content, aes))
        # result["data"] =  "验签失败"
    config = {"url": url, "username": username, "node": node}
    return content, result, config


def db(Key):
    data = Apiconfig.objects.get(key=Key)
    return data


def data(content):
    content["CaseId"] = caseid()
    config = db(content['Key'])
    aes = config.aes
    private_key = config.private_rsa_key
    public_rsa_Key = config.public_rsa_key
    host = config.host
    testhost = config.testhost
    url = config.url
    username = config.name
    if content.has_key('setting') and content["setting"]:
        hosturl = host + url
        node = "正式环境"
    else:
        hosturl = testhost + url
        node = "测试环境"

    return content, aes, private_key, public_rsa_Key, hosturl, username, node