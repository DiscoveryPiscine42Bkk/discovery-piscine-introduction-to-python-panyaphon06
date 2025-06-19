def checkmate(board: str):
    board = board.strip().split('\n')
    size = len(board)  #เอาข้อความกระดานที่รับมา ตัดช่องว่าง + แยกบรรทัดเก็บไว้ในรูปแบบ list (board)เช่น '....\n.K..\n....\n.R..' → ['....', '.K..', '....', '.R..']
                        #size คือขนาดกระดาน เช่น ถ้ามี 4 แถว size = 4

    # ตรวจสอบว่าเป็นกระดานสี่เหลี่ยม
    for row in board: 
        if len(row) != size:
            print("Error")  #เช็กว่า แต่ละแถวต้องยาวเท่ากัน เช่น ต้องมี 4 ตัวอักษรในแต่ละแถวถ้าไม่ใช่ จะพิมพ์ "Error" และหยุด
            return

    # หาตำแหน่งของ King
    king_pos = None
    for i in range(size):
        for j in range(size):
            if board[i][j] == 'K':  #ไล่หาว่าตัว K อยู่ที่แถวไหน คอลัมน์ไหน แล้วเก็บไว้ในตัวแปร king_pos เช่น K อยู่แถว 1 คอลัมน์ 1 → king_pos = (1, 1)

                king_pos = (i, j)
                break
        if king_pos:
            break

    if not king_pos:
        print("Error")
        return

    def in_bounds(x, y):  #โค้ดอันนี้คือป้องกันการตรวจหมากนอกกระดาน
        return 0 <= x < size and 0 <= y < size

    def is_pawn_attacking():
        x, y = king_pos
        # Pawn ฝั่งตรงข้ามโจมตีเฉียงขึ้นซ้าย-ขวา (เพราะ K เป็นหมากขาว)
        for dx, dy in [(-1, -1), (-1, 1)]:
            nx, ny = x + dx, y + dy #ตรวจว่ามีเบี้ย (P) อยู่ทแยงหน้า 2 ช่องของราชาไหม (เหมือนท่ากินปกติของเบี้ย) ถ้ามี P อยู่ในตำแหน่งนั้น → มีภัยต่อราชา
            if in_bounds(nx, ny) and board[nx][ny] == 'P':
                return True 
        return False
    
    #ไล่ตรวจทิศทางทแยงทั้ง 4 ทิศ ถ้ามี Bishop (B) หรือ Queen (Q) ในทิศทางนั้นแบบไม่มีอะไรกั้น → ถือว่าราชาถูกโจมตี
       #(ส่วนนี้ยังไม่จบในภาพนะ แต่คอนเซปต์คือไล่เช็กแนวทแยง)

    def is_bishop_attacking():
        x, y = king_pos
        for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            nx, ny = x + dx, y + dy
            while in_bounds(nx, ny):
                piece = board[nx][ny]
                if piece == '.':
                    nx += dx
                    ny += dy
                elif piece in ('B', 'Q'):
                    return True
                else:
                    break
        return False

    def is_rook_attacking():
        x, y = king_pos
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            while in_bounds(nx, ny):
                piece = board[nx][ny]
                if piece == '.':
                    nx += dx
                    ny += dy
                elif piece in ('R', 'Q'):
                    return True
                else:
                    break
        return False

    if is_pawn_attacking() or is_bishop_attacking() or is_rook_attacking():
        print("Success")
    else:
        print("Fail")
