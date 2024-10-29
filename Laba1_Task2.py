disk_size_mb = 1.44
pages = 100
lines = 50
chars = 25
bytes_per_char = 4

disk_size_bytes = disk_size_mb * 1024 * 1024

book_size_bytes = pages * lines * chars * bytes_per_char

num_books = disk_size_bytes // book_size_bytes

print("Количество книг, помещающихся на дискету:", int(num_books))