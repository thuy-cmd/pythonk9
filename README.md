# 1) Cập nhật nhánh chính

# git checkout main

# git fetch origin && git pull --rebase origin main

# 2) Tạo nhánh làm việc từ main mới nhất

# git checkout -b feat/<mo-ta>

# 3) Lưu & commit thay đổi

# git add -A && git commit -m "feat: <mo-ta>"

# 4) Đẩy nhánh lên repo gốc

# git push -u origin feat/<mo-ta>

# (MỞ PR trên Git hosting: feat/<mo-ta> → main)

# 5) Trong lúc code: luôn sync nhánh với main để tránh conflict

# git fetch origin && git rebase origin/main

# 6) Nếu đã từng push và vừa rebase: đẩy lại an toàn

# git push --force-with-lease

# 7) Sau khi PR được merge: về main và cập nhật

# git checkout main && git pull --rebase origin main

# 8) Dọn nhánh local đã dùng

# git branch -d feat/<mo-ta>

# 9) Dọn nhánh trên remote

# git push origin --delete feat/<mo-ta>

# 10) Kéo nhánh của bạn cùng lớp (nếu cần xem code bạn ấy)

# git fetch origin && git checkout -b friend/<ten-nhanh> origin/<ten-nhanh>

# Cap nhat lai file thu xem

# Da cap nhat

# Lam lai
