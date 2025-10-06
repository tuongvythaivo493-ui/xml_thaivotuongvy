from lxml import etree
import os

file_path = os.path.join(os.path.dirname(__file__), "sv.xml")
tree = etree.parse(file_path)
root = tree.getroot()

print("1. Tất cả sinh viên:")
student_ids = root.xpath("//student/id/text()")
student_names = root.xpath("//student/name/text()")
student_dates = root.xpath("//student/date/text()")
for i, (student_id, name, date) in enumerate(zip(student_ids, student_names, student_dates), 1):
    print(f"  {i}. Mã SV: {student_id}, Tên: {name}, Ngày sinh: {date}")
print("\n" + "="*50 + "\n")
print("- Số lượng:", len(root.xpath("//student")), "\n")

print("2. Tên tất cả sinh viên:")
print(root.xpath("//student/name/text()"), "\n")

print("3. ID của sinh viên:")
print(root.xpath("//student/id/text()"), "\n")

print("4. Ngày sinh SV01:")
print(root.xpath("//student[id='SV01']/date/text()"), "\n")

print("5. Các khóa học:")
print(root.xpath("//enrollment/course/text()"), "\n")

print("6. Sinh viên đầu tiên:")
sv_first = root.xpath("//student[1]")
print(etree.tostring(sv_first[0], pretty_print=True, encoding='unicode'), "\n")

print("7. Mã sinh viên học Vatly203:")
print(root.xpath("//enrollment[course='Vatly203']/studentRef/text()"), "\n")

print("8. Tên sinh viên học Toan101:")
print(root.xpath("//student[id=//enrollment[course='Toan101']/studentRef]/name/text()"), "\n")

print("9. Tên sinh viên học Vatly203:")
print(root.xpath("//student[id=//enrollment[course='Vatly203']/studentRef]/name/text()"), "\n")

print("10. Ngày sinh SV01:")
print(root.xpath("//student[id='SV01']/date/text()"), "\n") 

print("11. Sinh viên sinh năm 1997 (tên + ngày sinh):")
print(root.xpath("//student[starts-with(date,'1997')]/name/text() | //student[starts-with(date,'1997')]/date/text()"), "\n")

print("12. Sinh viên sinh trước năm 1998:")
print(root.xpath("//student[number(substring(date,1,4))<1998]/name/text()"), "\n")

print("13. Tổng số sinh viên:")
print(root.xpath("count(//student)"), "\n")

print("14. Sinh viên chưa đăng ký môn nào:")
print(root.xpath("//student[not(id=//enrollment/studentRef)]/name/text()"), "\n")

print("15. <date> sau <name> của SV01:")
print(root.xpath("//student[id='SV01']/name/following-sibling::date/text()"), "\n")

print("16. <id> trước <name> của SV02:")
print(root.xpath("//student[id='SV02']/name/preceding-sibling::id/text()"), "\n")

print("17. Node <course> của SV03:")
print(root.xpath("//enrollment[studentRef='SV03']/course/text()"), "\n")

print("18. Sinh viên họ Trần:")
print(root.xpath("//student[starts-with(name,'Trần')]/name/text()"), "\n")

print("19. Năm sinh của SV01:")
print(root.xpath("substring(//student[id='SV01']/date,1,4)"), "\n")
