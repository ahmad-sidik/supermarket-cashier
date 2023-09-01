class Transaction:
    
    def __init__(self):
        # inisialisasi untuk untuk self-service
        # instance self.order_list digunakan untuk menyimpan nilai pembelian
        self.order_list = {}
        
    def add_item(self, item_info):
        ''' 
        Method ini digunakan untuk menambahkan item transaksi.
        Parameter:
        - item_info berisi list yang terdiri dari nama item, jumlah item, dan harga item
        output:
        - tidak ada
        '''
        # kode di bawah ini digunakan untuk memecah nilai dari parameter `item_info` menjadi `name`, `qty`, dan `price`
        # kemudian ditambahkan ke dalam `self.order_list`
        name, qty, price = item_info
        if name not in self.order_list:
            self.order_list[name] = [qty, price]
        else:
            self.order_list[name][0] += qty         # ini merujuk ke index[0] dari value self.order_list{}
            
    def update_item_name(self, name, update_name):
        '''
        Method ini digunakan untuk mengupdate nama item
        parameter:
        - name adalah nama item yang akan diperbarui
        - update_name adalah nama item yang baru
        output: 
        - Tidak ada
        '''        
        # kode dibawah ini bekerja dengan cara mencocokkan key name yang baru dengan yang lama menggunakan function .pop()
        self.order_list[update_name] = self.order_list.pop(name)
        
    def update_item_qty(self, name, update_qty):
        ''' 
        Method ini digunakan untuk mengupdate jumlah item
        Parameter:
        - name adalah nama item yang akan diubah jumlah itemnya
        - update_qty adalah jumlah barang yang baru
        output:
        - tidak ada
        '''
        # kode di bawah ini digunakan untuk mengupdate jumlah item
        self.order_list[name][0] = update_qty
        
    def update_item_price(self, name, update_price):
        ''' 
        Method ini digunakan untuk mengupdate jumlah item
        Parameter:
        - name adalah nama item yang akan diubah harganya
        - update_price adalah harga item terbaru
        output:
        - tidak ada
        '''
        # kode di bawah ini digunakan untuk mengupdate harga item
        self.order_list[name][1] = update_price
        
    def delete_item(self, name):
        '''
        method ini digunakan untuk menghapus item
        Parameter:
        - name adalah nama item yang akan dihapus
        output:
        - tidak ada
        '''
        # kode di bawah digunakan untuk menghapus item menggunakan `del`
        del self.order_list[name]
        
    def reset_transaction(self):
        ''' 
        method ini digunakan untuk menghapus isi self.order_list()
        Parameter:
        - menggunakan instance dari class Transaction()
        ''' 
        # kode di bawah ini digunakan untuk menghapus semua nilai dari `self.order_list` menggunakan `.clear()`
        self.order_list.clear()
        return 'Semua item berhasil dihapus'
        
    def check_order(self):
        ''' 
        method ini digunakan untuk mengecek orderan user
        parameter:
        - menggunakan instance dari class Transaction()
        '''
        # kode di bawah ini digunakan untuk menghitung total belanja dari masing-masing item dan membuat tabel belanja
        if not self.order_list:
            print('Belum ada item yang dibeli')
        else:
            col_names = '| No |  Nama item  | Jumlah item | Harga/item | Total harga |'
            print(col_names)
            print('-' * len(col_names))
            for index, (name, item_info) in enumerate(self.order_list.items(), start = 1): # dict_items([(name, [qty, price]), ... ])
                qty, price = item_info
                total = qty * price
                print(f"| {index:<2} | {name:<11} | {qty:<11} | {price:<10,.0f} | {total:<11,.0f} |")
            print('-' * len(col_names))
            return ''
        
    def total_price(self):
        ''' 
        method ini digunakan untuk menghitung total belanja
        parameter:
        - menggunakan instance dari class Transaction()
        '''
        # kode di bawah digunakan untuk menghitung total harga
        total_price = 0
        for (name, item_info) in self.order_list.items():
            qty, price = item_info
            total_price += (qty * price)
        
        # kode di bawah digunakan untuk menghitung diskon
        discount = 0
        if total_price > 500_000:
            discount += 0.1
        elif total_price > 300_000:
            discount += 0.08
        elif total_price > 200_000:
            discount += 0.05
        else:
            discount += 0  # Tidak ada diskon jika tidak memenuhi kondisi di atas

        # kode di bawah digunakan untuk menghitung total harga setelah diskon dari total semua item
        discounted_price = total_price - (total_price * discount)
        return discounted_price
