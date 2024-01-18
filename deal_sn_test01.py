import logging
import time
from datetime import datetime
from decimal import Decimal

import MySQLdb
from dateutil.relativedelta import *

from my_utils.MysqlUtility import MySQL
from itertools import groupby

logger = logging.getLogger("deal_equity_data")
logger.setLevel(logging.DEBUG)
fileHandler = logging.FileHandler("import.log")
fileHandler.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
cnslhandler = logging.StreamHandler()
cnslhandler.setLevel(logging.DEBUG)
cnslhandler.setFormatter(formatter)
logger.addHandler(cnslhandler)

edun_pro_cfg = {
    "host": "192.168.5.22",
    "port": 3307,
    "user": "user_yangll",
    "passwd": "vGxw9jWg",
    "db": "gps",
    "charset": "utf8",
}


edun_test_cfg = {
    "host": "192.168.3.222",
    "port": 3307,
    "user": "root",
    "passwd": "Msd^*$@online",
    "db": "newgps",
    "charset": "utf8",
}


from pymysql.converters import escape_string

#
def paddstr(strx):
    return "NULL" if strx == None else "\'" + escape_string(str(strx))+ "\'"


def deal_sn_data():
    bizProConn = MySQL(edun_pro_cfg)
    sql = """
       SELECT deviceType,deviceNo,sn,imsi,iccid,simPhone,isActive,activeDate,checkCode,modelId,userId,createtime,updateTime,d_LoginUserId,issub,vehicleId,partner,validateStatus,validateBy,validateNums,soft_version,imei,deviceId,source,networkCardNubmer FROM d_track_info dti WHERE dti.sn IN (	
       SELECT dti.sn
       FROM d_vehicle dv,
       d_track_info dti,
       d_class dc
       WHERE dti.vehicleId = dv.vehicleId
       AND dc.classid = dv.classId
       AND dv.status = 0
       AND dc.vehicleGroupId IN (402));
    """
    if not bizProConn.query(sql):
        logger.error("deal_equity_data fail, sql=%s", sql)
        return
    result = bizProConn.fetchAllRows()
    for row in result:
        print(row)
        bizTestConn = MySQL(edun_test_cfg)
        sql01 = f"""
        INSERT INTO d_track_info (deviceType,deviceNo,sn,imsi,iccid,simPhone,isActive,activeDate,checkCode,modelId,userId,createtime,updateTime,d_LoginUserId,issub,vehicleId,partner,validateStatus,validateBy,validateNums,imei,soft_version,deviceId,source,networkCardNubmer) VALUES
	      ({paddstr(row[0])},{paddstr(row[1])},{paddstr(row[2])},{paddstr(row[3])},{paddstr(row[4])},{paddstr(row[5])},{paddstr(row[6])},{paddstr(row[7])},{paddstr(row[8])},{paddstr(row[9])},{paddstr(row[10])},{paddstr(row[11])},{paddstr(row[12])},{paddstr(row[13])},{paddstr(row[14])},{paddstr(row[15])},{paddstr(row[16])},{paddstr(row[17])},{paddstr(row[18])},{paddstr(row[19])},{paddstr(row[20])},{paddstr(row[21])},{paddstr(row[22])},{paddstr(row[23])},{paddstr(row[24])});
        """
        print(sql01)
        bizTestConn.insert(sql01)


if __name__ == "__main__":
    deal_sn_data()
