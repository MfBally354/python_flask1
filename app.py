"""
Flask To-Do List App - Proyek Pembelajaran untuk Pemula
File: app.py

Struktur folder yang dibutuhkan:
flask_todo/
├── app.py
├── templates/
│   └── index.html
└── static/
    └── style.css
"""

from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'kunci_rahasia_untuk_flash_message'

# Simulasi database dengan list (untuk pemula)
# Nanti bisa diganti dengan database real seperti SQLite
todos = []

@app.route('/')
def index():
    """Halaman utama - menampilkan semua to-do"""
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add_todo():
    """Menambah to-do baru"""
    task = request.form.get('task')
    
    if task and task.strip():  # Validasi input tidak kosong
        new_todo = {
            'id': len(todos) + 1,
            'task': task.strip(),
            'completed': False,
            'created_at': datetime.now().strftime('%d/%m/%Y %H:%M')
        }
        todos.append(new_todo)
        flash('Task berhasil ditambahkan! ✅', 'success')
    else:
        flash('Task tidak boleh kosong! ⚠️', 'warning')
    
    return redirect(url_for('index'))

@app.route('/complete/<int:todo_id>')
def complete_todo(todo_id):
    """Menandai to-do sebagai selesai"""
    for todo in todos:
        if todo['id'] == todo_id:
            todo['completed'] = not todo['completed']  # Toggle status
            status = 'selesai' if todo['completed'] else 'belum selesai'
            flash(f'Task ditandai sebagai {status}! 🎯', 'info')
            break
    return redirect(url_for('index'))

@app.route('/delete/<int:todo_id>')
def delete_todo(todo_id):
    """Menghapus to-do"""
    global todos
    todos = [todo for todo in todos if todo['id'] != todo_id]
    flash('Task berhasil dihapus! 🗑️', 'danger')
    return redirect(url_for('index'))

@app.route('/clear')
def clear_all():
    """Menghapus semua to-do"""
    global todos
    todos.clear()
    flash('Semua task berhasil dihapus! 🧹', 'info')
    return redirect(url_for('index'))

# Error handler untuk halaman tidak ditemukan
@app.errorhandler(404)
def page_not_found(e):
    return render_template('index.html', todos=todos), 404

if __name__ == '__main__':
    # Menambahkan beberapa contoh task untuk demo
    todos = [
        {
            'id': 1,
            'task': 'Belajar Flask routing',
            'completed': False,
            'created_at': datetime.now().strftime('%d/%m/%Y %H:%M')
        },
        {
            'id': 2,
            'task': 'Membuat template HTML',
            'completed': True,
            'created_at': datetime.now().strftime('%d/%m/%Y %H:%M')
        }
    ]
    
    print("🚀 Flask To-Do App berjalan di http://localhost:5000")
    print("📝 Tekan CTRL+C untuk menghentikan server")
    app.run(host='0.0.0.0', port=5000, debug=True)
