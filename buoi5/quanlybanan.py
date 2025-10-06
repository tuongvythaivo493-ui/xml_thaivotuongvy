from lxml import etree
import os

file_path = os.path.join(os.path.dirname(__file__), "quanlybanan.xml")
tree = etree.parse(file_path)
root = tree.getroot()

print("\n1. Lấy tất cả bàn:")
bans = root.xpath("//BAN")
for ban in bans:
    soban = ban.findtext("SOBAN")
    tenban = ban.findtext("TENBAN")
    print(f"  - Số bàn: {soban}, Tên bàn: {tenban}")

print("\n2. Lấy tất cả nhân viên:")
nhanviens = root.xpath("//NHANVIEN")
for nv in nhanviens:
    manv = nv.findtext("MANV")
    tenv = nv.findtext("TENV")
    print(f"  - Mã NV: {manv}, Tên: {tenv}")

print("\n3. Lấy tất cả tên món:")
ten_mons = root.xpath("//MON/TENMON/text()")
for ten in ten_mons:
    print(f"  - {ten}")

print("\n4. Lấy tên nhân viên có mã NV02:")
ten_nv02 = root.xpath("//NHANVIEN[MANV='NV02']/TENV/text()")
print(f"  - Tên nhân viên: {ten_nv02[0]}")

print("\n5. Lấy tên và số điện thoại của nhân viên NV03:")
nv03 = root.xpath("//NHANVIEN[MANV='NV03']")[0]
ten_nv03 = nv03.findtext("TENV")
sdt_nv03 = nv03.findtext("SDT")
print(f"  - Tên: {ten_nv03}, SĐT: {sdt_nv03}")

print("\n6. Lấy tên món có giá > 50,000:")
mon_gia_cao = root.xpath("//MON[GIA > 50000]/TENMON/text()")
for ten_mon in mon_gia_cao:
    print(f"  - {ten_mon}")

print("\n7. Lấy số bàn của hóa đơn HD03:")
soban_hd03 = root.xpath("//HOADON[SOHD='HD03']/SOBAN/text()")
print(f"  - Số bàn: {soban_hd03[0]}")

print("\n8. Lấy tên món có mã M02:")
ten_m02 = root.xpath("//MON[MAMON='M02']/TENMON/text()")
print(f"  - Tên món: {ten_m02[0]}")

print("\n9. Lấy ngày lập của hóa đơn HD03:")
ngaylap_hd03 = root.xpath("//HOADON[SOHD='HD03']/NGAYLAP/text()")
print(f"  - Ngày lập: {ngaylap_hd03[0]}")

print("\n10. Lấy tất cả mã món trong hóa đơn HD01:")
mamons_hd01 = root.xpath("//HOADON[SOHD='HD01']//CTHD/MAMON/text()")
print(f"  - Các mã món: {mamons_hd01}")

print("\n11. Lấy tên món trong hóa đơn HD01:")
tenmons_hd01 = root.xpath("//MON[MAMON = //HOADON[SOHD='HD01']//CTHD/MAMON]/TENMON/text()")
for ten in tenmons_hd01:
    print(f"  - {ten}")

print("\n12. Lấy tên nhân viên lập hóa đơn HD02:")
tenv_hd02 = root.xpath("//NHANVIEN[MANV = //HOADON[SOHD='HD02']/MANV]/TENV/text()")
print(f"  - Tên nhân viên: {tenv_hd02[0]}")

print("\n13. Đếm số bàn:")
so_ban = root.xpath("count(//BAN)")
print(f"  - Tổng số bàn: {int(so_ban)}")

print("\n14. Đếm số hóa đơn lập bởi NV01:")
so_hd_nv01 = root.xpath("count(//HOADON[MANV='NV01'])")
print(f"  - Số hóa đơn: {int(so_hd_nv01)}")

print("\n15. Lấy tên tất cả món có trong hóa đơn của bàn số 2:")
tenmon_ban2 = root.xpath("//MON[MAMON = //HOADON[SOBAN='2']//CTHD/MAMON]/TENMON/text()")
for ten in tenmon_ban2:
    print(f"  - {ten}")

print("\n16. Lấy tất cả nhân viên từng lập hóa đơn cho bàn số 3:")
nv_ban3 = root.xpath("//NHANVIEN[MANV = //HOADON[SOBAN='3']/MANV]")
for nv in nv_ban3:
    print(f"  - Tên nhân viên: {nv.findtext('TENV')}")

print("\n17. Lấy tất cả hóa đơn mà nhân viên nữ lập:")
hd_nv_nu = root.xpath("//HOADON[MANV = //NHANVIEN[GIOITINH='Nữ']/MANV]")
for hd in hd_nv_nu:
    print(f"  - Số hóa đơn: {hd.findtext('SOHD')}, do NV: {hd.findtext('MANV')}")

print("\n18. Lấy tất cả nhân viên từng phục vụ bàn số 1:")
nv_ban1 = root.xpath("//NHANVIEN[MANV = //HOADON[SOBAN='1']/MANV]")
for nv in nv_ban1:
    print(f"  - Tên nhân viên: {nv.findtext('TENV')}")

print("\n19. Lấy tất cả món được gọi nhiều hơn 1 lần trong các hóa đơn:")
mon_nhieu = root.xpath("//MON[MAMON = //CTHD[SOLUONG > 1]/MAMON]/TENMON/text()")
for ten in mon_nhieu:
    print(f"  - {ten}")

print("\n20. Lấy tên bàn + ngày lập hóa đơn tương ứng SOHD='HD02':")
# Lấy số bàn từ hóa đơn HD02
so_ban_hd02 = root.xpath("//HOADON[SOHD='HD02']/SOBAN/text()")[0]

# Dùng số bàn vừa lấy để tìm tên bàn
ten_ban_hd02 = root.xpath(f"//BAN[SOBAN='{so_ban_hd02}']/TENBAN/text()")[0]

# Lấy ngày lập hóa đơn
ngay_lap_hd02 = root.xpath("//HOADON[SOHD='HD02']/NGAYLAP/text()")[0]

print(f"  - Tên bàn: {ten_ban_hd02}")
print(f"  - Ngày lập: {ngay_lap_hd02}")