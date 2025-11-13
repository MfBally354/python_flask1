# 📝 Flask To-Do List App

<div align="center">

![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)

**Aplikasi To-Do List sederhana namun powerful untuk mengelola tugas harian Anda**

[Demo](#-demo) • [Fitur](#-fitur) • [Instalasi](#-instalasi) • [Penggunaan](#-penggunaan) • [Pengembangan](#-pengembangan-selanjutnya)

</div>

---

## 🎯 Tentang Proyek

Proyek ini adalah aplikasi web **To-Do List** yang dibangun menggunakan **Flask Framework**. Cocok untuk pemula yang ingin belajar Flask dengan proyek nyata yang fungsional. Aplikasi ini mencakup operasi CRUD (Create, Read, Update, Delete) lengkap dengan antarmuka yang modern dan responsif.

### 🎓 Konsep yang Dipelajari

Melalui proyek ini, Anda akan mempelajari:

- ✅ **Flask Routing** - Mengelola URL dan endpoint
- ✅ **HTTP Methods** - GET dan POST request
- ✅ **Template Engine** - Jinja2 untuk dynamic HTML
- ✅ **Flash Messages** - Notifikasi feedback ke user
- ✅ **Static Files** - Mengelola CSS dan assets
- ✅ **Form Handling** - Input validation dan processing
- ✅ **CRUD Operations** - Create, Read, Update, Delete data
- ✅ **URL Building** - Menggunakan url_for()
- ✅ **Error Handling** - Custom error pages

## ✨ Fitur

### Fitur Utama
- 📌 **Tambah Task Baru** - Buat to-do dengan mudah
- ✔️ **Toggle Completion** - Tandai task selesai/belum selesai
- 🗑️ **Hapus Task** - Hapus task individual atau semua sekaligus
- 📊 **Statistik Real-time** - Monitor progress task Anda
- 💬 **Flash Notifications** - Feedback visual untuk setiap aksi
- 🎨 **Modern UI/UX** - Design gradien yang menarik
- 📱 **Responsive Design** - Optimal di desktop dan mobile
- ⚡ **Fast & Lightweight** - Performa yang cepat

### Fitur Teknis
- 🔄 Dynamic content rendering dengan Jinja2
- 🎭 Smooth animations dan transitions
- 🛡️ Input validation
- 📅 Timestamp untuk setiap task
- 🎯 Clean code structure

## 📸 Demo

### Tampilan Utama
```
┌─────────────────────────────────────────┐
│         📝 My To-Do List                │
│   Kelola tugas harianmu dengan mudah    │
│                                         │
│  ┌────────────────────────────────┐    │
│  │ Tambahkan task baru...    ➕   │    │
│  └────────────────────────────────┘    │
│                                         │
│  ┌─────┐  ┌─────┐  ┌─────┐            │
│  │  3  │  │  1  │  │  2  │            │
│  │Total│  │Done │  │Todo │            │
│  └─────┘  └─────┘  └─────┘            │
│                                         │
│  ✅ Belajar Flask routing               │
│  ☐  Membuat REST API                    │
│  ☐  Deploy ke production                │
└─────────────────────────────────────────┘
```

## 🛠️ Teknologi

| Teknologi | Versi | Deskripsi |
|-----------|-------|-----------|
| Python | 3.x | Backend language |
| Flask | 3.x | Web framework |
| Jinja2 | 3.x | Template engine |
| HTML5 | - | Markup language |
| CSS3 | - | Styling |

## 📋 Prasyarat

Sebelum memulai, pastikan Anda sudah menginstall:

- **Python 3.7+** - [Download Python](https://www.python.org/downloads/)
- **pip** - Python package manager (biasanya sudah terinstall dengan Python)
- **Text Editor** - VS Code, Sublime, atau editor favorit Anda

Cek instalasi Python:
```bash
python3 --version
pip3 --version
```

## 🚀 Instalasi

### 1️⃣ Clone Repository

```bash
git clone https://github.com/username/flask-todo-app.git
cd flask-todo-app
```

### 2️⃣ Buat Virtual Environment (Recommended)

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install flask
```

Atau jika menggunakan requirements.txt:
```bash
pip install -r requirements.txt
```

### 4️⃣ Struktur Folder

Pastikan struktur folder Anda seperti ini:

```
flask_todo/
│
├── app.py                 # File utama Flask application
├── requirements.txt       # Python dependencies
├── README.md             # Dokumentasi (file ini)
│
├── templates/            # Folder HTML templates
│   └── index.html       # Template halaman utama
│
└── static/              # Folder static files
    └── style.css        # CSS styling
```

## ▶️ Cara Menjalankan

### Development Mode

```bash
# Pastikan Anda di direktori proyek
cd flask_todo

# Jalankan aplikasi
python3 app.py
```

Output yang diharapkan:
```
🚀 Flask To-Do App berjalan di http://localhost:5000
📝 Tekan CTRL+C untuk menghentikan server
 * Running on http://0.0.0.0:5000
```

### Akses Aplikasi

Buka browser dan kunjungi:
- **Local:** `http://localhost:5000`
- **Network:** `http://<IP-ADDRESS>:5000`

### Hentikan Server

Tekan `CTRL + C` di terminal

## 📖 Penggunaan

### Menambah Task Baru
1. Ketik task di input field
2. Klik tombol "➕ Tambah" atau tekan Enter
3. Task akan muncul di daftar

### Menandai Task Selesai
1. Klik checkbox di sebelah task
2. Task akan dicoret dan ditandai selesai
3. Klik lagi untuk menandai belum selesai

### Menghapus Task
1. Klik tombol ❌ di sebelah kanan task
2. Konfirmasi penghapusan
3. Task akan dihapus dari daftar

### Menghapus Semua Task
1. Klik tombol "🗑️ Hapus Semua"
2. Konfirmasi penghapusan
3. Semua task akan dibersihkan

## 📁 Penjelasan Kode

### app.py - Backend Logic

```python
@app.route('/')
def index():
    """Menampilkan halaman utama dengan semua task"""
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add_todo():
    """Menambahkan task baru ke daftar"""
    # Logic untuk validasi dan menambah task
    
@app.route('/complete/<int:todo_id>')
def complete_todo(todo_id):
    """Toggle status completed task"""
    # Logic untuk mengubah status task
```

### index.html - Frontend Template

Menggunakan Jinja2 template engine:
```html
{% for todo in todos %}
    <li class="todo-item {% if todo.completed %}completed{% endif %}">
        {{ todo.task }}
    </li>
{% endfor %}
```

### style.css - Styling

Modern design dengan:
- Gradient backgrounds
- Smooth animations
- Responsive layout
- Glassmorphism effects

## 🔧 Konfigurasi

### Mengubah Port

Edit bagian ini di `app.py`:
```python
app.run(host='0.0.0.0', port=5000, debug=True)
```

Ganti `5000` dengan port yang diinginkan.

### Debug Mode

Debug mode sudah aktif (`debug=True`). Untuk production, ubah menjadi `False`:
```python
app.run(debug=False)
```

### Secret Key

Ganti secret key di `app.py` untuk keamanan:
```python
app.secret_key = 'ganti_dengan_kunci_rahasia_yang_kuat'
```

## 🎯 Pengembangan Selanjutnya

Ide untuk meningkatkan aplikasi:

### Level Beginner
- [ ] Tambah fitur edit task
- [ ] Implementasi kategori/tag
- [ ] Filter task (All/Active/Completed)
- [ ] Search functionality
- [ ] Sort by date/alphabet

### Level Intermediate
- [ ] Integrasi database SQLite/PostgreSQL
- [ ] User authentication & authorization
- [ ] Due date & reminder
- [ ] Priority levels (High/Medium/Low)
- [ ] Task notes/description

### Level Advanced
- [ ] REST API endpoints
- [ ] Multiple users support
- [ ] Real-time updates (WebSocket)
- [ ] Export/Import tasks (JSON/CSV)
- [ ] Analytics dashboard
- [ ] Mobile app (React Native/Flutter)
- [ ] Email notifications
- [ ] Collaborative tasks

## 🐛 Troubleshooting

### Port Already in Use

**Problem:** Port 5000 sudah digunakan aplikasi lain

**Solution:**
```bash
# Cari process yang menggunakan port
sudo lsof -i :5000

# Kill process tersebut
kill -9 <PID>

# Atau gunakan port lain di app.py
```

### Module Not Found

**Problem:** `ModuleNotFoundError: No module named 'flask'`

**Solution:**
```bash
# Pastikan virtual environment aktif
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Install Flask
pip install flask
```

### Template Not Found

**Problem:** `jinja2.exceptions.TemplateNotFound: index.html`

**Solution:**
- Pastikan folder `templates/` ada
- Pastikan `index.html` ada di dalam folder `templates/`
- Cek nama file (case-sensitive)

### CSS Not Loading

**Problem:** Styling tidak muncul

**Solution:**
- Pastikan folder `static/` ada
- Pastikan `style.css` ada di dalam folder `static/`
- Clear browser cache (Ctrl+F5)
- Cek console browser untuk errors

## 📚 Resources & Learning

### Dokumentasi
- [Flask Official Docs](https://flask.palletsprojects.com/)
- [Jinja2 Documentation](https://jinja.palletsprojects.com/)
- [Python Official Docs](https://docs.python.org/3/)

### Tutorial
- [Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
- [Real Python Flask Tutorials](https://realpython.com/tutorials/flask/)
- [Flask by Example](https://realpython.com/learning-paths/flask-by-example/)

### Video
- [Corey Schafer - Flask Tutorial](https://www.youtube.com/playlist?list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH)
- [Tech With Tim - Flask Series](https://www.youtube.com/watch?v=mqhxxeeTbu0)

## 🤝 Kontribusi

Kontribusi sangat diterima! Berikut cara berkontribusi:

1. Fork repository ini
2. Buat branch baru (`git checkout -b feature/AmazingFeature`)
3. Commit perubahan (`git commit -m 'Add some AmazingFeature'`)
4. Push ke branch (`git push origin feature/AmazingFeature`)
5. Buat Pull Request

### Panduan Kontribusi
- Ikuti style code yang ada
- Tulis commit message yang jelas
- Update dokumentasi jika diperlukan
- Test sebelum submit PR

## 📝 Changelog

### Version 1.0.0 (2024-11-13)
- ✨ Initial release
- ✅ CRUD functionality lengkap
- 🎨 Modern responsive UI
- 📊 Task statistics
- 💬 Flash messages
- 🎯 Sample tasks untuk demo

## 📄 Lisensi

Proyek ini menggunakan lisensi **MIT License**. Lihat file `LICENSE` untuk detail lengkap.

```
MIT License

Copyright (c) 2024

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...
```

## 👤 Author

**Iqbal**

- GitHub: [@iqbal](https://github.com/iqbal)
- Email: iqbal@example.com

## 🙏 Acknowledgments

- Flask framework dari Pallets Projects
- Inspirasi design dari berbagai sumber
- Komunitas Python Indonesia
- Stack Overflow community

## ⭐ Support

Jika proyek ini membantu Anda, berikan ⭐ di repository ini!

### Cara Support Lainnya:
- 🐛 Report bugs di Issues
- 💡 Berikan saran improvement
- 📢 Share ke teman-teman
- ☕ [Buy me a coffee](https://buymeacoffee.com/)

---

<div align="center">

**Dibuat dengan ❤️ menggunakan Flask**

**Happy Coding! 🚀**

[![Made with Flask](https://img.shields.io/badge/Made%20with-Flask-000000?style=flat&logo=flask)](https://flask.palletsprojects.com/)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-3776AB?style=flat&logo=python)](https://www.python.org/)

</div>
