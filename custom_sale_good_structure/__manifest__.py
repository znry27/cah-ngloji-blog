{
    "name": "Custom Sale", # isi bebas
    "author": "Cah Ngloji", # isi bebas
    "version": "1.0.0", # isi bebas
    "category": "Sales", # isi bebas
    'website': 'http://www.cahngloji.blogspot.com', # isi bebas
    'summary': 'Contoh Module', # isi bebas, jangan kelewat panjang
    'description': """
            Deskripsi isi module, isi bebas sesuai keinginan
        """,
    "depends": [
        "sale", # penting, ini menandakan bahwa kita akan menambah / mengurangi fitur module sale, pastikan module sale sudah terinstall
    ],
    "data": [
        "views/custom_sale_view.xml" # penting, isi dengan nama file xml yang sudah kita buat, jangan lupa nama foldernya
    ],
    "license": 'LGPL-3', # isi bebas
    'installable': True # isi bebas
}
