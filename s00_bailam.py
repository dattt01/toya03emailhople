#region debai
"""
--- ma debai / id
get_name_in_email(email_list)

--- nopbai
00 fork tu bainopmau tren replit tu trang web duoiday 
   https://replit.com/@NamG1/toya03emailhople

01 lam bai vao tep s00_bailam.py, chay Run de co ketqua tatca la 1
02a tao github repo, mo trinhduyetweb de kiemtra tep s00_bailam.py, va lay diachi/url aka githubbailamurl

02b dán diachi githubbailamurl theo mẫu ở trang web duoiday
    https://forms.gle/ZwjSxkx9mEqhL8mj6

--- debai / problem
Viết hàm 
  get_name_in_email(email_list)
trả về tên tài khoản trong email 
Nếu email không hợp lệ, trả về 'ERROR invaid email'

--- vidu mau / testcase
Khi chay voi input                                        | Ketqua output
--------------------------------------------------------- | -----------------
get_name_in_email(['ai-btx@gmail.com'])                   | ['ai-btx']
get_name_in_email(['user1@gmail.com', 'user2@gmail.com']) | ['user1', 'user2']
get_name_in_email([])                                     | []
get_name_in_email(['abb#ccc'])                            | ['ERROR invaid email']
get_name_in_email([None])                                 | ['ERROR invaid email']
get_name_in_email([None, 'abb#ccc'])                      | ['ERROR invaid email', 'ERROR invaid email']
"""

#endregion debai

#region bailam


def get_name_in_email(email_list):
  dc_email = []  # dia chi email
  for i in range(len(email_list)):
    ttk_email = email_list[i]  #phan tu trong mang email_list
    if ttk_email is not None:
      if ttk_email.find('@') >= 0:  #tim vi tri @ trong chuoi ky tu
        ten_hople = ttk_email[0:ttk_email.index('@')]  # tach ten hop le trong dia chi mail
        dc_email.append(ten_hople)
      else:
        dc_email.append('ERROR invaid email')
    else:
      dc_email.append('ERROR invaid email')
  return dc_email
 

if __name__ == '__main__':
  pass
#endregion bailam
