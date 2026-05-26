branch_names = ["Highlands Nhà Thờ", "Highlands Bà Triệu", "Highlands Nguyễn Du", "Highlands Landmark 81", "Highlands Trần Hưng Đạo"]
daily_revenues = [15500000, 28000000, 9200000, 45000000, 11000000] 
target_achieved = [True, True, False, True, False] 
status = ""

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ DOANH THU HIGHLANDS =====")
    print("1. Hiển thị báo cáo doanh thu tổng hợp")
    print("2. Thống kê chi nhánh Cao nhất / Thấp nhất")
    print("3. Lọc danh sách cơ sở kém (Không đạt chỉ tiêu)")
    print("4. Thoát chương trình")
    print("================================================")

    choice = input("Nhập lựa chọn của bạn (1-4): ").strip()

    if choice == '1':

        total_revenue = 0
        print("\n--- BÁO CÁO DOANH THU TỔNG HỢP ---")
        print("Tên Cơ Sở                    | Doanh Thu      | Trạng Thái")

        for i, branch in enumerate(branch_names):
            revenue = daily_revenues[i]
            total_revenue += revenue

            if target_achieved[i]:
                status = "Đạt"
            else:
                status = "Không Đạt"
            print(f"{branch:<30} | {revenue:>13,} | {status}")

        print("--------------------------------------------------------------")
        print(f"TỔNG DOANH THU: {total_revenue:,} VNĐ")
    elif choice == '2':
        max_revenue = max(daily_revenues)
        min_revenue = min(daily_revenues)
        max_index = daily_revenues.index(max_revenue)
        min_index = daily_revenues.index(min_revenue)

        print("\n--- THỐNG KÊ DOANH THU ---")
        print(f"Chi nhánh doanh thu cao nhất là: "f"{branch_names[max_index]} - {max_revenue} VNĐ")
        print(f"Chi nhánh doanh thu thấp nhất là: "f"{branch_names[min_index]} - {min_revenue} VNĐ")
    elif choice == '3':
        failed_branches = []
        for index, value in enumerate(target_achieved):
            if value == False:
                failed_branches.append(branch_names[index])
        print("\n--- DANH SÁCH CƠ SỞ KHÔNG ĐẠT CHỈ TIÊU ---")
        print(failed_branches)
    elif choice == '4':
        print("Hệ thống ghi nhận dữ liệu hoàn tất. Tạm biệt!")
        break
    else:
        print("[Lỗi] Lựa chọn không hợp lệ, vui lòng nhập lại số từ 1 đến 4!")