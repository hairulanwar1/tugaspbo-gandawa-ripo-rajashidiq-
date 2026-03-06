class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Restoran:", self.restaurant_name)
        print("Tipe Masakan:", self.cuisine_type)

    def open_restaurant(self):
        print("Restoran", self.restaurant_name, "sedang buka untuk pelanggan.")


# Membuat objek restoran
my_resto = Restaurant("Warung Nusantara", "Masakan Indonesia")

# Menampilkan atribut
print("Nama Restoran:", my_resto.restaurant_name)
print("Jenis Masakan:", my_resto.cuisine_type)

# Memanggil method
my_resto.describe_restaurant()
my_resto.open_restaurant()


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Nama Restoran :", self.restaurant_name)
        print("Menu Utama    :", self.cuisine_type)
        print("-" * 30)


# Membuat beberapa objek restoran
restaurant1 = Restaurant("Sushi Tokyo", "Masakan Jepang")
restaurant2 = Restaurant("Pizza Italia", "Masakan Italia")
restaurant3 = Restaurant("Padang Sederhana", "Masakan Padang")

# Menampilkan informasi restoran
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()


class User:
    def __init__(self, first_name, last_name, age, email, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.city = city

    def describe_user(self):
        print("Nama Lengkap :", self.first_name, self.last_name)
        print("Umur         :", self.age)
        print("Email        :", self.email)
        print("Asal Kota    :", self.city)

    def greet_user(self):
        print("Halo", self.first_name + ",", "senang bertemu denganmu!")
        print()


# Membuat objek user
user_a = User("Gandawa", "Gan", 17, "Gandawaripo@email.com", "Pekanbaru")
user_b = User("Budi", "Santoso", 20, "budi@email.com", "Jakarta")
user_c = User("Siti", "Aisyah", 19, "siti@email.com", "Bandung")

# Menjalankan method
user_a.describe_user()
user_a.greet_user()

user_b.describe_user()
user_b.greet_user()

user_c.describe_user()
user_c.greet_user()