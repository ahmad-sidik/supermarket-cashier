from script_cashier import Transaction

trnsc = Transaction()

def main():
    print('Selamat datang di aplikasi self-service supermarket Andi')
    print('Melalui aplikasi ini Anda dapat memastikan serta menghitung pesanan Anda')
    print('Pertama masukkan item belanja Anda!')
    while True:
        try:
            while True:
                    
                nama_item = str(input('Masukkan nama item yang Anda beli : '))
                qty = int(input(f'Masukkan jumlah {nama_item.lower()} yang Anda beli : '))
                price = int(input(f'Masukkan harga {nama_item.lower()} : '))
            
                trnsc.add_item([nama_item, qty, price])
                cont_add_item = str(input('Apakah Anda ingin menambahkan item lagi? (Ya/Tidak) : '))
                
                    
                if cont_add_item == 'Ya':
                    continue
                elif cont_add_item == 'Tidak':
                    break
                elif cont_add_item != 'Ya' or cont_add_item != 'Tidak':
                    print('Harap masukkan input Ya atau Tidak ')
            
            while True:
                check_update_name = str(input('Apakah Anda ingin mengubah nama item yang Anda beli? (Ya/Tidak) : '))
                if check_update_name == 'Ya':
                    name = str(input('Masukkan nama item yang ingin Anda perbarui : '))
                    update_name = str(input(f'Masukkan nama baru untuk item {name.lower()} : '))
                    trnsc.update_item_name(name, update_name)
                elif check_update_name == 'Tidak':
                    break
                elif check_update_name != 'Ya' or check_update_name != 'Tidak':
                    print('Harap masukkan input Ya atau Tidak ')
                
            while True:
                check_qty = str(input('Apakah Anda ingin mengubah jumlah item yang Anda beli? (Ya/Tidak) : '))
                if check_qty == 'Ya':
                    name = str(input('Masukkan nama item yang ingin Anda ubah jumlahnya : '))
                    update_qty = int(input(f'Masukkan jumlah {name.lower()} yang baru : '))
                    trnsc.update_item_qty(name, update_qty)
                elif check_qty == 'Tidak':
                    break
                elif check_qty != 'Ya' or check_qty != 'Tidak':
                    print('Harap masukkan input Ya atau Tidak ')
                
            while True:
                check_price = str(input('Apakah Anda ingin mengubah harga item yang Anda beli? (Ya/Tidak) : '))
                if check_price == 'Ya':
                    name = str(input('Masukkan nama item yang ingin Anda ubah harganya : '))
                    update_price = int(input(f'Masukkan harga {name.lower()} yang baru : '))
                    trnsc.update_item_price(name, update_price)
                elif check_price == 'Tidak':
                    break
                elif check_price != 'Ya' or check_price != 'Tidak':
                    print('Harap masukkan input Ya atau Tidak ')
                
            
            while True:
                choice = str(input('Apakah Anda ingin menghapus item tertentu atau menghapus semua pesanan? (Ya/Tidak) : '))
                if choice == 'Tidak':
                    break
                elif choice == 'Ya':
                    del_or_reset = str(input('Hapus item / menghapus semua pesanan (Hapus/Reset)'))
                    if del_or_reset == 'Hapus':
                        name = str(input('Masukkan nama item yang ingin Anda hapus : '))
                        trnsc.delete_item(name)
                        break
                    elif del_or_reset == 'Reset':
                        trnsc.reset_transaction()
                        break
                    elif del_or_reset != 'Hapus' or del_or_reset != 'Reset':
                        print('Harap masukkan input Hapus atau Reset ')
                elif choice != 'Ya' or choice != 'Tidak':
                    print('Harap masukkan input Ya atau Tidak ')
            
            ending_sentence = 'Setelah Anda mengubah isi pesanan berikut adalah tabel pesanan Anda'
            print(ending_sentence)
            print('=' * len(ending_sentence))
            trnsc.check_order()
            print('=' * len(ending_sentence))
            print('Jika total belanja Anda melebihi 200.000 Anda mendapatkan diskon 5%')
            print('Jika total belanja Anda melebihi 300.000 Anda mendapatkan diskon 8%')
            print('Jika total belanja Anda melebihi 500.000 Anda mendapatkan diskon 10%')
            print(f'Berikut adalah total belanja Anda {int(trnsc.total_price())}')
            print('Terima kasih karena mempercayakan kebutuhan Anda kepada kami :)')
            break
        except ValueError: print('Maaf ada kesalahan pada input yang Anda masukkan')
        except Exception as e:
            print(e)
        
if __name__ == '__main__':
    main()