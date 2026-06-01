saving_accounts = [
    {
        "account_id": "STK001",
        "customer_name": "Nguyễn Văn An",
        "balance": 50000000,
        "term_months": 6,
        "interest_rate": 6.5,
        "status": "active"
    },
    {
        "account_id": "STK002",
        "customer_name": "Trần Thị Bình",
        "balance": 120000000,
        "term_months": 12,
        "interest_rate": 7.2,
        "status": "active"
    }
]

while True:
    print("\n")
    print("=" * 67)
    print("   HỆ THỐNG QUẢN LÝ TÀI KHOẢN TIẾT KIỆM TECHBANK   ")
    print("=" * 67)
    print("1. Xem danh sách sổ tiết kiệm")
    print("2. Mở sổ tiết kiệm mới")
    print("3. Cập nhật thông tin sổ tiết kiệm")
    print("4. Tất toán sổ tiết kiệm")
    print("5. Tính lãi dự kiến khi đến hạn")
    print("6. Kiểm tra điều kiện rút trước hạn")
    print("7. Thoát chương trình")
    print("=" * 57)

    # Input: Người dùng nhập lựa chọn menu
    choice = input("Nhập lựa chọn của bạn: ").strip()

    # Output: Thông báo lỗi nếu nhập ngoài phạm vi từ 1 đến 7
    if choice not in ["1", "2", "3", "4", "5", "6", "7"]:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại")
        continue

    if choice == "1":
        print("\n--- DANH SÁCH SỔ TIẾT KIỆM ---")
        # Output: Thông báo nếu danh sách không có dữ liệu
        if len(saving_accounts) == 0:
            print("Danh sách sổ tiết kiệm hiện đang trống")
        else:
            # Output: In toàn bộ danh sách sổ tiết kiệm hiện có
            for i, acc in enumerate(saving_accounts, start=1):
                print(
                    f"{i}. Mã sổ: {acc['account_id']} | "
                    f"Khách hàng: {acc['customer_name']} | "
                    f"Số tiền gửi: {acc['balance']} | "
                    f"Kỳ hạn: {acc['term_months']} tháng | "
                    f"Lãi suất: {acc['interest_rate']}%/năm | "
                    f"Trạng thái: {acc['status']}"
                )   

    elif choice == "2":
        print("\n--- MỞ SỔ TIẾT KIỆM MỚI ---")
        # Input: Nhập mã sổ tiết kiệm mới
        input_id = input("Nhập mã sổ tiết kiệm: ").strip().upper()

        da_ton_tai = False
        for acc in saving_accounts:
            if acc["account_id"] == input_id:
                da_ton_tai = True
                break

        # Output: Thông báo lỗi trùng mã sổ
        if da_ton_tai:
            print("Mã sổ tiết kiệm đã tồn tại!")
        else:
            # Input: Nhập tên khách hàng mới
            input_name = input("Nhập tên khách hàng: ").strip()
            
            # Output: Thông báo lỗi bỏ trống tên
            if input_name == "":
                print("Tên khách hàng không được để trống")
            else:
                # Input: Nhập số tiền gửi và kỳ hạn gửi dưới dạng chuỗi thô
                raw_balance = input("Nhập số tiền gửi: ").strip()
                raw_term = input("Nhập kỳ hạn gửi theo tháng: ").strip()
                
                # Output: Thông báo lỗi nếu tiền gửi hoặc kỳ hạn không phải số nguyên dương
                if not raw_balance.isdigit() or not raw_term.isdigit() or int(raw_balance) <= 0 or int(raw_term) <= 0:
                    print("Số tiền gửi hoặc kỳ hạn không hợp lệ")
                else:
                    # Input: Nhập lãi suất năm dưới dạng chuỗi thô
                    raw_rate = input("Nhập lãi suất năm: ").strip()
                    
                    la_hop_le = True
                    if not raw_rate or raw_rate.count('.') > 1:
                        la_hop_le = False
                    else:
                        chuoi_so = raw_rate.replace('.', '', 1)
                        if not chuoi_so.isdigit() or float(raw_rate) <= 0:
                            la_hop_le = False
                    
                    # Output: Thông báo lỗi nếu lãi suất không hợp lệ
                    if not la_hop_le:
                        print("Lãi suất không hợp lệ!")
                    else:
                        input_balance = int(raw_balance)
                        input_term = int(raw_term)
                        input_rate = float(raw_rate)
                        
                        saving_accounts.append({
                            "account_id": input_id,
                            "customer_name": input_name,
                            "balance": input_balance,
                            "term_months": input_term,
                            "interest_rate": input_rate,
                            "status": "active"
                        })
                        # Output: Thông báo thêm tài khoản mới thành công
                        print(f"Đã mở sổ tiết kiệm mới: {input_id} – {input_name}")

    elif choice == "3":
        print("\n--- CẬP NHẬT THÔNG TIN SỔ TIẾT KIỆM ---")
        # Input: Nhập mã sổ cần cập nhật thông tin
        input_id = input("Nhập mã sổ tiết kiệm cần cập nhật: ").strip().upper()

        tim_thay = False
        index_so = -1
        for i, acc in enumerate(saving_accounts):
            if acc["account_id"] == input_id:
                tim_thay = True
                index_so = i
                break

        # Output: Thông báo lỗi không tìm thấy mã sổ
        if not tim_thay:
            print("Không tìm thấy mã sổ tiết kiệm!")
        else:
            # Output: Thông báo lỗi nếu sổ đã tất toán (closed)
            if saving_accounts[index_so]["status"] == "closed":
                print("Không thể cập nhật sổ tiết kiệm đã tất toán!")
            else:
                # Input: Nhập tên khách hàng mới để cập nhật
                input_name = input("Nhập tên khách hàng mới: ").strip()
                
                # Output: Thông báo lỗi bỏ trống tên mới
                if input_name == "":
                    print("Tên khách hàng không được để trống")
                else:
                    # Input: Nhập số tiền gửi mới và kỳ hạn mới
                    raw_balance = input("Nhập số tiền gửi mới: ").strip()
                    raw_term = input("Nhập kỳ hạn mới theo tháng: ").strip()
                    
                    # Output: Thông báo lỗi nếu thông tin mới không phải số nguyên dương
                    if not raw_balance.isdigit() or not raw_term.isdigit() or int(raw_balance) <= 0 or int(raw_term) <= 0:
                        print("Số tiền gửi hoặc kỳ hạn không hợp lệ")
                    else:
                        # Input: Nhập lãi suất năm mới
                        raw_rate = input("Nhập lãi suất năm mới: ").strip()
                        
                        la_hop_le = True
                        if not raw_rate or raw_rate.count('.') > 1:
                            la_hop_le = False
                        else:
                            chuoi_so = raw_rate.replace('.', '', 1)
                            if not chuoi_so.isdigit() or float(raw_rate) <= 0:
                                la_hop_le = False
                        
                        # Output: Thông báo lỗi lãi suất mới không hợp lệ
                        if not la_hop_le:
                            print("Lãi suất không hợp lệ!")
                        else:
                            saving_accounts[index_so]["customer_name"] = input_name
                            saving_accounts[index_so]["balance"] = int(raw_balance)
                            saving_accounts[index_so]["term_months"] = int(raw_term)
                            saving_accounts[index_so]["interest_rate"] = float(raw_rate)
                            # Output: Thông báo cập nhật dữ liệu thành công
                            print(f"Đã cập nhật sổ {input_id} thành công.")

    elif choice == "4":
        print("\n--- TẤT TOÁN SỔ TIẾT KIỆM ---")
        # Input: Nhập mã sổ cần thực hiện tất toán
        input_id = input("Nhập mã sổ tiết kiệm cần tất toán/xóa: ").strip().upper()

        tim_thay = False
        index_so = -1
        for i, acc in enumerate(saving_accounts):
            if acc["account_id"] == input_id:
                tim_thay = True
                index_so = i
                break

        # Output: Thông báo lỗi không tìm thấy mã sổ
        if not tim_thay:
            print("Không tìm thấy mã sổ tiết kiệm!")
        else:
            # Output: Thông báo nếu sổ đã đóng từ trước
            if saving_accounts[index_so]["status"] == "closed":
                print("Sổ tiết kiệm này đã được tất toán trước đó.")
            else:
                saving_accounts[index_so]["status"] = "closed"
                # Output: Thông báo tất toán thành công và đổi trạng thái sang closed
                print(f"Đã tất toán sổ {input_id} – {saving_accounts[index_so]['customer_name']}. Trạng thái: closed")

    elif choice == "5":
        print("\n--- TÍNH LÃI DỰ KIẾN KHI ĐẾN HẠN ---")
        # Input: Nhập mã sổ cần tính toán tiền lãi đến hạn
        input_id = input("Nhập mã sổ tiết kiệm cần tính lãi: ").strip().upper()

        tim_thay = False
        index_so = -1
        for i, acc in enumerate(saving_accounts):
            if acc["account_id"] == input_id:
                tim_thay = True
                index_so = i
                break

        # Output: Thông báo lỗi không tìm thấy mã sổ
        if not tim_thay:
            print("Không tìm thấy mã sổ tiết kiệm!")
        else:
            # Output: Thông báo lỗi từ chối thao tác với sổ đã closed
            if saving_accounts[index_so]["status"] == "closed":
                print("Không thể thao tác với sổ tiết kiệm đã tất toán")
            else:
                hien_tai = saving_accounts[index_so]
                tien_lai = hien_tai["balance"] * hien_tai["interest_rate"] / 100 * hien_tai["term_months"] / 12
                tong_tien = hien_tai["balance"] + tien_lai
                
                # Output: Hiển thị bảng tính toán số tiền lãi và tổng số tiền nhận dự kiến
                print(f"\nSổ: {hien_tai['account_id']} | Khách hàng: {hien_tai['customer_name']}")
                print(f"Số tiền gửi      : {hien_tai['balance']:,} VNĐ")
                print(f"Kỳ hạn           : {hien_tai['term_months']} tháng")
                print(f"Lãi suất         : {hien_tai['interest_rate']}%/năm")
                print(f"Tiền lãi dự kiến : {tien_lai:,} VNĐ")
                print(f"Tổng tiền nhận   : {tong_tien:,} VNĐ")

    elif choice == "6":
        print("\n--- KIỂM TRA ĐIỀU KIỆN RÚT TRƯỚC HẠN ---")
        # Input: Nhập mã sổ cần thực hiện kiểm tra rút tiền trước hạn
        input_id = input("Nhập mã sổ tiết kiệm cần kiểm tra: ").strip().upper()

        tim_thay = False
        index_so = -1
        for i, acc in enumerate(saving_accounts):
            if acc["account_id"] == input_id:
                tim_thay = True
                index_so = i
                break

        # Output: Thông báo lỗi không tìm thấy mã sổ
        if not tim_thay:
            print("Không tìm thấy mã sổ tiết kiệm!")
        else:
            # Output: Thông báo lỗi từ chối thao tác với sổ đã closed
            if saving_accounts[index_so]["status"] == "closed":
                print("Không thể thao tác với sổ tiết kiệm đã tất toán")
            else:
                # Input: Nhập số tháng thực tế mà khách hàng đã gửi tiền
                raw_months = input("Nhập số tháng thực gửi: ").strip()
                
                # Output: Thông báo lỗi số tháng thực gửi không phải số nguyên dương
                if not raw_months.isdigit() or int(raw_months) <= 0:
                    print("Số tháng thực gửi không hợp lệ!")
                else:
                    thang_thuc_gui = int(raw_months)
                    hien_tai = saving_accounts[index_so]
                    
                    if thang_thuc_gui < hien_tai["term_months"]:
                        lai_suat_ap_dung = 0.5
                        loai = "RÚT TRƯỚC HẠN"
                    else:
                        lai_suat_ap_dung = hien_tai["interest_rate"]
                        loai = "ĐỦ KỲ HẠN"

                    tien_lai = hien_tai["balance"] * lai_suat_ap_dung / 100 * thang_thuc_gui / 12
                    tong_tien = hien_tai["balance"] + tien_lai

                    # Output: Hiển thị chi tiết kết quả phân loại kỳ hạn, lãi suất áp dụng và số tiền nhận thực tế
                    print(f"\nSổ: {hien_tai['account_id']} | Khách hàng: {hien_tai['customer_name']}")
                    print(f"  Kỳ hạn ban đầu     : {hien_tai['term_months']} tháng")
                    print(f"  Số tháng thực gửi  : {thang_thuc_gui} tháng")
                    print(f"  Kết quả            : {loai}")
                    print(f"  Lãi suất áp dụng   : {lai_suat_ap_dung}%/năm")
                    print(f"  Tiền lãi thực nhận : {tien_lai:,} VNĐ")
                    print(f"  Tổng tiền thực nhận: {tong_tien:,} VNĐ")

    elif choice == "7":
        # Output: Thông báo thoát
        print("Thoát chương trình")
        break
