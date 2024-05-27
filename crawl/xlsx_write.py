# 액셀 저장 모듈 (py로 만든 건 모두 모듈, 다른 py에서 사용 가능)
# 함수로 만든 후 불러쓰기

from openpyxl import Workbook

# listdata = [[], [], []]

# import os
# 현재 디렉토리 위치 확인 : print(os.getcwd())


def write_excel_template(filename, sheetname, listdata):
    # openpyxl workbook 생성
    wb = Workbook()
    ws = wb.active

    ws.title = sheetname
    # 너비 조정
    ws.column_dimensions["A"].width = 100

    # 행 삽입
    for row in listdata:
        ws.append(row)

    base_dir = "./crawl/file/"
    wb.save(base_dir + filename)
    wb.close()


# 모듈 테스트용
if __name__ == "__main__":
    listdata = [["이름", "나이"], ["홍길동", 25], ["성춘향", 22]]
    write_excel_template("temp.xlsx", "test", listdata)
