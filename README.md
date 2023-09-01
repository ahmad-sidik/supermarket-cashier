# supermarket-cashier

## Background

Andi adalah seorang pemilik supermarket terbesar di Indonesia. Andi ingin melakukan perbaikan proses bisnis yaitu dengan cara membuat aplikasi kasir _self-service_ sehingga para konsumen dapat memasukkan item yang dibeli, jumlah item yang dibeli, dan harganya. Andi juga memberikan diskon kepada para customer. Customer yang belanja lebih dari 200.000 mendapatkan diskon sebesar 5%, 300.000 mendapatkan diskon 8%, dan 500.000 mendapatkan diskon 10%.

## Tujuan

Aplikasi ini bertujuan agar memudahkan customer melakukan pengecekan belanja mereka sendiri sebelum melakukan pembayaran.

## Deskripsi

Dalam repo ini terdapat dua file `.py` yaitu script `main.py` dan modul `script_cashier.py`. `main.py` digunakan untuk menjalankan aplikasi dan `script_cashier.py` digunakan untuk menyimpan fitur-fitur aplikasi.

### Fitur-fitur `script_cashier.py` 

- `self.order_list` digunakan untuk menyimpan list belanjaan user
- `add_item()` digunakan untuk menambahkan item belanja yang disimpan di `self.order_list`
- `update_item_name()` digunakan untuk mengupdate nama item
- `update_item_qty` digunakan untuk mengupdate jumlah item
- `update_item_price()` digunakan untuk mengupdate harga item
- `delete_item()` digunakan untuk meghapus item
- `reset_transaction` digunakan untuk menghapus semua item
- `check_order` digunakan untuk mengecek semua daftar belanja
- `total_price` digunakan untuk mengecek harga total setelah diskon

### Flowchart

### Penjelasan Kode `script_cashier.py`

- `self.order_list` adalah inisialisasi untuk menyimpan nilai
```python
    def __init__(self):
        
        # inisialisasi untuk untuk self-service
        # instance self.order_list digunakan untuk menyimpan nilai pembelian
        self.order_list = {}
```
- `add_item` berisi kode yang digunakan untuk mengecek tipe data input dan menambahkan item namun jika nama item sudah sama maka yang akan ditambah adalah jumlah itemnya
```py
def add_item(self, item_info):
        ''' 
        Method ini digunakan untuk menambahkan item transaksi.
        Parameter:
        - item_info berisi list yang terdiri dari nama item, jumlah item, dan harga item
        output:
        - tidak ada
        '''
        # jika sudah input yang dimasukkan sudah benar maka tinggal dilanjutkan brancing di bawah ini
        name, qty, price = item_info
        # brancing di bawah ini digunakan untuk mengecek apakah tipe data yang diinput sudah benar
        if not isinstance(name, str):
            raise ValueError('Harap masukkan nama item dengan benar')
        if not isinstance(qty, int) and item_info[1] < 1:
            raise ValueError('Harap masukkan jumlah item dengan benar')
        if not isinstance(price, int) and item_info[2] % 1000 != 0:
            raise ValueError('Harap masukkan harga item dengan benar')
        if name not in self.order_list:
            self.order_list[name] = [qty, price]
        else:
            self.order_list[name][0] += qty         # ini merujuk ke index[0] dari value self.order_list{}
```
- `update_item_name()`
```py
def update_item_name(self, name, update_name):
        '''
        Method ini digunakan untuk mengupdate nama item
        
        parameter:
        - name adalah nama item yang akan diperbarui
        - update_name adalah nama item yang baru
        
        output: 
        - Tidak ada
        '''
        # kode digunakan untuk mengecek apakah name ada dalam self.order_list
        if name not in self.order_list:
            raise ValueError(f'Item {name} tidak ada dalam daftar pembelian')
        
        # kode dibawah ini bekerja dengan cara mencocokkan key name yang baru dengan yang lama menggunakan function .pop()
        self.order_list[update_name] = self.order_list.pop(name)
```
