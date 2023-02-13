# -*- coding: utf-8 -*-

# 신고 유형
RECV_EMG_CD_긴급="C0"
RECV_EMG_CD_중요="C1"
RECV_EMG_CD_일반="C2"
RECV_EMG_CD_민원="C3"
RECV_EMG_CD_기타="C4"

# 종결 코드
END_CD_체포 = "101"
END_CD_임의동행 = "102"
END_CD_통고처분 = "103"
END_CD_즉결심판 = "104"
END_CD_검거후훈방 = "105"
END_CD_현장조치 = "201"
END_CD_합의해산 = "202"
END_CD_순찰강화 = "203"
END_CD_상담안내 = "204"
END_CD_훈방 = "205"
END_CD_계속조사 = "301"
END_CD_보호조치 = "302"
END_CD_수배조치 = "303"
END_CD_타부서인계 = "304"
END_CD_타청_타서인계 = "305"
END_CD_타기관인계 = "401"
END_CD_귀가조치 = "402"
END_CD_병원인계 = "403"
END_CD_이미해산 = "501"
END_CD_불발견 = "502"
END_CD_신고취소 = "503"
END_CD_무조취종결 = "504"
END_CD_무응답 = "505"
END_CD_미도착종결 = "506"
END_CD_허위오인 = "601"
END_CD_오인 = "602"
END_CD_오작동 = "603"
END_CD_FTX = "604"
END_CD_경찰콜센터 = "701"
END_CD_110 = "702"
END_CD_타청_타서 = "703"
END_CD_기타 = "704"
END_CD_상담안내 = "705"
END_CD_수배조치 = "706"
END_CD_조치없이_종결 = "707"
END_CD_동일 = "708"
END_CD_이첩 = "709"
END_CD_FAX전송종결 = "710"

# 사건 종별 코드
EVT_CL_CD_살인 = "101"
EVT_CL_CD_강도 = "102"
EVT_CL_CD_치기 = "103"
EVT_CL_CD_절도 = "104"
EVT_CL_CD_납치감금 = "105"
EVT_CL_CD_성폭력 = "106"
EVT_CL_CD_가정폭력 = "107"
EVT_CL_CD_아동학대_가정내 = "108"
EVT_CL_CD_아동학대_기타 = "109"
EVT_CL_CD_폭력 = "201"
EVT_CL_CD_사기 = "202"
EVT_CL_CD_공갈 = "203"
EVT_CL_CD_협박 = "204"
EVT_CL_CD_도박 = "205"
EVT_CL_CD_재물손괴 = "206"
EVT_CL_CD_주거침입 = "207"
EVT_CL_CD_풍속영업 = "208"
EVT_CL_CD_수배불심자 = "209"
EVT_CL_CD_기타형사범 = "210"
EVT_CL_CD_데이트폭력 = "211"
EVT_CL_CD_스토킹 = "212"
EVT_CL_CD_학교폭력 = "213"
EVT_CL_CD_마약 = "214"
EVT_CL_CD_보이스피싱 = "215"
EVT_CL_CD_동물학대 = "216"
EVT_CL_CD_시비 = "301"
EVT_CL_CD_행패소란 = "302"
EVT_CL_CD_청소년비행 = "303"
EVT_CL_CD_무전취식승차 = "304"
EVT_CL_CD_주취자 = "305"
EVT_CL_CD_보호조치 = "306"
EVT_CL_CD_위험방지 = "307"
EVT_CL_CD_기타경범 = "308"
EVT_CL_CD_교통사고 = "401"
EVT_CL_CD_교통불편 = "402"
EVT_CL_CD_교통위반 = "403"
EVT_CL_CD_사망_대형사고 = "404"
EVT_CL_CD_인피도주 = "405"
EVT_CL_CD_음주운전 = "406"
EVT_CL_CD_상담문의 = "501"
EVT_CL_CD_변사자 = "502"
EVT_CL_CD_비상벨 = "503"
EVT_CL_CD_경비업체요청 = "504"
EVT_CL_CD_가출_등 = "505"
EVT_CL_CD_분실습득 = "506"
EVT_CL_CD_FTX = "507"
EVT_CL_CD_자살 = "508"
EVT_CL_CD_실종_실종아동_등 = "509"
EVT_CL_CD_내용확인불가 = "601"
EVT_CL_CD_화재 = "602"
EVT_CL_CD_구조요청 = "603"
EVT_CL_CD_소음 = "604"
EVT_CL_CD_노점상 = "605"
EVT_CL_CD_기타_타기관 = "606"
EVT_CL_CD_서비스요청 = "607"
EVT_CL_CD_청탁금지법 = "608"
EVT_CL_CD_재해재난 = "609"
EVT_CL_CD_위험동물 = "610"

'''
arrest : 검거
investigation : 계속조사 
end_report : 신고종결
not_handle : 미처리 
'''

def end_cd_arrest_mask(df):     # 검거 마스킹
    return (df.end_cd == END_CD_체포) | (df.end_cd == END_CD_임의동행) | (df.end_cd == END_CD_통고처분) | (
            df.end_cd == END_CD_즉결심판) | (df.end_cd == END_CD_검거후훈방)

def end_cd_investigation_mask(df):      # 계속조사 마스킹
    return (df.end_cd == END_CD_계속조사) | (df.end_cd == END_CD_보호조치) | (df.end_cd == END_CD_수배조치) | (
            df.end_cd == END_CD_타부서인계) | (df.end_cd == END_CD_타청_타서인계)

def end_cd_end_report_mask(df):     # 신고종결 마스킹
    return (df.end_cd == END_CD_현장조치) | (df.end_cd == END_CD_합의해산) | (df.end_cd == END_CD_순찰강화) | (
            df.end_cd == END_CD_상담안내) | (df.end_cd == END_CD_훈방) | (df.end_cd == END_CD_타기관인계) | (
            df.end_cd == END_CD_귀가조치) | (df.end_cd == END_CD_병원인계) | (df.end_cd == END_CD_허위오인) | (
            df.end_cd == END_CD_오인) | (df.end_cd == END_CD_오작동) | (df.end_cd == END_CD_FTX) | (
            df.end_cd == END_CD_경찰콜센터) | (df.end_cd == END_CD_110) | (df.end_cd == END_CD_타청_타서) | (
            df.end_cd == END_CD_기타) | (df.end_cd == END_CD_상담안내) | (df.end_cd == END_CD_수배조치) | (
            df.end_cd == END_CD_조치없이_종결) | (df.end_cd == END_CD_동일) | (df.end_cd == END_CD_이첩) | (
            df.end_cd == END_CD_FAX전송종결)


def end_cd_not_handle_mask(df):     # 미처리 마스킹
    return (df.end_cd == END_CD_이미해산) | (df.end_cd == "0") | (df.end_cd == END_CD_불발견) | (
            df.end_cd == END_CD_신고취소) | (df.end_cd == END_CD_무조취종결) | (df.end_cd == END_CD_무응답) | (
            df.end_cd == END_CD_미도착종결)

def end_cd_mask_list(report) :
    return [end_cd_arrest_mask(report),
            end_cd_investigation_mask(report),
            end_cd_end_report_mask(report),
            end_cd_not_handle_mask(report)]

