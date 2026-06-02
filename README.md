# Fujitsu Scanner Service - Landing Page

Ini adalah proyek *landing page* responsif dan interaktif untuk layanan perbaikan scanner spesialis Fujitsu, yang dibangun menggunakan ekosistem **Nuxt 4** dan **Tailwind CSS v4**. 

Proyek ini dibangun secara modular menggunakan Vue.js, memanfaatkan transisi halaman *Single Page Application* (SPA), sistem komponen terpisah, dan terintegrasi dengan utilitas form seperti Vuelidate.

## Persyaratan Sistem (Requirements)

Sebelum melakukan instalasi dan pengembangan, pastikan perangkat Anda telah memiliki:
- **Node.js** (Direkomendasikan versi 18.x LTS, 20.x, atau yang lebih baru)
- **NPM** (Otomatis terinstal bersama Node.js)

## Instalasi dan Cara Menjalankan

1. **Instalasi Dependencies**
   Buka terminal atau CMD Anda, arahkan ke folder utama proyek (*root folder*), lalu jalankan:
   ```bash
   npm install
   ```
   *(Proses ini akan mengunduh semua pustaka yang dibutuhkan seperti Nuxt, Vue, Vuelidate, TailwindCSS, dan ikon)*.

2. **Menjalankan Mode Development (Local)**
   Untuk memulai server pengembangan dengan fitur *Hot Module Replacement* (HMR), jalankan:
   ```bash
   npm run dev
   ```
   Buka *browser* Anda dan kunjungi `http://localhost:3000`. Setiap kali Anda menyimpan file, tampilan akan otomatis diperbarui.

3. **Build untuk Produksi (Production)**
   Jika aplikasi sudah siap diluncurkan (deploy), Anda harus melakukan *build* terlebih dahulu:
   ```bash
   npm run build
   ```
   Aplikasi kemudian dapat di-hosting sesuai ekosistem Nitro dari Nuxt.

## Struktur Proyek Utama

- `app/pages/`: Berisi seluruh dokumen rute halaman seperti Beranda (`index.vue`), Layanan (`services.vue`), Kontak (`contact.vue`), dan lain-lain.
- `app/components/global/`: Berisi komponen antar muka permanen seperti navigasi `MainHeader.vue` dan `MainFooter.vue`.
- `app/layouts/`: Mengatur tata letak kerangka utama halaman bawaan Nuxt.
- `nuxt.config.ts`: Konfigurasi inti framework Nuxt.
